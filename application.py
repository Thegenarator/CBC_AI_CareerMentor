"""
WSGI Entry Point for AWS Elastic Beanstalk Deployment
This file allows Elastic Beanstalk to run the Flask application.
"""
import os
from app import app

# Elastic Beanstalk expects 'application' variable
application = app

if __name__ == "__main__":
    # For local testing
    application.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)

