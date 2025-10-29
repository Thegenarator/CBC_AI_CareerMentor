"""
M-Pesa Integration Module for AI CareerMentor Kenya
Handles STK Push, payment verification, and subscription management
"""

import requests
import base64
import json
import hashlib
import time
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()

class MpesaIntegration:
    def __init__(self):
        # M-Pesa API Configuration
        # Using provided credentials from Safaricom Developer Portal
        self.consumer_key = os.getenv('MPESA_CONSUMER_KEY', 'GnMdAhLo9w1oGUApZpWh9myVB0G35tTqchfkKAdhtmifCeoK')
        self.consumer_secret = os.getenv('MPESA_CONSUMER_SECRET', 'Pr1n6TFKcMqj7iYkVfA7HnvQAnUeYO2MBcx8SbGScVyQAGDXOSADiInJ7gGdxtpD')
        self.business_shortcode = os.getenv('MPESA_BUSINESS_SHORTCODE', '174379')
        self.passkey = os.getenv('MPESA_PASSKEY')
        self.callback_url = os.getenv('MPESA_CALLBACK_URL', 'https://your-domain.com/mpesa/callback')
        self.environment = os.getenv('MPESA_ENVIRONMENT', 'sandbox')  # sandbox or production
        
        # API URLs
        if self.environment == 'sandbox':
            self.base_url = 'https://sandbox.safaricom.co.ke'
        else:
            self.base_url = 'https://api.safaricom.co.ke'
        
        self.oauth_url = f"{self.base_url}/oauth/v1/generate?grant_type=client_credentials"
        self.stk_push_url = f"{self.base_url}/mpesa/stkpush/v1/processrequest"
        self.stk_query_url = f"{self.base_url}/mpesa/stkpushquery/v1/query"
        
        # Access token cache
        self.access_token = None
        self.token_expires_at = None

    def get_access_token(self):
        """Get OAuth access token from M-Pesa API"""
        try:
            # Check if token is still valid
            if self.access_token and self.token_expires_at and datetime.now() < self.token_expires_at:
                return self.access_token
            
            # Generate new token
            auth_string = f"{self.consumer_key}:{self.consumer_secret}"
            encoded_auth = base64.b64encode(auth_string.encode()).decode()
            
            headers = {
                'Authorization': f'Basic {encoded_auth}',
                'Content-Type': 'application/json'
            }
            
            response = requests.get(self.oauth_url, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            self.access_token = data['access_token']
            # Token expires in 1 hour, refresh 5 minutes early
            self.token_expires_at = datetime.now() + timedelta(minutes=55)
            
            return self.access_token
            
        except Exception as e:
            print(f"Error getting access token: {e}")
            return None

    def generate_timestamp(self):
        """Generate timestamp in YYYYMMDDHHMMSS format"""
        return datetime.now().strftime('%Y%m%d%H%M%S')

    def generate_password(self, timestamp):
        """Generate password for STK Push"""
        password_string = f"{self.business_shortcode}{self.passkey}{timestamp}"
        return base64.b64encode(password_string.encode()).decode()

    def initiate_stk_push(self, phone_number, amount, account_reference, transaction_desc):
        """
        Initiate STK Push payment request
        
        Args:
            phone_number: Customer's phone number (format: 254XXXXXXXXX)
            amount: Amount to charge
            account_reference: Unique reference for the transaction
            transaction_desc: Description of the transaction
        """
        try:
            access_token = self.get_access_token()
            if not access_token:
                return {"error": "Failed to get access token"}

            timestamp = self.generate_timestamp()
            password = self.generate_password(timestamp)

            # Format phone number (remove + and ensure it starts with 254)
            if phone_number.startswith('+'):
                phone_number = phone_number[1:]
            if phone_number.startswith('0'):
                phone_number = '254' + phone_number[1:]
            if not phone_number.startswith('254'):
                phone_number = '254' + phone_number

            payload = {
                "BusinessShortCode": self.business_shortcode,
                "Password": password,
                "Timestamp": timestamp,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": int(amount),
                "PartyA": phone_number,
                "PartyB": self.business_shortcode,
                "PhoneNumber": phone_number,
                "CallBackURL": self.callback_url,
                "AccountReference": account_reference,
                "TransactionDesc": transaction_desc
            }

            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }

            response = requests.post(self.stk_push_url, json=payload, headers=headers)
            response.raise_for_status()
            
            return response.json()

        except Exception as e:
            print(f"Error initiating STK Push: {e}")
            return {"error": str(e)}

    def query_stk_push_status(self, checkout_request_id):
        """Query the status of an STK Push transaction"""
        try:
            access_token = self.get_access_token()
            if not access_token:
                return {"error": "Failed to get access token"}

            timestamp = self.generate_timestamp()
            password = self.generate_password(timestamp)

            payload = {
                "BusinessShortCode": self.business_shortcode,
                "Password": password,
                "Timestamp": timestamp,
                "CheckoutRequestID": checkout_request_id
            }

            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }

            response = requests.post(self.stk_query_url, json=payload, headers=headers)
            response.raise_for_status()
            
            return response.json()

        except Exception as e:
            print(f"Error querying STK Push status: {e}")
            return {"error": str(e)}

    def process_callback(self, callback_data):
        """Process M-Pesa callback data"""
        try:
            # Parse callback data
            if isinstance(callback_data, str):
                callback_data = json.loads(callback_data)
            
            # Extract transaction details
            result_code = callback_data.get('Body', {}).get('stkCallback', {}).get('ResultCode')
            result_desc = callback_data.get('Body', {}).get('stkCallback', {}).get('ResultDesc')
            checkout_request_id = callback_data.get('Body', {}).get('stkCallback', {}).get('CheckoutRequestID')
            
            if result_code == 0:  # Success
                callback_metadata = callback_data.get('Body', {}).get('stkCallback', {}).get('CallbackMetadata', {}).get('Item', [])
                
                # Extract payment details
                amount = None
                mpesa_receipt_number = None
                transaction_date = None
                phone_number = None
                
                for item in callback_metadata:
                    if item.get('Name') == 'Amount':
                        amount = item.get('Value')
                    elif item.get('Name') == 'MpesaReceiptNumber':
                        mpesa_receipt_number = item.get('Value')
                    elif item.get('Name') == 'TransactionDate':
                        transaction_date = item.get('Value')
                    elif item.get('Name') == 'PhoneNumber':
                        phone_number = item.get('Value')
                
                return {
                    "success": True,
                    "checkout_request_id": checkout_request_id,
                    "amount": amount,
                    "mpesa_receipt_number": mpesa_receipt_number,
                    "transaction_date": transaction_date,
                    "phone_number": phone_number,
                    "result_desc": result_desc
                }
            else:
                return {
                    "success": False,
                    "checkout_request_id": checkout_request_id,
                    "result_code": result_code,
                    "result_desc": result_desc
                }
                
        except Exception as e:
            print(f"Error processing callback: {e}")
            return {"error": str(e)}

# Subscription Management
class SubscriptionManager:
    def __init__(self, db):
        self.db = db
        self.subscription_plans = {
            "basic": {
                "name": "Basic Plan",
                "price": 300,
                "duration_days": 30,
                "features": ["20 AI interactions/month", "Basic CV generation", "Pathway exploration", "1 premium feature/month"]
            },
            "premium": {
                "name": "Premium Plan", 
                "price": 500,
                "duration_days": 30,
                "features": ["Unlimited AI interactions", "All premium features", "Priority support", "Advanced analytics", "PDF downloads"]
            },
            "professional": {
                "name": "Professional Plan",
                "price": 1000,
                "duration_days": 30,
                "features": ["Everything in Premium", "Bulk CV generation", "Team management", "Advanced analytics dashboard", "API access"]
            }
        }

    def create_subscription(self, user_id, plan_type, payment_reference):
        """Create a new subscription for a user"""
        try:
            plan = self.subscription_plans.get(plan_type)
            if not plan:
                return {"error": "Invalid plan type"}

            subscription_data = {
                "user_id": user_id,
                "plan_type": plan_type,
                "plan_name": plan["name"],
                "price": plan["price"],
                "payment_reference": payment_reference,
                "start_date": datetime.now(),
                "end_date": datetime.now() + timedelta(days=plan["duration_days"]),
                "status": "active",
                "created_at": datetime.now()
            }

            # Save to Firebase
            doc_ref = self.db.collection("subscriptions").add(subscription_data)
            return {"success": True, "subscription_id": doc_ref[1].id}

        except Exception as e:
            print(f"Error creating subscription: {e}")
            return {"error": str(e)}

    def check_subscription_status(self, user_id):
        """Check if user has an active subscription"""
        try:
            subscriptions = self.db.collection("subscriptions").where("user_id", "==", user_id).where("status", "==", "active").stream()
            
            for sub in subscriptions:
                sub_data = sub.to_dict()
                if sub_data["end_date"] > datetime.now():
                    return {
                        "active": True,
                        "plan_type": sub_data["plan_type"],
                        "plan_name": sub_data["plan_name"],
                        "end_date": sub_data["end_date"],
                        "features": self.subscription_plans[sub_data["plan_type"]]["features"]
                    }
            
            return {"active": False}

        except Exception as e:
            print(f"Error checking subscription status: {e}")
            return {"error": str(e)}

    def get_plan_details(self, plan_type):
        """Get details for a specific plan"""
        return self.subscription_plans.get(plan_type)

    def get_all_plans(self):
        """Get all available subscription plans"""
        return self.subscription_plans

