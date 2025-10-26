# 🚀 Deployment Guide for Global Logistics Performance Dashboard

## Quick Deployment Options

### 1. 🌟 Streamlit Community Cloud (Recommended - FREE)

**Steps:**

1. **Push to GitHub:**

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/logistics-dashboard.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file: `app.py`
   - Click "Deploy!"

**Pros:** ✅ Free, Easy, Automatic updates from GitHub
**Cons:** ❌ Public repositories only (for free tier)

---

### 2. 🐳 Docker Deployment

**Create Dockerfile:**

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
```

**Deploy:**

```bash
# Build image
docker build -t logistics-dashboard .

# Run container
docker run -p 8501:8501 logistics-dashboard
```

---

### 3. ☁️ Heroku Deployment

**Setup files needed:**

```bash
# Create Procfile
echo "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile

# Create setup.sh
echo "mkdir -p ~/.streamlit/" > setup.sh
echo "echo \"[server]\" > ~/.streamlit/config.toml" >> setup.sh
echo "echo \"port = $PORT\" >> ~/.streamlit/config.toml" >> setup.sh
echo "echo \"address = '0.0.0.0'\" >> ~/.streamlit/config.toml" >> setup.sh
```

**Deploy to Heroku:**

```bash
# Install Heroku CLI, then:
heroku create your-logistics-dashboard
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

---

### 4. 🔥 Railway (Modern Alternative)

1. **Install Railway CLI:**

   ```bash
   npm install -g @railway/cli
   ```

2. **Deploy:**

   ```bash
   railway login
   railway init
   railway up
   ```

---

### 5. 💻 Local Network Deployment

**For internal company use:**

```bash
# Run on network (accessible to other computers)
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

**Access from other devices:** `http://YOUR_IP_ADDRESS:8501`

---

## 📋 Pre-Deployment Checklist

### ✅ Required Files

- [x] `app.py` - Main application
- [x] `requirements.txt` - Dependencies
- [x] `dynamic_supply_chain_logistics_dataset.csv` - Default dataset
- [x] `README.md` - Documentation

### ⚙️ Configuration Files (Create if needed)

**.streamlit/config.toml:**

```toml
[server]
maxUploadSize = 200

[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
```

**runtime.txt (for Heroku):**

```
python-3.9.20
```

---

## 🔒 Security Considerations

### For Production

1. **Environment Variables:**

   ```python
   import os
   
   # Add to app.py
   SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
   ```

2. **Authentication (Optional):**

   ```python
   import streamlit_authenticator as stauth
   # Add login system if needed
   ```

3. **HTTPS:** Enable SSL/TLS in production

---

## 📊 Performance Optimization

### Large Dataset Handling

```python
# Add to app.py
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_large_dataset():
    return pd.read_csv("large_dataset.csv")
```

### Memory Management

```python
# Limit file upload size
st.set_page_config(
    page_title="Logistics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

---

## 🌐 Custom Domain (Optional)

### With Streamlit Cloud

1. Go to app settings
2. Add custom domain
3. Configure DNS CNAME record

### With Other Providers

- Configure reverse proxy (Nginx)
- Set up SSL certificate
- Point domain to your server

---

## 📈 Monitoring & Analytics

### Add Usage Tracking

```python
import streamlit.analytics as sta

# Track page views
sta.track_event("page_view", {"page": "dashboard"})
```

### Error Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

---

## 🚀 Quick Start Commands

### Option 1: Streamlit Cloud (Easiest)

```bash
# 1. Create GitHub repository
# 2. Push code to GitHub  
# 3. Deploy at share.streamlit.io
```

### Option 2: Docker (Containerized)

```bash
docker build -t logistics-dashboard .
docker run -p 8501:8501 logistics-dashboard
```

### Option 3: Local Server

```bash
streamlit run app.py --server.address 0.0.0.0
```

---

## 💡 Next Steps After Deployment

1. **Test all features** on deployed version
2. **Set up monitoring** and alerts
3. **Configure backups** for uploaded datasets
4. **Add user authentication** if needed
5. **Enable HTTPS** for security
6. **Monitor performance** and optimize

---

## 🆘 Troubleshooting

### Common Issues

- **Memory errors:** Reduce dataset size or add pagination
- **Upload failures:** Check file size limits
- **Slow loading:** Implement caching and optimize queries
- **Connection issues:** Verify firewall and network settings

### Debug Mode

```bash
streamlit run app.py --logger.level=debug
```

---

**Choose the deployment method that best fits your needs!**

- **Free & Easy:** Streamlit Community Cloud
- **Professional:** Docker + Cloud provider
- **Enterprise:** Custom server with authentication
