#!/bin/bash
# AWS EC2 Deployment Script
# This script sets up the application on an EC2 instance

set -e  # Exit on error

echo "🚀 Starting AWS EC2 Deployment Setup..."

# Update system
echo "📦 Updating system packages..."
sudo yum update -y

# Install Python 3.9 or later
echo "🐍 Installing Python 3..."
sudo yum install -y python3 python3-pip git

# Verify Python version (ensure compatibility)
python3 --version

# Install PostgreSQL client libraries (if needed for future DB)
sudo yum install -y postgresql-devel

# Install Gunicorn for production WSGI server
echo "⚙️ Installing Gunicorn..."
pip3 install gunicorn

# Create application directory
APP_DIR="/var/www/cbc_ai"
echo "📁 Creating application directory at $APP_DIR..."
sudo mkdir -p $APP_DIR
sudo chown -R ec2-user:ec2-user $APP_DIR

# Clone or copy application files
echo "📥 Setting up application files..."
cd $APP_DIR

# If using git, uncomment:
# git clone https://github.com/Thegenarator/CBC_AI_CareerMentor.git .

# Install Python dependencies
echo "📚 Installing Python dependencies..."
pip3 install -r requirements.txt

# Create systemd service file
echo "🔧 Creating systemd service..."
sudo tee /etc/systemd/system/cbc-ai.service > /dev/null <<EOF
[Unit]
Description=CBC AI CareerMentor Flask Application
After=network.target

[Service]
User=ec2-user
Group=ec2-user
WorkingDirectory=$APP_DIR
Environment="PATH=$APP_DIR/venv/bin:$PATH"
EnvironmentFile=$APP_DIR/.env
ExecStart=/usr/local/bin/gunicorn --bind 0.0.0.0:8000 --workers 3 --timeout 120 application:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Create Nginx configuration
echo "🌐 Configuring Nginx..."
sudo tee /etc/nginx/conf.d/cbc-ai.conf > /dev/null <<EOF
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    # Redirect HTTP to HTTPS (uncomment after setting up SSL)
    # return 301 https://\$server_name\$request_uri;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_read_timeout 120s;
    }

    location /static {
        alias $APP_DIR/static;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
EOF

# Install and configure Nginx
sudo yum install -y nginx
sudo systemctl enable nginx
sudo systemctl start nginx

# Configure firewall
echo "🔥 Configuring firewall..."
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload

# Enable and start the application service
echo "🎯 Enabling application service..."
sudo systemctl daemon-reload
sudo systemctl enable cbc-ai
# Don't start yet - need to set up .env first
# sudo systemctl start cbc-ai

echo "✅ Deployment setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Copy your .env file to $APP_DIR"
echo "2. Copy firebase_config.json to $APP_DIR"
echo "3. Run: sudo systemctl start cbc-ai"
echo "4. Check status: sudo systemctl status cbc-ai"
echo "5. View logs: sudo journalctl -u cbc-ai -f"

