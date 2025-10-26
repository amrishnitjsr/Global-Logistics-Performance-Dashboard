#!/bin/bash

# 🚀 Quick Deployment Script for Logistics Dashboard

echo "🚚 Global Logistics Performance Dashboard - Deployment Assistant"
echo "================================================================="

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found. Creating it..."
    pip freeze > requirements.txt
fi

echo "📋 Available Deployment Options:"
echo "1. 🌟 Streamlit Community Cloud (Free, GitHub required)"
echo "2. 🐳 Docker Local"
echo "3. 💻 Local Network Server"
echo "4. 🔥 Railway"
echo ""

read -p "Choose deployment option (1-4): " choice

case $choice in
    1)
        echo "🌟 Setting up for Streamlit Community Cloud..."
        echo ""
        echo "📝 Next steps:"
        echo "1. Push this code to GitHub:"
        echo "   git init"
        echo "   git add ."
        echo "   git commit -m 'Initial commit'"
        echo "   git branch -M main" 
        echo "   git remote add origin YOUR_GITHUB_REPO_URL"
        echo "   git push -u origin main"
        echo ""
        echo "2. Go to https://share.streamlit.io"
        echo "3. Sign in with GitHub"
        echo "4. Click 'New app' and select your repository"
        echo "5. Set main file: app.py"
        echo "6. Click 'Deploy!'"
        ;;
    2)
        echo "🐳 Building Docker container..."
        docker build -t logistics-dashboard .
        echo "🚀 Starting Docker container..."
        docker run -p 8501:8501 logistics-dashboard
        echo "✅ Dashboard available at: http://localhost:8501"
        ;;
    3)
        echo "💻 Starting local network server..."
        streamlit run app.py --server.address 0.0.0.0 --server.port 8501
        ;;
    4)
        echo "🔥 Railway deployment..."
        echo "1. Install Railway CLI: npm install -g @railway/cli"
        echo "2. Run: railway login"
        echo "3. Run: railway init"
        echo "4. Run: railway up"
        ;;
    *)
        echo "❌ Invalid option. Please run the script again."
        ;;
esac