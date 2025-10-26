# Global Logistics Performance Dashboard# Global Logistics Performance Dashboard



[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)A comprehensive real-time analytics dashboard for supply chain logistics management, built with Streamlit and modern web technologies.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)## 🎯 Overview



A comprehensive real-time analytics dashboard for supply chain logistics management, built with Streamlit and modern web technologies.This dashboard provides logistics professionals with powerful tools to monitor, analyze, and optimize supply chain operations through intuitive visualizations and real-time data processing.



## 🎯 Overview## ✨ Key Features



This dashboard provides logistics professionals with powerful tools to monitor, analyze, and optimize supply chain operations through intuitive visualizations and real-time data processing.### 📊 Analytics & Monitoring

- **Executive Dashboard**: High-level KPIs and performance metrics

## ✨ Key Features- **Risk Management**: Real-time risk classification and monitoring

- **Performance Tracking**: Comprehensive logistics performance indicators

### 📊 Analytics & Monitoring- **Trend Analysis**: Historical data analysis and forecasting capabilities

- **Executive Dashboard**: High-level KPIs and performance metrics

- **Risk Management**: Real-time risk classification and monitoring### 🗺️ Geospatial Intelligence

- **Performance Tracking**: Comprehensive logistics performance indicators- **GPS Tracking**: Interactive maps with real-time vehicle positioning

- **Trend Analysis**: Historical data analysis and forecasting capabilities- **Route Optimization**: Visual route analysis and efficiency metrics

- **Geographic Analytics**: Regional performance insights

### 🗺️ Geospatial Intelligence- **3D Visualizations**: Advanced PyDeck-powered mapping

- **GPS Tracking**: Interactive maps with real-time vehicle positioning

- **Route Optimization**: Visual route analysis and efficiency metrics### 🔧 Data Management

- **Geographic Analytics**: Regional performance insights- **Multi-format Support**: CSV and Excel file uploads

- **3D Visualizations**: Advanced PyDeck-powered mapping- **Data Validation**: Automatic column mapping and quality checks

- **Persistent Storage**: Uploaded datasets saved permanently

### 🔧 Data Management- **Export Capabilities**: Download filtered and processed data

- **Multi-format Support**: CSV and Excel file uploads

- **Data Validation**: Automatic column mapping and quality checks### 🎛️ Interactive Controls

- **Persistent Storage**: Uploaded datasets saved permanently- **Dynamic Filtering**: Real-time data filtering across multiple dimensions

- **Export Capabilities**: Download filtered and processed data- **Customizable Views**: Personalized dashboard configurations

- **Auto-refresh**: Live updates for operational monitoring

### 🎛️ Interactive Controls- **Responsive Design**: Optimized for desktop and mobile devices

- **Dynamic Filtering**: Real-time data filtering across multiple dimensions

- **Customizable Views**: Personalized dashboard configurations## 🚀 Quick Start

- **Auto-refresh**: Live updates for operational monitoring

- **Responsive Design**: Optimized for desktop and mobile devices### Installation

```bash

## 🚀 Quick Start# Clone the repository

git clone https://github.com/your-username/logistics-dashboard.git

### Prerequisitescd logistics-dashboard

- Python 3.8 or higher

- pip package manager# Install dependencies

pip install -r requirements.txt

### Installation

```bash# Run the application

# Clone the repositorystreamlit run app.py

git clone https://github.com/amrishnitjsr/Global-Logistics-Performance-Dashboard.git```

cd Global-Logistics-Performance-Dashboard

### Access

# Install dependenciesOpen your browser and navigate to `http://localhost:8501`

pip install -r requirements.txt

## 📋 Dashboard Sections

# Run the application

streamlit run app.py### 1. Executive Dashboard

```**Purpose**: High-level operational overview for management

**Features**:

### Access- Total shipments and volume metrics

Open your browser and navigate to `http://localhost:8501`- Average shipping costs and variance tracking

- Delivery performance indicators

## 📋 Dashboard Sections- Customer satisfaction scores

- Real-time status indicators

### 1. Executive Dashboard

**Purpose**: High-level operational overview for management### 2. Analytics Deep Dive

**Purpose**: Detailed analysis for operational teams

**Features**:**Features**:

- Total shipments and volume metrics- Correlation analysis between key metrics

- Average shipping costs and variance tracking- Distribution analysis and statistical insights

- Delivery performance indicators- Performance trend visualization

- Customer satisfaction scores- Comparative analytics across time periods

- Real-time status indicators- Risk factor analysis



### 2. Analytics Deep Dive### 3. Data Management

**Purpose**: Detailed analysis for operational teams**Purpose**: Dataset administration and quality control

**Features**:

**Features**:- Upload new datasets (CSV/Excel)

- Correlation analysis between key metrics- Data validation and quality assessment

- Distribution analysis and statistical insights- Column mapping assistance

- Performance trend visualization- Dataset preview and statistics

- Comparative analytics across time periods- Export and download capabilities

- Risk factor analysis

### 4. Global Map View

### 3. Data Management**Purpose**: Geospatial analysis and tracking

**Purpose**: Dataset administration and quality control**Features**:

- Interactive 3D GPS tracking

**Features**:- Risk-based color coding

- Upload new datasets (CSV/Excel)- Route visualization and analysis

- Data validation and quality assessment- Geographic performance metrics

- Column mapping assistance- Regional operational insights

- Dataset preview and statistics

- Export and download capabilities## 🎚️ Control Panel



### 4. Global Map View### Filtering Options

**Purpose**: Geospatial analysis and tracking- **Risk Classification**: Low, Medium, High, Critical Risk levels

- **Time Ranges**: Flexible date range selection

**Features**:- **Delivery Metrics**: Performance threshold settings

- Interactive 3D GPS tracking- **Geographic Filters**: Region and route-based filtering

- Risk-based color coding- **Cargo Conditions**: Quality and condition parameters

- Route visualization and analysis

- Geographic performance metrics### Dataset Management

- Regional operational insights- **Upload Interface**: Drag-and-drop file upload

- **Validation Engine**: Automatic data quality checks

## 📊 Data Requirements- **Storage System**: Permanent dataset retention

- **Version Control**: Track dataset changes and updates

### Essential Columns

| Column | Type | Description | Example |## 📊 Data Requirements

|--------|------|-------------|---------|

| `timestamp` | DateTime | Event timestamp | 2024-01-15 14:30:00 |### Essential Columns

| `risk_classification` | String | Risk level | Low Risk, High Risk || Column | Type | Description | Example |

| `shipping_costs` | Float | Shipping expenses | 1250.50 ||--------|------|-------------|---------|

| `delay_probability` | Float | Delay likelihood (0-1) | 0.15 || `timestamp` | DateTime | Event timestamp | 2024-01-15 14:30:00 |

| `vehicle_gps_latitude` | Float | GPS coordinates | 40.7128 || `risk_classification` | String | Risk level | Low Risk, High Risk |

| `vehicle_gps_longitude` | Float | GPS coordinates | -74.0060 || `shipping_costs` | Float | Shipping expenses | 1250.50 |

| `delay_probability` | Float | Delay likelihood (0-1) | 0.15 |

### Sample Data Structure| `vehicle_gps_latitude` | Float | GPS coordinates | 40.7128 |

```csv| `vehicle_gps_longitude` | Float | GPS coordinates | -74.0060 |

timestamp,risk_classification,shipping_costs,delay_probability,vehicle_gps_latitude,vehicle_gps_longitude,customer_satisfaction

2024-01-15 09:00:00,Low Risk,1250.50,0.15,40.7128,-74.0060,4.2### Optional Enhancements

2024-01-15 11:30:00,Medium Risk,1875.25,0.35,34.0522,-118.2437,3.8- **Operational Metrics**: delivery_time_deviation, route_efficiency

2024-01-15 14:45:00,High Risk,2100.75,0.75,41.8781,-87.6298,3.1- **Quality Indicators**: cargo_condition_status, customer_satisfaction

```- **Logistics Data**: product_category, transportation_mode

- **Performance Data**: driver_performance, vehicle_maintenance

## 🏗️ Technical Architecture- **Business Metrics**: order_value, supplier_reliability



### Core Technologies### Sample Data Structure

- **Frontend**: Streamlit (Python web framework)```csv

- **Visualization**: Plotly, PyDeck for interactive charts and 3D mapstimestamp,risk_classification,shipping_costs,delay_probability,vehicle_gps_latitude,vehicle_gps_longitude,customer_satisfaction

- **Data Processing**: Pandas, NumPy for efficient data manipulation2024-01-15 09:00:00,Low Risk,1250.50,0.15,40.7128,-74.0060,4.2

- **Geospatial**: PyDeck for advanced mapping capabilities2024-01-15 11:30:00,Medium Risk,1875.25,0.35,34.0522,-118.2437,3.8

- **Storage**: Local file system with JSON metadata management2024-01-15 14:45:00,High Risk,2100.75,0.75,41.8781,-87.6298,3.1

```

### System Requirements

- **Python**: 3.8 or higher## 🏗️ Technical Architecture

- **Memory**: 4GB RAM minimum (8GB recommended)

- **Storage**: 1GB available space for datasets### Core Technologies

- **Browser**: Modern browser with JavaScript enabled- **Frontend**: Streamlit (Python web framework)

- **Visualization**: Plotly, PyDeck for interactive charts and 3D maps

## 🛠️ Configuration- **Data Processing**: Pandas, NumPy for efficient data manipulation

- **Geospatial**: PyDeck for advanced mapping capabilities

### Environment Setup- **Storage**: Local file system with JSON metadata management

Create `.streamlit/config.toml` for custom settings:

```toml### Performance Optimizations

[server]- **Caching Strategy**: Streamlit's @st.cache_data for improved load times

headless = true- **Lazy Loading**: Efficient data loading and processing

port = 8501- **Memory Management**: Optimized data structures and processing

maxUploadSize = 200- **Responsive UI**: Fast rendering and smooth interactions



[theme]### System Requirements

primaryColor = "#FF6B6B"- **Python**: 3.8 or higher

backgroundColor = "#FFFFFF"- **Memory**: 4GB RAM minimum (8GB recommended)

secondaryBackgroundColor = "#F0F2F6"- **Storage**: 1GB available space for datasets

textColor = "#262730"- **Browser**: Modern browser with JavaScript enabled

```

## 🛠️ Configuration

## 🔧 Deployment Options

### Environment Setup

### 1. Streamlit Cloud (Recommended)Create `.streamlit/config.toml` for custom settings:

1. Push your code to GitHub```toml

2. Go to [share.streamlit.io](https://share.streamlit.io)[server]

3. Connect your GitHub repositoryheadless = true

4. Deploy with one clickport = 8501

maxUploadSize = 200

### 2. Docker Deployment

```bash[theme]

# Build containerprimaryColor = "#FF6B6B"

docker build -t logistics-dashboard .backgroundColor = "#FFFFFF"

secondaryBackgroundColor = "#F0F2F6"

# Run containertextColor = "#262730"

docker run -p 8501:8501 logistics-dashboard```

```

### Data Storage

### 3. Heroku Deployment- **Default Dataset**: `dynamic_supply_chain_logistics_dataset.csv`

The repository includes `Procfile` and deployment scripts for easy Heroku deployment.- **Uploaded Files**: `uploaded_datasets/` directory

- **Metadata**: `uploaded_datasets/dataset_registry.json`

## 💡 Usage Best Practices

## 🔧 Deployment Options

### Data Management

1. **Regular Updates**: Keep datasets current for accurate insights### 1. Streamlit Cloud (Recommended)

2. **Quality Control**: Use validation features before analysis```bash

3. **Backup Strategy**: Export important datasets regularly# Push to GitHub

4. **Performance**: Monitor data size for optimal performancegit add .

git commit -m "Deploy dashboard"

### Analysis Workflowgit push origin main

1. **Start with Executive Dashboard**: Get overview of operations

2. **Use Filters**: Focus on specific time periods or risk levels# Deploy at share.streamlit.io

3. **Deep Dive Analysis**: Explore detailed metrics and correlations```

4. **Geographic Review**: Check GPS tracking and route efficiency

5. **Export Results**: Save findings for further analysis### 2. Docker Deployment

```bash

## 🤝 Contributing# Build container

docker build -t logistics-dashboard .

We welcome contributions to improve the dashboard:

# Run container

1. **Fork** the repositorydocker run -p 8501:8501 logistics-dashboard

2. **Create** a feature branch (`git checkout -b feature/enhancement`)```

3. **Commit** your changes (`git commit -m 'Add new feature'`)

4. **Push** to the branch (`git push origin feature/enhancement`)### 3. Local Network

5. **Open** a Pull Request```bash

# Run on network

### Development Guidelinesstreamlit run app.py --server.address 0.0.0.0

- Follow PEP 8 Python style guidelines```

- Add comments for complex functions

- Test new features thoroughly## 💡 Usage Best Practices

- Update documentation for new capabilities

### Data Management

## 📞 Support & Contact1. **Regular Updates**: Keep datasets current for accurate insights

2. **Quality Control**: Use validation features before analysis

### Getting Help3. **Backup Strategy**: Export important datasets regularly

- **Issues**: Report bugs via [GitHub Issues](https://github.com/amrishnitjsr/Global-Logistics-Performance-Dashboard/issues)4. **Performance**: Monitor data size for optimal performance

- **Questions**: Use GitHub Discussions for community support

- **Features**: Request enhancements through GitHub Issues### Analysis Workflow

1. **Start with Executive Dashboard**: Get overview of operations

### Resources2. **Use Filters**: Focus on specific time periods or risk levels

- **Live Demo**: [View Dashboard](https://your-app-url.streamlit.app) (coming soon)3. **Deep Dive Analysis**: Explore detailed metrics and correlations

- **Documentation**: Complete guides in project wiki4. **Geographic Review**: Check GPS tracking and route efficiency

- **Examples**: Sample datasets included in repository5. **Export Results**: Save findings for further analysis



## 📄 License### Performance Tips

1. **Filter Early**: Use sidebar controls to reduce data processing

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.2. **Refresh Strategically**: Use auto-refresh only when needed

3. **Optimize Uploads**: Clean data before uploading for better performance

## 🙏 Acknowledgments4. **Monitor Memory**: Keep dataset sizes manageable for smooth operation



Built with powerful open-source technologies:## 🤝 Contributing

- [Streamlit](https://streamlit.io/) team for the exceptional framework

- [Plotly](https://plotly.com/) community for visualization capabilitiesWe welcome contributions to improve the dashboard:

- [PyDeck](https://pydeck.gl/) developers for geospatial mapping

- Contributors and logistics professionals for feedback and improvements1. **Fork** the repository

2. **Create** a feature branch (`git checkout -b feature/enhancement`)

---3. **Commit** your changes (`git commit -m 'Add new feature'`)

4. **Push** to the branch (`git push origin feature/enhancement`)

**Empowering logistics professionals with data-driven insights for smarter supply chain decisions.**5. **Open** a Pull Request

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

**Empowering logistics professionals with data-driven insights for smarter supply chain decisions.**#   G l o b a l - L o g i s t i c s - P e r f o r m a n c e - D a s h b o a r d 
 
 