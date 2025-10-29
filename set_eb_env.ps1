# PowerShell Script to Set Elastic Beanstalk Environment Variables
# Run this after creating your EB environment

Write-Host "🚀 Setting Elastic Beanstalk Environment Variables..." -ForegroundColor Green

# Load variables from .env file (if exists)
$envFile = ".env"
if (Test-Path $envFile) {
    Write-Host "📝 Loading variables from .env file..." -ForegroundColor Yellow
    Get-Content $envFile | ForEach-Object {
        if ($_ -match '^\s*([^#][^=]+)\s*=\s*(.+)$') {
            $key = $matches[1].Trim()
            $value = $matches[2].Trim()
            Write-Host "Setting $key..." -ForegroundColor Cyan
            & eb setenv "$key=$value"
        }
    }
} else {
    Write-Host "⚠️  .env file not found. Setting variables manually..." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Please set these variables manually using:" -ForegroundColor Yellow
    Write-Host "  eb setenv KEY=value" -ForegroundColor White
    Write-Host ""
    Write-Host "Required variables:" -ForegroundColor Yellow
    Write-Host "  - FIREBASE_API_KEY" -ForegroundColor White
    Write-Host "  - FIREBASE_AUTH_DOMAIN" -ForegroundColor White
    Write-Host "  - FIREBASE_PROJECT_ID" -ForegroundColor White
    Write-Host "  - FIREBASE_APP_ID" -ForegroundColor White
    Write-Host "  - OPENAI_API_KEY" -ForegroundColor White
    Write-Host "  - GROQ_API_KEY" -ForegroundColor White
    Write-Host "  - SECRET_KEY" -ForegroundColor White
    Write-Host "  - ADMIN_EMAIL" -ForegroundColor White
    Write-Host "  - ADMIN_PASSWORD" -ForegroundColor White
    Write-Host "  - MPESA_CONSUMER_KEY" -ForegroundColor White
    Write-Host "  - MPESA_CONSUMER_SECRET" -ForegroundColor White
    Write-Host "  - MPESA_BUSINESS_SHORTCODE" -ForegroundColor White
    Write-Host "  - MPESA_PASSKEY" -ForegroundColor White
    Write-Host "  - MPESA_CALLBACK_URL" -ForegroundColor White
    Write-Host "  - MPESA_ENVIRONMENT" -ForegroundColor White
    Write-Host "  - FLASK_ENV" -ForegroundColor White
}

Write-Host ""
Write-Host "✅ Done! Verify with: eb printenv" -ForegroundColor Green

