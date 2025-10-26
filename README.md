# Global Logistics Performance Dashboard

A comprehensive real-time analytics dashboard for supply chain logistics management, built with Streamlit and modern web technologies.

## 🎯 Overview

This dashboard provides logistics professionals with powerful tools to monitor, analyze, and optimize supply chain operations through intuitive visualizations and real-time data processing.

## ✨ Key Features

### 📊 Analytics & Monitoring
- **Executive Dashboard**: High-level KPIs and performance metrics
- **Risk Management**: Real-time risk classification and monitoring
- **Performance Tracking**: Comprehensive logistics performance indicators
- **Trend Analysis**: Historical data analysis and forecasting capabilities

### 🗺️ Geospatial Intelligence
- **GPS Tracking**: Interactive maps with real-time vehicle positioning
- **Route Optimization**: Visual route analysis and efficiency metrics
- **Geographic Analytics**: Regional performance insights
- **3D Visualizations**: Advanced PyDeck-powered mapping

### 🔧 Data Management
- **Multi-format Support**: CSV and Excel file uploads
- **Data Validation**: Automatic column mapping and quality checks
- **Persistent Storage**: Uploaded datasets saved permanently
- **Export Capabilities**: Download filtered and processed data

### 🎛️ Interactive Controls
- **Dynamic Filtering**: Real-time data filtering across multiple dimensions
- **Customizable Views**: Personalized dashboard configurations
- **Auto-refresh**: Live updates for operational monitoring
- **Responsive Design**: Optimized for desktop and mobile devices

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone https://github.com/your-username/logistics-dashboard.git
cd logistics-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Access
Open your browser and navigate to `http://localhost:8501`

## 📋 Dashboard Sections

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

## 🎚️ Control Panel

### Filtering Options
- **Risk Classification**: Low, Medium, High, Critical Risk levels
- **Time Ranges**: Flexible date range selection
- **Delivery Metrics**: Performance threshold settings
- **Geographic Filters**: Region and route-based filtering
- **Cargo Conditions**: Quality and condition parameters

### Dataset Management
- **Upload Interface**: Drag-and-drop file upload
- **Validation Engine**: Automatic data quality checks
- **Storage System**: Permanent dataset retention
- **Version Control**: Track dataset changes and updates

## 📊 Data Requirements

### Essential Columns
| Column | Type | Description | Example |
|--------|------|-------------|---------|
| `timestamp` | DateTime | Event timestamp | 2024-01-15 14:30:00 |
| `risk_classification` | String | Risk level | Low Risk, High Risk |
| `shipping_costs` | Float | Shipping expenses | 1250.50 |
| `delay_probability` | Float | Delay likelihood (0-1) | 0.15 |
| `vehicle_gps_latitude` | Float | GPS coordinates | 40.7128 |
| `vehicle_gps_longitude` | Float | GPS coordinates | -74.0060 |

### Optional Enhancements
- **Operational Metrics**: delivery_time_deviation, route_efficiency
- **Quality Indicators**: cargo_condition_status, customer_satisfaction
- **Logistics Data**: product_category, transportation_mode
- **Performance Data**: driver_performance, vehicle_maintenance
- **Business Metrics**: order_value, supplier_reliability

### Sample Data Structure
```csv
timestamp,risk_classification,shipping_costs,delay_probability,vehicle_gps_latitude,vehicle_gps_longitude,customer_satisfaction
2024-01-15 09:00:00,Low Risk,1250.50,0.15,40.7128,-74.0060,4.2
2024-01-15 11:30:00,Medium Risk,1875.25,0.35,34.0522,-118.2437,3.8
2024-01-15 14:45:00,High Risk,2100.75,0.75,41.8781,-87.6298,3.1
```

## 🏗️ Technical Architecture

### Core Technologies
- **Frontend**: Streamlit (Python web framework)
- **Visualization**: Plotly, PyDeck for interactive charts and 3D maps
- **Data Processing**: Pandas, NumPy for efficient data manipulation
- **Geospatial**: PyDeck for advanced mapping capabilities
- **Storage**: Local file system with JSON metadata management

### Performance Optimizations
- **Caching Strategy**: Streamlit's @st.cache_data for improved load times
- **Lazy Loading**: Efficient data loading and processing
- **Memory Management**: Optimized data structures and processing
- **Responsive UI**: Fast rendering and smooth interactions

### System Requirements
- **Python**: 3.8 or higher
- **Memory**: 4GB RAM minimum (8GB recommended)
- **Storage**: 1GB available space for datasets
- **Browser**: Modern browser with JavaScript enabled

## 🛠️ Configuration

### Environment Setup
Create `.streamlit/config.toml` for custom settings:
```toml
[server]
headless = true
port = 8501
maxUploadSize = 200

[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
```

### Data Storage
- **Default Dataset**: `dynamic_supply_chain_logistics_dataset.csv`
- **Uploaded Files**: `uploaded_datasets/` directory
- **Metadata**: `uploaded_datasets/dataset_registry.json`

## 🔧 Deployment Options

### 1. Streamlit Cloud (Recommended)
```bash
# Push to GitHub
git add .
git commit -m "Deploy dashboard"
git push origin main

# Deploy at share.streamlit.io
```

### 2. Docker Deployment
```bash
# Build container
docker build -t logistics-dashboard .

# Run container
docker run -p 8501:8501 logistics-dashboard
```

### 3. Local Network
```bash
# Run on network
streamlit run app.py --server.address 0.0.0.0
```

## 💡 Usage Best Practices

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

### Performance Tips
1. **Filter Early**: Use sidebar controls to reduce data processing
2. **Refresh Strategically**: Use auto-refresh only when needed
3. **Optimize Uploads**: Clean data before uploading for better performance
4. **Monitor Memory**: Keep dataset sizes manageable for smooth operation

## 🤝 Contributing

We welcome contributions to improve the dashboard:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/enhancement`)
3. **Commit** your changes (`git commit -m 'Add new feature'`)
4. **Push** to the branch (`git push origin feature/enhancement`)
5. **Open** a Pull Request

### Development Guidelines
- Follow PEP 8 Python style guidelines
- Add comments for complex functions
- Test new features thoroughly
- Update documentation for new capabilities

## 📞 Support & Documentation

### Getting Help
- **Issues**: Report bugs via GitHub Issues
- **Questions**: Use GitHub Discussions for community support
- **Features**: Request enhancements through GitHub Issues

### Resources
- **Documentation**: Complete guides in `/docs` directory
- **Examples**: Sample datasets in `/examples` folder
- **Tutorials**: Step-by-step guides for common tasks

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built with powerful open-source technologies:
- Streamlit team for the exceptional framework
- Plotly community for visualization capabilities
- PyDeck developers for geospatial mapping
- Contributors and logistics professionals for feedback and improvements

---

**Empowering logistics professionals with data-driven insights for smarter supply chain decisions.**#   G l o b a l - L o g i s t i c s - P e r f o r m a n c e - D a s h b o a r d  
 