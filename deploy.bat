@echo off
REM 🚀 Windows Deployment Script for Logistics Dashboard

echo 🚚 Global Logistics Performance Dashboard - Deployment Assistant
echo =================================================================

REM Check if requirements.txt exists
if not exist "requirements.txt" (
    echo ❌ requirements.txt not found. Creating it...
    pip freeze > requirements.txt
)

echo 📋 Available Deployment Options:
echo 1. 🌟 Streamlit Community Cloud (Free, GitHub required^)
echo 2. 🐳 Docker Local
echo 3. 💻 Local Network Server
echo 4. 🔥 Railway
echo.

set /p choice="Choose deployment option (1-4): "

if "%choice%"=="1" (
    echo 🌟 Setting up for Streamlit Community Cloud...
    echo.
    echo 📝 Next steps:
    echo 1. Push this code to GitHub:
    echo    git init
    echo    git add .
    echo    git commit -m "Initial commit"
    echo    git branch -M main
    echo    git remote add origin YOUR_GITHUB_REPO_URL
    echo    git push -u origin main
    echo.
    echo 2. Go to https://share.streamlit.io
    echo 3. Sign in with GitHub
    echo 4. Click 'New app' and select your repository
    echo 5. Set main file: app.py
    echo 6. Click 'Deploy!'
) else if "%choice%"=="2" (
    echo 🐳 Building Docker container...
    docker build -t logistics-dashboard .
    echo 🚀 Starting Docker container...
    docker run -p 8501:8501 logistics-dashboard
    echo ✅ Dashboard available at: http://localhost:8501
) else if "%choice%"=="3" (
    echo 💻 Starting local network server...
    streamlit run app.py --server.address 0.0.0.0 --server.port 8501
) else if "%choice%"=="4" (
    echo 🔥 Railway deployment...
    echo 1. Install Railway CLI: npm install -g @railway/cli
    echo 2. Run: railway login
    echo 3. Run: railway init
    echo 4. Run: railway up
) else (
    echo ❌ Invalid option. Please run the script again.
)

pause