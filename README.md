# Global Logistics Performance Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive real-time analytics dashboard for supply chain logistics management, built with Streamlit and modern web technologies.

##  Overview

This dashboard provides logistics professionals with powerful tools to monitor, analyze, and optimize supply chain operations through intuitive visualizations and real-time data processing.

##  Project Structure

`
Global-Logistics-Performance-Dashboard/
 app.py                           # Main Streamlit application
 requirements.txt                 # Python dependencies
 runtime.txt                      # Python version specification
 Procfile                        # Heroku deployment configuration
 Dockerfile                      # Docker containerization
 deploy.bat                      # Windows deployment script
 deploy.sh                       # Unix/Linux deployment script
 deployment_guide.md             # Detailed deployment instructions
 github_setup_instructions.md    # GitHub setup guide
 dynamic_supply_chain_logistics_dataset.csv  # Sample dataset
 .streamlit/
    config.toml                 # Streamlit configuration
 __pycache__/                    # Python cache files
     app.cpython-313.pyc
`

##  Key Features

###  Analytics & Monitoring
- **Executive Dashboard**: High-level KPIs and performance metrics
- **Risk Management**: Real-time risk classification and monitoring
- **Performance Tracking**: Comprehensive logistics performance indicators
- **Trend Analysis**: Historical data analysis and forecasting capabilities

###  Geospatial Intelligence
- **GPS Tracking**: Interactive maps with real-time vehicle positioning
- **Route Optimization**: Visual route analysis and efficiency metrics
- **Geographic Analytics**: Regional performance insights
- **3D Visualizations**: Advanced PyDeck-powered mapping

###  Data Management
- **Multi-format Support**: CSV and Excel file uploads
- **Data Validation**: Automatic column mapping and quality checks
- **Persistent Storage**: Uploaded datasets saved permanently
- **Export Capabilities**: Download filtered and processed data

###  Interactive Controls
- **Dynamic Filtering**: Real-time data filtering across multiple dimensions
- **Customizable Views**: Personalized dashboard configurations
- **Auto-refresh**: Live updates for operational monitoring
- **Responsive Design**: Optimized for desktop and mobile devices

##  Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation
`ash
# Clone the repository
git clone https://github.com/amrishnitjsr/Global-Logistics-Performance-Dashboard.git
cd Global-Logistics-Performance-Dashboard

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
`

### Access
Open your browser and navigate to http://localhost:8501

##  Dashboard Sections

### 1. Executive Dashboard
**Purpose**: High-level operational overview for management

**Features**:
- Total shipments and volume metrics
- Average shipping costs and variance tracking
- Delivery performance indicators
- Customer satisfaction scores
- Real-time status indicators

### 2. Analytics Deep Dive
**Purpose**: Detailed analysis for operational teams

**Features**:
- Correlation analysis between key metrics
- Distribution analysis and statistical insights
- Performance trend visualization
- Comparative analytics across time periods
- Risk factor analysis

### 3. Data Management
**Purpose**: Dataset administration and quality control

**Features**:
- Upload new datasets (CSV/Excel)
- Data validation and quality assessment
- Column mapping assistance
- Dataset preview and statistics
- Export and download capabilities

### 4. Global Map View
**Purpose**: Geospatial analysis and tracking

**Features**:
- Interactive 3D GPS tracking
- Risk-based color coding
- Route visualization and analysis
- Geographic performance metrics
- Regional operational insights

##  Data Requirements

### Essential Columns
| Column | Type | Description | Example |
|--------|------|-------------|---------|
| timestamp | DateTime | Event timestamp | 2024-01-15 14:30:00 |
| risk_classification | String | Risk level | Low Risk, High Risk |
| shipping_costs | Float | Shipping expenses | 1250.50 |
| delay_probability | Float | Delay likelihood (0-1) | 0.15 |
| vehicle_gps_latitude | Float | GPS coordinates | 40.7128 |
| vehicle_gps_longitude | Float | GPS coordinates | -74.0060 |

### Sample Data Structure
`csv
timestamp,risk_classification,shipping_costs,delay_probability,vehicle_gps_latitude,vehicle_gps_longitude,customer_satisfaction
2024-01-15 09:00:00,Low Risk,1250.50,0.15,40.7128,-74.0060,4.2
2024-01-15 11:30:00,Medium Risk,1875.25,0.35,34.0522,-118.2437,3.8
2024-01-15 14:45:00,High Risk,2100.75,0.75,41.8781,-87.6298,3.1
`

##  Technical Architecture

### Core Technologies
- **Frontend**: Streamlit (Python web framework)
- **Visualization**: Plotly, PyDeck for interactive charts and 3D maps
- **Data Processing**: Pandas, NumPy for efficient data manipulation
- **Geospatial**: PyDeck for advanced mapping capabilities
- **Storage**: Local file system with JSON metadata management

### System Requirements
- **Python**: 3.8 or higher
- **Memory**: 4GB RAM minimum (8GB recommended)
- **Storage**: 1GB available space for datasets
- **Browser**: Modern browser with JavaScript enabled

##  Configuration

### Environment Setup
Create .streamlit/config.toml for custom settings:
`	oml
[server]
headless = true
port = 8501
maxUploadSize = 200

[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
`

##  Deployment Options

### 1. Streamlit Cloud (Recommended)
1. Push your code to GitHub
2. Go to share.streamlit.io
3. Connect your GitHub repository
4. Deploy with one click

### 2. Docker Deployment
`ash
# Build container
docker build -t logistics-dashboard .

# Run container
docker run -p 8501:8501 logistics-dashboard
`

### 3. Heroku Deployment
The repository includes Procfile and deployment scripts for easy Heroku deployment.

##  Usage Best Practices

### Data Management
1. **Regular Updates**: Keep datasets current for accurate insights
2. **Quality Control**: Use validation features before analysis
3. **Backup Strategy**: Export important datasets regularly
4. **Performance**: Monitor data size for optimal performance

### Analysis Workflow
1. **Start with Executive Dashboard**: Get overview of operations
2. **Use Filters**: Focus on specific time periods or risk levels
3. **Deep Dive Analysis**: Explore detailed metrics and correlations
4. **Geographic Review**: Check GPS tracking and route efficiency
5. **Export Results**: Save findings for further analysis

##  Contributing

We welcome contributions to improve the dashboard:

1. **Fork** the repository
2. **Create** a feature branch (git checkout -b feature/enhancement)
3. **Commit** your changes (git commit -m 'Add new feature')
4. **Push** to the branch (git push origin feature/enhancement)
5. **Open** a Pull Request

### Development Guidelines
- Follow PEP 8 Python style guidelines
- Add comments for complex functions
- Test new features thoroughly
- Update documentation for new capabilities

##  Support & Contact

### Getting Help
- **Issues**: Report bugs via GitHub Issues
- **Questions**: Use GitHub Discussions for community support
- **Features**: Request enhancements through GitHub Issues

### Resources
- **Live Demo**: View Dashboard (coming soon)
- **Documentation**: Complete guides in project wiki
- **Examples**: Sample datasets included in repository

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Acknowledgments

Built with powerful open-source technologies:
- Streamlit team for the exceptional framework
- Plotly community for visualization capabilities
- PyDeck developers for geospatial mapping
- Contributors and logistics professionals for feedback and improvements

---

**Empowering logistics professionals with data-driven insights for smarter supply chain decisions.**
