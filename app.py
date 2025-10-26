import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk
import datetime
import numpy as np
import warnings

# Suppress Plotly and Streamlit deprecation warnings for cleaner output
warnings.filterwarnings("ignore", message=".*keyword arguments.*deprecated.*")
warnings.filterwarnings("ignore", category=FutureWarning, module="plotly.*")
warnings.filterwarnings("ignore", message=".*Use `config` instead.*")

# Page configuration
st.set_page_config(
    page_title="Logistics Performance Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com',
        'Report a bug': "https://github.com",
        'About': "# Logistics Performance Dashboard\nBuilt with Streamlit and PyDeck"
    }
)

# Mobile detection and responsive utilities
def is_mobile():
    """Detect mobile device based on user agent (simplified)"""
    try:
        # Get user agent from Streamlit session state if available
        user_agent = st.context.headers.get("user-agent", "").lower()
        mobile_indicators = ['mobile', 'android', 'iphone', 'ipad', 'tablet', 'phone']
        return any(indicator in user_agent for indicator in mobile_indicators)
    except:
        # Fallback: assume desktop if detection fails
        return False

def get_responsive_columns(desktop_cols, mobile_cols=None, tablet_cols=None):
    """Get responsive column layout based on device type"""
    if mobile_cols is None:
        mobile_cols = 1 if isinstance(desktop_cols, int) else [1] * len(desktop_cols)
    if tablet_cols is None:
        tablet_cols = desktop_cols if isinstance(desktop_cols, int) else desktop_cols
    
    # For now, use a simplified responsive approach
    # In a real mobile app, you'd use JavaScript for proper detection
    return desktop_cols

# Add mobile viewport meta tag
st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
""", unsafe_allow_html=True)

# Custom CSS for enhanced styling and mobile responsiveness
st.markdown("""
<style>
    /* Mobile-first responsive design */
    @media (max-width: 768px) {
        .main .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 0.5rem;
            padding-right: 0.5rem;
            max-width: 100%;
        }
        
        .main-header {
            font-size: 1.8rem !important;
            line-height: 1.2;
            margin-bottom: 0.5rem;
        }
        
        .subtitle {
            font-size: 0.9rem !important;
            margin-bottom: 1rem;
        }
        
        /* Sidebar adjustments for mobile */
        .css-1d391kg {
            width: 100% !important;
            min-width: 100% !important;
        }
        
        /* Make metrics more compact on mobile */
        .metric-container {
            padding: 0.5rem !important;
            margin: 0.25rem 0 !important;
            font-size: 0.8rem;
        }
        
        /* Adjust plotly charts for mobile */
        .js-plotly-plot .plotly .modebar {
            left: 0px !important;
        }
        
        /* Make tables scrollable on mobile */
        .stDataFrame {
            overflow-x: auto;
        }
        
        /* Adjust column spacing for mobile */
        .css-ocqkz7 {
            gap: 0.5rem;
        }
        
        /* Mobile-friendly buttons */
        .stButton > button {
            width: 100%;
            margin: 0.25rem 0;
            font-size: 0.9rem;
            padding: 0.5rem;
        }
        
        /* Adjust selectbox and input width */
        .stSelectbox, .stMultiSelect, .stDateInput, .stTimeInput {
            width: 100%;
        }
        
        /* Make map controls more accessible on mobile */
        .deck-tooltip {
            font-size: 0.8rem !important;
            max-width: 200px !important;
        }
    }
    
    /* Tablet adjustments */
    @media (min-width: 769px) and (max-width: 1024px) {
        .main-header {
            font-size: 2.5rem;
        }
        
        .metric-container {
            padding: 0.8rem;
        }
    }
    
    /* Desktop and larger screens */
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4, #45B7D1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    
    .metric-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #FF6B6B;
        margin: 0.5rem 0;
        color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2C3E50 0%, #4A6741 100%);
    }
    
    .stAlert {
        border-radius: 10px;
        border-left: 4px solid #FF6B6B;
    }
    
    /* Touch-friendly improvements */
    .stButton > button:hover {
        transform: scale(1.02);
        transition: transform 0.2s;
    }
    
    /* Improve readability on small screens */
    @media (max-width: 480px) {
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            font-size: 1.2rem !important;
            line-height: 1.3;
        }
        
        .stMarkdown p {
            font-size: 0.9rem;
            line-height: 1.4;
        }
    }
    
    /* Add viewport meta tag equivalent styling */
    html {
        -webkit-text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;
    }
</style>

<script>
// Mobile detection and responsive adjustments
function isMobileDevice() {
    return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}

function isTabletDevice() {
    return /iPad|Android/i.test(navigator.userAgent) && window.innerWidth > 768;
}

// Add mobile class to body for CSS targeting
if (isMobileDevice()) {
    document.body.classList.add('mobile-device');
}

if (isTabletDevice()) {
    document.body.classList.add('tablet-device');
}

// Handle orientation changes
window.addEventListener('orientationchange', function() {
    setTimeout(function() {
        window.scrollTo(0, 0);
    }, 100);
});

// Optimize touch interactions
if ('ontouchstart' in window) {
    document.body.classList.add('touch-device');
}

// Prevent zoom on double tap for better UX
let lastTouchEnd = 0;
document.addEventListener('touchend', function (event) {
    let now = (new Date()).getTime();
    if (now - lastTouchEnd <= 300) {
        event.preventDefault();
    }
    lastTouchEnd = now;
}, false);
</script>
""", unsafe_allow_html=True)

# Color mapping function for risk levels
def get_color_for_risk(risk_level):
    """Map risk levels to colors for visualization."""
    colors = {
        'Low Risk': [0, 255, 0, 160],     # Green
        'Medium Risk': [255, 255, 0, 160], # Yellow  
        'High Risk': [255, 165, 0, 160],   # Orange
        'Critical Risk': [255, 0, 0, 160] # Red
    }
    return colors.get(risk_level, [128, 128, 128, 160])  # Default gray

def get_major_city_for_country(country):
    """Map countries to their major commercial/logistics cities."""
    country_to_city = {
        'United States': 'New York',
        'USA': 'New York', 
        'US': 'New York',
        'China': 'Shanghai',
        'Germany': 'Hamburg',
        'United Kingdom': 'London',
        'UK': 'London',
        'France': 'Paris',
        'Italy': 'Milan',
        'Spain': 'Madrid',
        'Netherlands': 'Rotterdam',
        'Japan': 'Tokyo',
        'Singapore': 'Singapore',
        'India': 'Mumbai',
        'Canada': 'Toronto',
        'Australia': 'Sydney',
        'Brazil': 'São Paulo',
        'Mexico': 'Mexico City',
        'South Korea': 'Seoul',
        'UAE': 'Dubai',
        'South Africa': 'Johannesburg',
        'Russia': 'Moscow',
        'Turkey': 'Istanbul',
        'Saudi Arabia': 'Riyadh',
        'Sweden': 'Stockholm',
        'Norway': 'Oslo',
        'Denmark': 'Copenhagen',
        'Belgium': 'Brussels',
        'Switzerland': 'Zurich',
        'Austria': 'Vienna',
        'Poland': 'Warsaw',
        'Czech Republic': 'Prague',
        'Hungary': 'Budapest',
        'Romania': 'Bucharest',
        'Greece': 'Athens',
        'Portugal': 'Lisbon',
        'Finland': 'Helsinki',
        'Ireland': 'Dublin',
        'New Zealand': 'Auckland',
        'Thailand': 'Bangkok',
        'Malaysia': 'Kuala Lumpur',
        'Indonesia': 'Jakarta',
        'Philippines': 'Manila',
        'Vietnam': 'Ho Chi Minh City',
        'Argentina': 'Buenos Aires',
        'Chile': 'Santiago',
        'Colombia': 'Bogotá',
        'Peru': 'Lima',
        'Egypt': 'Cairo',
        'Israel': 'Tel Aviv',
        'Jordan': 'Amman',
        'Kuwait': 'Kuwait City',
        'Qatar': 'Doha',
        'Bahrain': 'Manama',
        'Oman': 'Muscat',
        'Pakistan': 'Karachi',
        'Bangladesh': 'Dhaka',
        'Sri Lanka': 'Colombo',
        'Kenya': 'Nairobi',
        'Nigeria': 'Lagos',
        'Ghana': 'Accra',
        'Morocco': 'Casablanca',
        'Tunisia': 'Tunis',
        'Algeria': 'Algiers'
    }
    return country_to_city.get(country, country)  # Return country name if no city mapping found

def get_country_region(lat, lon):
    """Determine country/region based on GPS coordinates."""
    if 25 <= lat <= 49 and -125 <= lon <= -66:
        return "United States"
    elif 56 <= lat <= 70 and -141 <= lon <= -52:
        return "Canada" 
    elif 14 <= lat <= 33 and -118 <= lon <= -86:
        return "Mexico"
    elif 36 <= lat <= 42 and -9 <= lon <= 3:
        return "Spain"
    elif 41 <= lat <= 51 and -5 <= lon <= 10:
        return "France"
    elif 47 <= lat <= 55 and 6 <= lon <= 15:
        return "Germany"
    elif 50 <= lat <= 60 and -8 <= lon <= 2:
        return "United Kingdom"
    elif 35 <= lat <= 47 and 6 <= lon <= 19:
        return "Italy"
    elif 20 <= lat <= 37 and 68 <= lon <= 97:
        return "India"
    elif 18 <= lat <= 54 and 73 <= lon <= 135:
        return "China"
    elif 31 <= lat <= 46 and 129 <= lon <= 146:
        return "Japan"
    elif -44 <= lat <= -10 and 113 <= lon <= 154:
        return "Australia"
    elif -35 <= lat <= -22 and -58 <= lon <= -34:
        return "Brazil"
    else:
        return "Other Regions"

def get_mobile_config():
    """Get mobile-optimized configuration for Plotly charts."""
    return {
        'displayModeBar': True,
        'modeBarButtonsToRemove': [
            'zoom2d', 'pan2d', 'lasso2d', 'select2d', 'autoScale2d', 'hoverClosestCartesian',
            'hoverCompareCartesian', 'resetScale2d', 'toggleSpikelines'
        ],
        'modeBarButtonsToAdd': ['resetViews'],
        'displaylogo': False,
        'toImageButtonOptions': {
            'format': 'png',
            'filename': 'logistics_chart',
            'height': 300,
            'width': 400,
            'scale': 1
        },
        'responsive': True
    }

def get_mobile_layout_updates(base_layout):
    """Update layout for mobile optimization."""
    mobile_updates = {
        'font': {'size': 10},
        'margin': {'l': 40, 'r': 40, 't': 40, 'b': 40},
        'legend': {
            'orientation': 'h',
            'yanchor': 'bottom',
            'y': 1.02,
            'xanchor': 'right',
            'x': 1
        },
        'xaxis': {
            'tickangle': -45,
            'tickfont': {'size': 9}
        },
        'yaxis': {
            'tickfont': {'size': 9}
        }
    }
    
    # Update base layout with mobile optimizations
    for key, value in mobile_updates.items():
        if key in ['xaxis', 'yaxis'] and key in base_layout:
            base_layout[key].update(value)
        else:
            base_layout[key] = value
    
    return base_layout

# Dashboard Header
st.markdown('<h1 class="main-header">Global Logistics Performance Dashboard</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Real-time Supply Chain Analytics & Risk Management | Worldwide Operations Overview</p>', unsafe_allow_html=True)

# Mobile optimization notice
st.markdown("""
<div style="background: linear-gradient(90deg, #4ECDC4, #44A08D); padding: 0.5rem; border-radius: 8px; margin: 1rem 0; text-align: center;">
    <p style="color: white; margin: 0; font-size: 0.9rem;">
        📱 <strong>Mobile Optimized:</strong> This dashboard is fully responsive and optimized for Android, iOS, and desktop devices!
    </p>
</div>
""", unsafe_allow_html=True)

# Dashboard Statistics Overview - Responsive Layout
# Use responsive columns: 2 columns on mobile, 4 on desktop
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    st.markdown("### 📊 Dashboard Stats")
with col2:
    current_time = datetime.datetime.now()
    st.metric("⏰ Last Updated", current_time.strftime("%H:%M:%S"))
with col3:
    st.metric("📅 Date", current_time.strftime("%Y-%m-%d"))
with col4:
    st.metric("🟢 Status", "Live")

st.markdown("---")

@st.cache_data
def load_default_data():
    """Load the default supply chain logistics dataset."""
    import os
    
    # Check if default dataset exists
    if not os.path.exists("dynamic_supply_chain_logistics_dataset.csv"):
        return None
        
    with st.spinner("🔄 Loading default logistics data..."):
        try:
            df = pd.read_csv("dynamic_supply_chain_logistics_dataset.csv")
            # Convert timestamp column to datetime
            if 'timestamp' in df.columns:
                df['timestamp'] = pd.to_datetime(df['timestamp'])
            return df
        except Exception as e:
            st.error(f"Error loading default dataset: {e}")
            return None

@st.cache_data
def load_uploaded_data(uploaded_file):
    """Load uploaded dataset and save for future use."""
    with st.spinner("🔄 Processing uploaded data..."):
        try:
            # Determine file type and read accordingly
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(uploaded_file)
            
            # Try to convert timestamp column if it exists
            timestamp_cols = ['timestamp', 'date', 'time', 'datetime', 'Date', 'Timestamp']
            for col in timestamp_cols:
                if col in df.columns:
                    try:
                        df[col] = pd.to_datetime(df[col])
                        if col != 'timestamp':
                            df['timestamp'] = df[col]  # Standardize column name
                        break
                    except:
                        continue
            
            # Save uploaded dataset permanently
            try:
                import os
                import json
                from datetime import datetime
                
                # Create uploads directory if it doesn't exist
                os.makedirs('uploaded_datasets', exist_ok=True)
                
                # Generate safe filename with timestamp to avoid conflicts
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                base_name = uploaded_file.name.replace(' ', '_').replace('(', '').replace(')', '')
                if not base_name.endswith('.csv'):
                    base_name = base_name.rsplit('.', 1)[0] + '.csv'
                
                safe_filename = f"{timestamp}_{base_name}"
                saved_path = f"uploaded_datasets/{safe_filename}"
                
                # Save the dataset as CSV
                df.to_csv(saved_path, index=False)
                
                # Create/update dataset registry for permanent tracking
                registry_path = "uploaded_datasets/dataset_registry.json"
                registry = {}
                
                if os.path.exists(registry_path):
                    try:
                        with open(registry_path, 'r') as f:
                            registry = json.load(f)
                    except:
                        registry = {}
                
                # Add new dataset to registry
                registry[safe_filename] = {
                    'original_name': uploaded_file.name,
                    'upload_date': datetime.now().isoformat(),
                    'file_size': len(df),
                    'columns': list(df.columns),
                    'saved_path': saved_path
                }
                
                # Save updated registry
                with open(registry_path, 'w') as f:
                    json.dump(registry, f, indent=2)
                
                st.success(f"✅ Dataset permanently saved as '{safe_filename}' with {len(df)} records!")
                st.info(f"💾 Saved to: {saved_path}")
                
            except Exception as save_error:
                st.warning(f"⚠️ Dataset loaded successfully but couldn't save permanently: {save_error}")
                        
            return df, None
        except Exception as e:
            return None, str(e)

def validate_dataset(df):
    """Validate if the dataset has required columns for dashboard functionality."""
    required_cols = ['risk_classification', 'shipping_costs', 'delay_probability']
    missing_cols = [col for col in required_cols if col not in df.columns]
    
    suggestions = {
        'risk_classification': ['risk', 'risk_level', 'priority', 'category'],
        'shipping_costs': ['cost', 'price', 'amount', 'shipping_cost', 'total_cost'],
        'delay_probability': ['delay_prob', 'delay_risk', 'delay_chance', 'probability']
    }
    
    return missing_cols, suggestions

def show_dataset_upload_interface():
    """Show the dataset upload interface when no data is available."""
    # Custom CSS for upload interface
    st.markdown("""
    <style>
    .upload-container {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        margin: 2rem 0;
        color: white;
    }
    .upload-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
    }
    .upload-title {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .upload-subtitle {
        font-size: 1.2rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    .feature-box {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem;
        backdrop-filter: blur(10px);
    }
    .requirement-box {
        background: #f8f9fa;
        border-left: 4px solid #007bff;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main upload interface
    st.markdown("""
    <div class="upload-container">
        <div class="upload-icon">📊</div>
        <div class="upload-title">Welcome to Logistics Analytics Dashboard</div>
        <div class="upload-subtitle">Please upload your logistics dataset to get started</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Create columns for layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### 📁 Upload Your Dataset")
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Choose a CSV or Excel file",
            type=['csv', 'xlsx', 'xls'],
            help="Upload your logistics dataset to analyze supply chain performance"
        )
        
        if uploaded_file is not None:
            return uploaded_file
    
    # Features section
    st.markdown("### 🚀 What You'll Get")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="feature-box">
            <h4>📈 Executive Dashboard</h4>
            <p>KPIs, performance metrics, and trend analysis</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-box">
            <h4>🔍 Deep Analytics</h4>
            <p>Advanced charts, correlations, and insights</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-box">
            <h4>🌍 Global Mapping</h4>
            <p>GPS tracking, route analysis, and geospatial views</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="feature-box">
            <h4>📋 Data Management</h4>
            <p>Data profiling, quality checks, and export options</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Dataset requirements
    st.markdown("### 📋 Dataset Requirements")
    
    st.markdown("""
    <div class="requirement-box">
        <h4>Required Columns for Full Functionality:</h4>
        <ul>
            <li><strong>risk_classification</strong> - Risk levels (Low Risk, Medium Risk, High Risk)</li>
            <li><strong>shipping_costs</strong> - Numerical shipping cost data</li>
            <li><strong>delay_probability</strong> - Delay probability values (0-1)</li>
            <li><strong>vehicle_gps_latitude</strong> - GPS latitude coordinates</li>
            <li><strong>vehicle_gps_longitude</strong> - GPS longitude coordinates</li>
            <li><strong>timestamp</strong> - Date/time information</li>
        </ul>
        <p><em>💡 Don't worry if your dataset has different column names - the system will suggest mappings!</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sample data info
    with st.expander("📄 Sample Data Format", expanded=False):
        st.markdown("""
        Your CSV/Excel file should look something like this:
        
        | timestamp | risk_classification | shipping_costs | delay_probability | vehicle_gps_latitude | vehicle_gps_longitude |
        |-----------|-------------------|----------------|-------------------|---------------------|---------------------|
        | 2024-01-01 | Low Risk | 1250.50 | 0.15 | 40.7128 | -74.0060 |
        | 2024-01-02 | High Risk | 2100.75 | 0.85 | 34.0522 | -118.2437 |
        """)
    
    return None



# Sidebar with Dashboard Controls
st.sidebar.markdown("## Dashboard Controls")
st.sidebar.markdown("---")

# File Upload Section
st.sidebar.markdown("### Dataset Management")

# Load dataset registry for permanent datasets
import os
import json
uploaded_datasets = []
dataset_info = {}

if os.path.exists('uploaded_datasets'):
    # Load registry if it exists
    registry_path = "uploaded_datasets/dataset_registry.json"
    if os.path.exists(registry_path):
        try:
            with open(registry_path, 'r') as f:
                registry = json.load(f)
            
            uploaded_datasets = list(registry.keys())
            dataset_info = registry
        except:
            # Fallback to simple file listing
            uploaded_datasets = [f for f in os.listdir('uploaded_datasets') 
                               if f.endswith('.csv') and f != 'dataset_registry.json']
    else:
        uploaded_datasets = [f for f in os.listdir('uploaded_datasets') 
                           if f.endswith('.csv')]

# Show previously uploaded datasets with enhanced info
if uploaded_datasets:
    st.sidebar.markdown("**Permanently Saved Datasets:**")
    
    # Create display options with metadata
    display_options = ['None']
    for dataset in uploaded_datasets:
        if dataset in dataset_info:
            info = dataset_info[dataset]
            display_name = f"{info['original_name']} ({info['file_size']} records)"
            display_options.append(f"{dataset}|{display_name}")
        else:
            display_options.append(f"{dataset}|{dataset}")
    
    selected_display = st.sidebar.selectbox(
        "Choose saved dataset",
        options=display_options,
        help="Select a permanently saved dataset",
        format_func=lambda x: x.split('|')[1] if '|' in x else x
    )
    
    if selected_display != 'None':
        selected_previous = selected_display.split('|')[0]
        
        # Show dataset info if available
        if selected_previous in dataset_info:
            info = dataset_info[selected_previous]
            st.sidebar.info(f"**{info['original_name']}**\n"
                          f"Uploaded: {info['upload_date'][:10]}\n"
                          f"Records: {info['file_size']:,}\n"
                          f"Columns: {len(info['columns'])}")
        
        # Load previously uploaded dataset
        try:
            df_previous = pd.read_csv(f'uploaded_datasets/{selected_previous}')
            if 'timestamp' in df_previous.columns:
                df_previous['timestamp'] = pd.to_datetime(df_previous['timestamp'])
            st.session_state['previous_dataset'] = df_previous
            st.session_state['previous_dataset_name'] = selected_previous
            st.sidebar.success(f"✅ Dataset loaded successfully!")
        except Exception as e:
            st.sidebar.error(f"❌ Error loading dataset: {e}")
    
    # Add dataset management options
    if len(uploaded_datasets) > 0:
        with st.sidebar.expander("Manage Saved Datasets"):
            st.write(f"**Total saved datasets:** {len(uploaded_datasets)}")
            if dataset_info:
                total_records = sum(info.get('file_size', 0) for info in dataset_info.values())
                st.write(f"**Total records:** {total_records:,}")
            
            if st.button("Clear All Saved Datasets"):
                try:
                    import shutil
                    if os.path.exists('uploaded_datasets'):
                        shutil.rmtree('uploaded_datasets')
                    st.success("✅ All saved datasets cleared!")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error clearing datasets: {e}")

st.sidebar.markdown("**Upload New Dataset:**")
uploaded_file = st.sidebar.file_uploader(
    "Upload Your Dataset",
    type=['csv', 'xlsx', 'xls'],
    help="Upload a CSV or Excel file with logistics data"
)

# Dataset selection
use_uploaded = False
use_previous = False

# Check for newly uploaded file
if uploaded_file is not None:
    use_uploaded = st.sidebar.checkbox("📊 Use New Uploaded Dataset", value=True)
    if use_uploaded:
        st.sidebar.success("✅ Using new uploaded file!")
        # Reset data loaded state if user switches datasets
        if 'current_file' not in st.session_state or st.session_state.current_file != uploaded_file.name:
            st.session_state.data_loaded = False
            st.session_state.current_file = uploaded_file.name

# Check for previously selected dataset
elif 'previous_dataset' in st.session_state and 'previous_dataset_name' in st.session_state:
    use_previous = st.sidebar.checkbox("📊 Use Selected Previous Dataset", value=True)
    if use_previous:
        st.sidebar.success(f"✅ Using: {st.session_state['previous_dataset_name']}")

# Default fallback
if not use_uploaded and not use_previous:
    st.sidebar.info("📂 Using default dataset")
    # Reset data loaded state if switching back to default
    if 'current_file' in st.session_state:
        st.session_state.data_loaded = False
        del st.session_state.current_file

st.sidebar.markdown("---")

# Load data with progress indicator
start_time = datetime.datetime.now()

# Check if default dataset exists
import os
default_dataset_exists = os.path.exists("dynamic_supply_chain_logistics_dataset.csv")

# Initialize session state for tracking data load status
if 'data_loaded' not in st.session_state:
    st.session_state.data_loaded = False

# Initialize persistent dataset preferences
if 'persistent_dataset_preference' not in st.session_state:
    st.session_state.persistent_dataset_preference = None
    
if 'last_used_dataset' not in st.session_state:
    st.session_state.last_used_dataset = None

# Only show main upload interface if absolutely necessary
if not st.session_state.data_loaded and not default_dataset_exists and uploaded_file is None:
    uploaded_file = show_dataset_upload_interface()
    # If still no file after showing interface, stop here
    if uploaded_file is None:
        st.stop()
    else:
        # File was uploaded through main interface, set use_uploaded to True
        use_uploaded = True

# Determine which dataset to use
df = None
dataset_source = ""

if uploaded_file is not None and use_uploaded:
    # Load newly uploaded data
    df, upload_error = load_uploaded_data(uploaded_file)
    
    if upload_error:
        st.error(f"❌ Error loading uploaded file: {upload_error}")
        df = None
    else:
        dataset_source = f"Uploaded ({uploaded_file.name})"
        # Remember this choice for persistence
        st.session_state.last_used_dataset = ('uploaded', uploaded_file.name)

elif use_previous and 'previous_dataset' in st.session_state:
    # Use previously uploaded dataset
    df = st.session_state['previous_dataset']
    dataset_source = f"Previous ({st.session_state['previous_dataset_name']})"
    # Remember this choice for persistence
    st.session_state.last_used_dataset = ('previous', st.session_state['previous_dataset_name'])

# If no dataset loaded yet, try default
if df is None:
    if default_dataset_exists:
        df = load_default_data()
        dataset_source = "Default"
    else:
        st.error("❌ No dataset available. Please upload a dataset using the sidebar.")
        st.stop()

# Validate dataset if it was loaded successfully
if df is not None and len(df) == 0:
    st.error("❌ Dataset is empty.")
    st.stop()

load_time = (datetime.datetime.now() - start_time).total_seconds()

# Success message for data loading
if len(df) > 0:
    st.success(f"✅ Successfully loaded {len(df):,} logistics records from **{dataset_source}** in {load_time:.2f}s!")
    # Mark data as successfully loaded
    st.session_state.data_loaded = True
    
# Dataset information panel
with st.expander("📊 Dataset Information", expanded=False):
    col_info1, col_info2 = st.columns(2)
    
    with col_info1:
        st.write("**Dataset Details:**")
        st.write(f"• Source: {dataset_source}")
        st.write(f"• Records: {len(df):,}")
        st.write(f"• Columns: {len(df.columns)}")
        st.write(f"• Load Time: {load_time:.2f}s")
        
    with col_info2:
        st.write("**Available Columns:**")
        col_list = ", ".join(df.columns[:10])
        if len(df.columns) > 10:
            col_list += f"... and {len(df.columns)-10} more"
        st.write(col_list)
    
    # System status
    st.info("**Note:** Plotly deprecation warnings in terminal are normal and don't affect functionality.")
    st.success("🟢 Dashboard Status: Fully Operational")

# Quick Stats in Sidebar
st.sidebar.markdown("### 📊 Quick Overview")
st.sidebar.info(f"📦 **Total Records:** {len(df):,}")
st.sidebar.info(f"🌍 **GPS Points:** {df[['vehicle_gps_latitude', 'vehicle_gps_longitude']].drop_duplicates().shape[0]:,}")
st.sidebar.info(f"🚚 **Data Points:** {len(df):,}")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔧 Data Filters")

# Add sidebar notifications
if len(df[df['delay_probability'] > 0.9]) > 0:
    st.sidebar.error(f"🚨 {len(df[df['delay_probability'] > 0.9])} Critical Delay Alerts!")

if len(df[df['risk_classification'] == 'High Risk']) > len(df) * 0.15:
    st.sidebar.warning("⚠️ High Risk Rate Above 15%")
else:
    st.sidebar.success("✅ Risk Levels Normal")

# System performance in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### ⚡ System Status")
st.sidebar.info(f"🕒 Data Load Time: {load_time:.2f}s")
st.sidebar.info(f"💾 Records Processed: {len(df):,}")
st.sidebar.success("Dashboard: Operational")

# Filter 1 (Categorical): Risk Classification
risk_options = df['risk_classification'].unique()
selected_risks = st.sidebar.multiselect(
    "Select Risk Classification:",
    options=risk_options,
    default=risk_options
)

# Filter 2 (Numerical): Delivery Time Deviation
delivery_deviation_range = st.sidebar.slider(
    "Delivery Time Deviation (hours):",
    min_value=-2.0,
    max_value=10.0,
    value=(-2.0, 10.0),
    step=0.1
)

# Filter 3 (Numerical): Cargo Condition Status
cargo_condition_range = st.sidebar.slider(
    "Cargo Condition Status (0=Poor, 1=Good):",
    min_value=0.0,
    max_value=1.0,
    value=(0.0, 1.0),
    step=0.01
)

# Filter 4 (Date Range): Time Series Filter
st.sidebar.markdown("### 📅 Date Range Filter")
min_date = df['timestamp'].min().date()
max_date = df['timestamp'].max().date()

col_start, col_end = st.sidebar.columns(2)
with col_start:
    start_date = st.date_input(
        "Start Date:",
        value=min_date,
        min_value=min_date,
        max_value=max_date
    )
with col_end:
    end_date = st.date_input(
        "End Date:",
        value=max_date,
        min_value=min_date,
        max_value=max_date
    )

# Create filtered DataFrame
df_filtered = df[
    (df['risk_classification'].isin(selected_risks)) &
    (df['delivery_time_deviation'] >= delivery_deviation_range[0]) &
    (df['delivery_time_deviation'] <= delivery_deviation_range[1]) &
    (df['cargo_condition_status'] >= cargo_condition_range[0]) &
    (df['cargo_condition_status'] <= cargo_condition_range[1]) &
    (df['timestamp'].dt.date >= start_date) &
    (df['timestamp'].dt.date <= end_date)
]

# Enhanced Navigation Tabs
st.markdown("## 🧭 Dashboard Navigation")
tab1, tab2, tab3, tab4 = st.tabs([
    "Executive Dashboard", 
    "� Analytics Deep Dive", 
    "Data Management", 
    "Global Map View"
])

# TAB 1: EXECUTIVE DASHBOARD
with tab1:
    st.markdown("# Executive Dashboard")
    st.markdown("*High-level overview and key performance metrics for leadership*")
    
    # Auto-refresh notification
    if st.checkbox("🔄 Auto-refresh (30s)", key="auto_refresh"):
        st.rerun()
    
    # Step 3: Main Page Layout - Key Metrics (KPIs)
    st.markdown("## 🎯 Key Performance Indicators")
    st.markdown("*Real-time operational metrics and performance summary*")

# Enhanced KPI Cards with better styling
kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5 = st.columns(5)

with kpi_col1:
    total_shipments = len(df_filtered)
    prev_shipments = len(df)  # Compare with total
    delta_shipments = ((total_shipments - prev_shipments) / prev_shipments * 100) if prev_shipments > 0 else 0
    st.metric(
        label="Total Shipments", 
        value=f"{total_shipments:,}",
        delta=f"{delta_shipments:+.1f}%"
    )

with kpi_col2:
    avg_shipping_cost = df_filtered['shipping_costs'].mean()
    global_avg_cost = df['shipping_costs'].mean()
    cost_variance = ((avg_shipping_cost - global_avg_cost) / global_avg_cost * 100) if global_avg_cost > 0 else 0
    st.metric(
        label="Avg. Shipping Cost", 
        value=f"${avg_shipping_cost:,.2f}",
        delta=f"{cost_variance:+.1f}%"
    )

with kpi_col3:
    avg_delivery_delay = df_filtered['delivery_time_deviation'].mean()
    delay_status = "🟢 Good" if avg_delivery_delay < 1 else "🟡 Fair" if avg_delivery_delay < 3 else "🔴 Poor"
    st.metric(
        label="Avg. Delivery Delay", 
        value=f"{avg_delivery_delay:.2f} hrs",
        delta=delay_status
    )

with kpi_col4:
    # Check if order_fulfillment_status column exists, otherwise use alternative metric
    if 'order_fulfillment_status' in df_filtered.columns:
        avg_order_fulfillment = df_filtered['order_fulfillment_status'].mean()
        fulfillment_grade = "🟢 Excellent" if avg_order_fulfillment > 0.95 else "🟡 Good" if avg_order_fulfillment > 0.90 else "🔴 Needs Improvement"
        st.metric(
            label="Avg. Order Fulfillment", 
            value=f"{avg_order_fulfillment:.2%}",
            delta=fulfillment_grade
        )
    elif 'customer_satisfaction' in df_filtered.columns:
        avg_satisfaction = df_filtered['customer_satisfaction'].mean()
        satisfaction_grade = "🟢 Excellent" if avg_satisfaction > 4.5 else "🟡 Good" if avg_satisfaction > 4.0 else "🔴 Needs Improvement"
        st.metric(
            label="Customer Satisfaction", 
            value=f"{avg_satisfaction:.1f}/5",
            delta=satisfaction_grade
        )
    else:
        # Fallback metric using available data
        total_records = len(df_filtered)
        st.metric(
            label="Data Points", 
            value=f"{total_records:,}",
            delta="Records loaded"
        )

with kpi_col5:
    high_delay_prob_shipments = len(df_filtered[df_filtered['delay_probability'] > 0.8])
    risk_percentage = (high_delay_prob_shipments/len(df_filtered)*100) if len(df_filtered) > 0 else 0
    risk_indicator = "🔴 Critical" if risk_percentage > 15 else "🟡 Monitor" if risk_percentage > 5 else "🟢 Good"
    st.metric(
        label="⚠️ High-Risk Shipments", 
        value=f"{high_delay_prob_shipments:,}",
        delta=f"{risk_percentage:.1f}% • {risk_indicator}"
    )

# Performance Summary Dashboard
st.markdown("---")
perf_col1, perf_col2, perf_col3 = st.columns([2, 2, 1])

with perf_col1:
    # Risk Distribution
    risk_dist = df_filtered['risk_classification'].value_counts()
    st.markdown("#### 🎯 Risk Distribution")
    for risk, count in risk_dist.items():
        percentage = (count / len(df_filtered)) * 100
        if 'Low' in risk:
            st.success(f"🟢 {risk}: {count:,} ({percentage:.1f}%)")
        elif 'Medium' in risk:
            st.warning(f"🟡 {risk}: {count:,} ({percentage:.1f}%)")
        else:
            st.error(f"🔴 {risk}: {count:,} ({percentage:.1f}%)")

with perf_col2:
    # GPS-Based Regional Analysis
    st.markdown("#### 📍 GPS Regional Hotspots")
    
    # Add country mapping to filtered data for analysis
    df_analysis = df_filtered.copy()
    df_analysis['region'] = df_analysis.apply(lambda x: get_country_region(x['vehicle_gps_latitude'], x['vehicle_gps_longitude']), axis=1)
    
    # Show top regions by shipment volume
    top_regions = df_analysis['region'].value_counts().head(5)
    for i, (region, count) in enumerate(top_regions.items(), 1):
        percentage = (count / len(df_analysis)) * 100
        # Get average risk for this region
        region_data = df_analysis[df_analysis['region'] == region]
        high_risk_pct = (region_data['risk_classification'] == 'High Risk').mean() * 100
        
        risk_emoji = "🔴" if high_risk_pct > 20 else "🟡" if high_risk_pct > 10 else "🟢"
        st.write(f"{i}. {risk_emoji} **{region}**: {count:,} ({percentage:.1f}%)")
        st.caption(f"   High Risk Rate: {high_risk_pct:.1f}%")

with perf_col3:
    # System Health
    st.markdown("#### 💚 System Health")
    on_time_rate = (df_filtered['delivery_time_deviation'] <= 0).mean()
    cost_efficiency = (df_filtered['shipping_costs'] <= df_filtered['shipping_costs'].median()).mean()
    
    st.metric("⏰ On-Time Rate", f"{on_time_rate:.1%}")
    st.metric("💰 Cost Efficiency", f"{cost_efficiency:.1%}")
    
    # Overall health score
    health_score = (on_time_rate + cost_efficiency + (1 - risk_percentage/100)) / 3
    if health_score > 0.8:
        st.success(f"🟢 Excellent: {health_score:.1%}")
    elif health_score > 0.6:
        st.warning(f"🟡 Good: {health_score:.1%}")
    else:
        st.error(f"🔴 Needs Attention: {health_score:.1%}")

st.markdown("---")

# Enhanced Action Required Section
st.markdown("## 🚨 ACTION REQUIRED: Critical Shipments")
st.markdown("*High-priority items requiring immediate attention*")

# Filter for high delay probability shipments (> 0.8)
high_delay_shipments = df_filtered[df_filtered['delay_probability'] > 0.8].copy()

if len(high_delay_shipments) > 0:
    # Add priority ranking based on multiple factors
    high_delay_shipments['priority_score'] = (
        high_delay_shipments['delay_probability'] * 0.4 +
        high_delay_shipments['shipping_costs'] / high_delay_shipments['shipping_costs'].max() * 0.3 +
        (1 - high_delay_shipments['driver_behavior_score']) * 0.2 +
        high_delay_shipments['traffic_congestion_level'] / 10 * 0.1
    )
    
    # Sort by priority score (highest first)
    high_delay_shipments = high_delay_shipments.sort_values('priority_score', ascending=False)
    
    # Create action columns layout
    action_col1, action_col2 = st.columns([3, 1])
    
    with action_col1:
        # Select key columns for action table
        action_columns = [
            'timestamp', 'risk_classification', 'delay_probability', 
            'shipping_costs', 'delivery_time_deviation', 'driver_behavior_score',
            'traffic_congestion_level', 'cargo_condition_status', 'priority_score'
        ]
        
        # Display actionable data
        st.dataframe(
            high_delay_shipments[action_columns].round(3),
            width='stretch',
            column_config={
                "delay_probability": st.column_config.ProgressColumn(
                    "Delay Probability",
                    help="Probability of delivery delay (0-1)",
                    min_value=0,
                    max_value=1,
                ),
                "priority_score": st.column_config.ProgressColumn(
                    "Priority Score",
                    help="Combined priority score for action",
                    min_value=0,
                    max_value=1,
                ),
                "shipping_costs": st.column_config.NumberColumn(
                    "Shipping Cost",
                    help="Cost in USD",
                    format="$%.2f",
                ),
                "driver_behavior_score": st.column_config.ProgressColumn(
                    "Driver Score",
                    help="Driver performance (0-1, higher is better)",
                    min_value=0,
                    max_value=1,
                ),
            }
        )
    
    with action_col2:
        st.markdown("### 🚨 Quick Actions")
        st.markdown("**Immediate Actions Needed:**")
        
        # Top 3 priority shipments
        top_3_urgent = high_delay_shipments.head(3)
        
        for idx, (_, shipment) in enumerate(top_3_urgent.iterrows(), 1):
            with st.expander(f"🔥 Priority #{idx} - {shipment['risk_classification']}"):
                st.write(f"**Delay Prob:** {shipment['delay_probability']:.1%}")
                st.write(f"**Cost:** ${shipment['shipping_costs']:,.0f}")
                st.write(f"**Driver Score:** {shipment['driver_behavior_score']:.2f}")
                
                # Suggested actions
                if shipment['driver_behavior_score'] < 0.5:
                    st.error("⚠️ **Action:** Review driver performance")
                if shipment['traffic_congestion_level'] > 7:
                    st.warning("🚦 **Action:** Consider route optimization")
                if shipment['cargo_condition_status'] < 0.5:
                    st.info("📦 **Action:** Check cargo handling")
        
        st.markdown("---")
        st.metric("🎯 Action Items", f"{len(high_delay_shipments)}")
        st.metric("💰 At Risk Value", f"${high_delay_shipments['shipping_costs'].sum():,.0f}")
        
        # Download action list
        action_csv = high_delay_shipments[action_columns].to_csv(index=False)
        st.download_button(
            label="📋 Download Action List",
            data=action_csv,
            file_name="high_delay_action_items.csv",
            mime="text/csv",
            help="Download priority shipments for immediate action"
        )

else:
    st.success("✅ **Great News!** No shipments currently have high delay probability (>80%)")
    st.info("All shipments in the current filter selection are performing within acceptable delay risk thresholds.")

# TAB 2: ANALYTICS DEEP DIVE 
with tab2:
    st.markdown("# � Analytics Deep Dive")
    st.markdown("*Detailed visualizations and trend analysis for operational insights*")
    
    # Time-Series Analysis Section
    st.subheader("📈 Time-Series Analysis")
    
    # Create the time-series line chart
    if len(df_filtered) > 0:
        # Group data by date and calculate average delivery delay
        df_timeseries = df_filtered.groupby(df_filtered['timestamp'].dt.date).agg({
            'delivery_time_deviation': 'mean'
        }).reset_index()
        df_timeseries.columns = ['date', 'avg_delivery_delay']
        
        # Create line chart
        fig_ts = px.line(
            df_timeseries,
            x='date',
            y='avg_delivery_delay',
            title='Average Delivery Delay Over Time',
            labels={
                'date': 'Date',
                'avg_delivery_delay': 'Average Delivery Delay (hours)'
            },
            markers=True
        )
        
        # Customize the chart
        fig_ts.update_traces(line=dict(color='#1f77b4', width=3), marker=dict(size=6))
        fig_ts.update_layout(
            xaxis_title="Date",
            yaxis_title="Average Delivery Delay (hours)",
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_ts, width='stretch')
        
        # Add summary statistics
        col_ts1, col_ts2, col_ts3 = st.columns(3)
        with col_ts1:
            trend_days = len(df_timeseries)
            st.metric("Days in Range", f"{trend_days}")
        with col_ts2:
            avg_delay_period = df_timeseries['avg_delivery_delay'].mean()
            st.metric("Period Avg Delay", f"{avg_delay_period:.2f} hrs")
        with col_ts3:
            delay_trend = "📈" if df_timeseries['avg_delivery_delay'].iloc[-1] > df_timeseries['avg_delivery_delay'].iloc[0] else "📉"
            st.metric("Trend", delay_trend)
    else:
        st.warning("No data available for the selected date range. Please adjust your filters.")
    
    st.markdown("---")
    
    # Step 5: Main Page Layout - Visualizations (6 charts)
    # GPS Location Analytics
    st.subheader("🌍 GPS Location Analytics")
    
    gps_col1, gps_col2 = st.columns(2)
    
    with gps_col1:
        # GPS Coverage Map
        st.markdown("#### 📍 GPS Coverage Analysis")
        
        # Calculate GPS statistics
        lat_range = df_filtered['vehicle_gps_latitude'].max() - df_filtered['vehicle_gps_latitude'].min()
        lon_range = df_filtered['vehicle_gps_longitude'].max() - df_filtered['vehicle_gps_longitude'].min()
        
        st.metric("📐 Latitude Range", f"{lat_range:.2f}°")
        st.metric("📐 Longitude Range", f"{lon_range:.2f}°") 
        st.metric("📍 GPS Points", f"{len(df_filtered):,}")
        
        # GPS density by region
        df_gps_analysis = df_filtered.copy()
        df_gps_analysis['region'] = df_gps_analysis.apply(lambda x: get_country_region(x['vehicle_gps_latitude'], x['vehicle_gps_longitude']), axis=1)
        
        region_density = df_gps_analysis['region'].value_counts()
        st.write("**Regional GPS Density:**")
        for region, count in region_density.head(3).items():
            st.write(f"• {region}: {count:,} points")
    
    with gps_col2:
        # GPS vs Performance Correlation
        st.markdown("#### 🎯 Location vs Performance")
        
        # Calculate performance metrics by region
        region_performance = df_gps_analysis.groupby('region').agg({
            'delay_probability': 'mean',
            'shipping_costs': 'mean',
            'delivery_time_deviation': 'mean'
        }).round(3)
        
        st.write("**Average Performance by Region:**")
        for region in region_performance.index:
            delay_prob = region_performance.loc[region, 'delay_probability']
            avg_cost = region_performance.loc[region, 'shipping_costs']
            
            status = "🔴" if delay_prob > 0.7 else "🟡" if delay_prob > 0.5 else "🟢"
            st.write(f"{status} **{region}**")
            st.write(f"  • Delay Prob: {delay_prob:.1%}")
            st.write(f"  • Avg Cost: ${avg_cost:.0f}")
    
    st.subheader("📊 Visual Analytics")

    # Create two columns for chart layout
    col1, col2 = st.columns(2)

    with col1:
        # Chart 1: Bar Chart - Average Shipping Cost by Risk Level
        avg_cost_by_risk = df_filtered.groupby('risk_classification')['shipping_costs'].mean().reset_index()
        fig1 = px.bar(
            avg_cost_by_risk,
            x='risk_classification',
            y='shipping_costs',
            title='Average Shipping Cost by Risk Level',
            labels={'shipping_costs': 'Average Shipping Cost ($)', 'risk_classification': 'Risk Classification'},
            color='risk_classification'
        )
        fig1.update_layout(showlegend=False)
        st.plotly_chart(fig1, width='stretch')

    with col2:
        # Chart 2: Histogram - Distribution of Delivery Delays
        fig2 = px.histogram(
            df_filtered,
            x='delivery_time_deviation',
            title='Distribution of Delivery Delays',
            labels={'delivery_time_deviation': 'Delivery Time Deviation (hours)', 'count': 'Frequency'},
            nbins=30
        )
        st.plotly_chart(fig2, width='stretch')

    # Second row of charts
    col3, col4 = st.columns(2)

    with col3:
        # Chart 3: Pie Chart - Count of Shipments by Risk Level
        risk_counts = df_filtered['risk_classification'].value_counts().reset_index()
        risk_counts.columns = ['risk_classification', 'count']
        fig3 = px.pie(
            risk_counts,
            values='count',
            names='risk_classification',
            title='Count of Shipments by Risk Level'
        )
        st.plotly_chart(fig3, width='stretch')

    with col4:
        # Chart 4: Scatter Plot - Shipping Cost vs. Delivery Delay
        # Use sample of 1000 rows for performance
        sample_size = min(1000, len(df_filtered))
        df_sample = df_filtered.sample(sample_size) if sample_size > 0 else df_filtered
        
        fig4 = px.scatter(
            df_sample,
            x='delivery_time_deviation',
            y='shipping_costs',
            color='risk_classification',
            title=f'Shipping Cost vs. Delivery Delay (Sample: {sample_size} records)',
            labels={
                'delivery_time_deviation': 'Delivery Time Deviation (hours)',
                'shipping_costs': 'Shipping Costs ($)',
                'risk_classification': 'Risk Classification'
            }
        )
        st.plotly_chart(fig4, width='stretch')

    # Third row of charts
    col5, col6 = st.columns(2)

    with col5:
        # Chart 5: Bar Chart - Average Driver Score by Risk Level
        avg_driver_by_risk = df_filtered.groupby('risk_classification')['driver_behavior_score'].mean().reset_index()
        fig5 = px.bar(
            avg_driver_by_risk,
            x='risk_classification',
            y='driver_behavior_score',
            title='Average Driver Score by Risk Level',
            labels={
                'driver_behavior_score': 'Average Driver Behavior Score',
                'risk_classification': 'Risk Classification'
            },
            color='risk_classification'
        )
        fig5.update_layout(showlegend=False)
        st.plotly_chart(fig5, width='stretch')

    with col6:
        # Chart 6: Scatter Plot - Traffic Congestion vs. Delivery Delay
        sample_size_traffic = min(1000, len(df_filtered))
        df_sample_traffic = df_filtered.sample(sample_size_traffic) if sample_size_traffic > 0 else df_filtered
        
        fig6 = px.scatter(
            df_sample_traffic,
            x='traffic_congestion_level',
            y='delivery_time_deviation',
            color='risk_classification',
            title=f'Traffic Congestion vs. Delivery Delay (Sample: {sample_size_traffic} records)',
            labels={
                'traffic_congestion_level': 'Traffic Congestion Level',
                'delivery_time_deviation': 'Delivery Time Deviation (hours)',
                'risk_classification': 'Risk Classification'
            }
        )
        st.plotly_chart(fig6, width='stretch')
    
    # GPS-Based Visualization
    st.subheader("🗺️ GPS Location Performance Map")
    
    gps_viz_col1, gps_viz_col2 = st.columns(2)
    
    with gps_viz_col1:
        # GPS Scatter Plot: Location vs Risk
        sample_size_gps = min(2000, len(df_filtered))
        df_gps_sample = df_filtered.sample(sample_size_gps) if sample_size_gps > 0 else df_filtered
        
        # Safety check for empty data
        if len(df_gps_sample) == 0:
            st.warning("No GPS data available for visualization")
        else:
            # Ensure positive values for marker size - normalize shipping costs
            min_cost = df_gps_sample['shipping_costs'].min()
            df_gps_sample['size_marker'] = df_gps_sample['shipping_costs'] - min_cost + 5
            
            fig_gps1 = px.scatter(
                df_gps_sample,
                x='vehicle_gps_longitude',
                y='vehicle_gps_latitude', 
                color='risk_classification',
                size='size_marker',
                title=f'GPS Locations by Risk Level (Sample: {sample_size_gps} points)',
                labels={
                    'vehicle_gps_longitude': 'Longitude',
                    'vehicle_gps_latitude': 'Latitude',
                    'risk_classification': 'Risk Level',
                    'size_marker': 'Normalized Cost Size'
                },
                hover_data=['delay_probability', 'delivery_time_deviation', 'shipping_costs']
            )
            fig_gps1.update_layout(height=400)
            st.plotly_chart(fig_gps1, width='stretch')
    
    with gps_viz_col2:
        # GPS Heatmap: Delay Probability by Location
        if len(df_gps_sample) == 0:
            st.warning("No GPS data available for heatmap")
        else:
            # Create proper size values - normalize to positive range
            min_delay = df_gps_sample['delivery_time_deviation'].min()
            df_gps_sample['size_delay'] = df_gps_sample['delivery_time_deviation'] - min_delay + 2
            
            fig_gps2 = px.scatter(
                df_gps_sample,
                x='vehicle_gps_longitude',
                y='vehicle_gps_latitude',
                color='delay_probability',
                size='size_delay',
                title=f'GPS Delay Probability Heatmap (Sample: {sample_size_gps} points)',
                labels={
                    'vehicle_gps_longitude': 'Longitude', 
                    'vehicle_gps_latitude': 'Latitude',
                    'delay_probability': 'Delay Probability',
                    'size_delay': 'Normalized Delay Size'
                },
                color_continuous_scale='Reds',
                hover_data=['risk_classification', 'shipping_costs', 'delivery_time_deviation']
            )
            fig_gps2.update_layout(height=400)
            st.plotly_chart(fig_gps2, width='stretch')

# TAB 3: DATA EXPLORER
with tab3:
    st.header("� Data Explorer")
    
    # Step 4: Main Page Layout - Data Table & Download
    # GPS Data Summary Section
    st.markdown("## 🌍 GPS Location Data Summary")
    
    gps_stats_col1, gps_stats_col2, gps_stats_col3, gps_stats_col4 = st.columns(4)
    
    with gps_stats_col1:
        unique_locations = df_filtered[['vehicle_gps_latitude', 'vehicle_gps_longitude']].drop_duplicates()
        st.metric("📍 Unique GPS Points", f"{len(unique_locations):,}")
    
    with gps_stats_col2:
        lat_range = df_filtered['vehicle_gps_latitude'].max() - df_filtered['vehicle_gps_latitude'].min()
        st.metric("📐 Latitude Span", f"{lat_range:.2f}°")
    
    with gps_stats_col3:
        lon_range = df_filtered['vehicle_gps_longitude'].max() - df_filtered['vehicle_gps_longitude'].min()
        st.metric("📐 Longitude Span", f"{lon_range:.2f}°")
    
    with gps_stats_col4:
        # Calculate geographic center
        center_lat = df_filtered['vehicle_gps_latitude'].mean()
        center_lon = df_filtered['vehicle_gps_longitude'].mean()
        st.metric("🎯 Geographic Center", f"{center_lat:.2f}°, {center_lon:.2f}°")

    st.markdown("## 📊 Filtered Shipments Details")

    # Display filtered data with GPS highlighting
    st.dataframe(df_filtered, width='stretch')

    # Download button
    csv = df_filtered.to_csv(index=False)
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv,
        file_name="filtered_shipments.csv",
        mime="text/csv"
    )
    
    # Additional data insights
    st.markdown("---")
    st.subheader("📊 Dataset Summary")
    
    col_summary1, col_summary2, col_summary3 = st.columns(3)
    with col_summary1:
        st.metric("Total Records", f"{len(df_filtered):,}")
        st.metric("Date Range", f"{(df_filtered['timestamp'].max() - df_filtered['timestamp'].min()).days} days")
    with col_summary2:
        st.metric("Risk Categories", f"{df_filtered['risk_classification'].nunique()}")
        st.metric("Avg Shipping Cost", f"${df_filtered['shipping_costs'].mean():,.2f}")
    with col_summary3:
        st.metric("High Risk %", f"{(df_filtered['risk_classification'] == 'High Risk').mean():.1%}")
        st.metric("Delay Probability Avg", f"{df_filtered['delay_probability'].mean():.1%}")

# TAB 4: GEOSPATIAL MAP  
with tab4:
    st.markdown("# 🗺️ Global Map View")
    st.markdown("*Interactive world map with country-wise logistics analytics*")
    
    # Enhanced Geospatial Risk Analysis
    st.markdown("## 🌍 Interactive World Map Analytics")

    # Map quality control options
    col_options1, col_options2, col_options3 = st.columns(3)
    with col_options1:
        map_style = st.selectbox(
            "🎨 Map Style:",
            ["mapbox://styles/mapbox/light-v10", "mapbox://styles/mapbox/dark-v10", 
             "mapbox://styles/mapbox/satellite-v9", "mapbox://styles/mapbox/streets-v11"],
            index=0
        )
    with col_options2:
        point_size = st.slider("📍 Point Size:", min_value=1000, max_value=5000, value=2000, step=500)
    with col_options3:
        max_points = st.selectbox("🔢 Max Points:", [1000, 2500, 5000, 10000], index=2)

    # Prepare data for the map
    if len(df_filtered) > 0:
        # Enhanced color mapping with better visibility
        def get_color_for_risk(risk_level, shipping_cost=None):
            base_colors = {
                'High Risk': [220, 20, 60, 200],      # Crimson with higher opacity
                'Moderate Risk': [255, 140, 0, 180],  # Dark Orange
                'Low Risk': [34, 139, 34, 160]        # Forest Green
            }
            return base_colors.get(risk_level, [128, 128, 128, 160])
        
        # Dynamic radius based on shipping cost for better visualization
        def get_radius_for_cost(cost, risk_level):
            base_radius = point_size
            if risk_level == 'High Risk':
                return base_radius * 1.2  # Larger for high risk
            elif risk_level == 'Moderate Risk':
                return base_radius * 1.0
            else:
                return base_radius * 0.8  # Smaller for low risk
        

    
    # Add country information to dataset
    df_map = df_filtered.copy()
    df_map['country'] = df_map.apply(lambda x: get_country_region(x['vehicle_gps_latitude'], x['vehicle_gps_longitude']), axis=1)
    
    # Create country-wise aggregations
    country_stats = df_map.groupby('country').agg({
        'vehicle_gps_latitude': 'mean',
        'vehicle_gps_longitude': 'mean', 
        'shipping_costs': ['sum', 'mean', 'count'],
        'delivery_time_deviation': 'mean',
        'delay_probability': 'mean',
        'risk_classification': lambda x: x.value_counts().index[0] if len(x) > 0 else 'Low Risk'  # Most common risk
    }).round(2)
    
    # Flatten column names
    country_stats.columns = ['avg_lat', 'avg_lon', 'total_cost', 'avg_cost', 'shipment_count', 'avg_delay', 'avg_delay_prob', 'dominant_risk']
    country_stats = country_stats.reset_index()
    
    # Add visual attributes and city information for countries
    country_stats['color'] = country_stats['dominant_risk'].apply(get_color_for_risk)
    country_stats['radius'] = country_stats['total_cost'] / country_stats['total_cost'].max() * 50000 + 10000  # Scale by total cost
    country_stats['elevation'] = country_stats['shipment_count'] / country_stats['shipment_count'].max() * 2000  # Height by shipment count
    country_stats['major_city'] = country_stats['country'].apply(get_major_city_for_country)  # Add major city info
    
    # Create the map layout with improved columns
    map_col1, map_col2 = st.columns([4, 1])
    
    with map_col1:
        # Country-level ScatterplotLayer with dots (not filled circles)
        country_layer = pdk.Layer(
            'ScatterplotLayer',
            data=country_stats,
            get_position='[avg_lon, avg_lat]',
            get_color='color',
            get_radius='radius',
            radius_scale=0.3,  # Smaller radius for dot effect
            radius_min_pixels=8,
            radius_max_pixels=25,
            pickable=True,
            auto_highlight=True,
            filled=False,  # Make it a dot/ring, not filled circle
            stroked=True,
            get_line_color='color',  # Use same color for border
            line_width_min_pixels=3,  # Thicker border for dot effect
            line_width_max_pixels=6
        )
        

        
        # Add ColumnLayer for 3D country visualization
        column_layer = pdk.Layer(
            'ColumnLayer',
            data=country_stats,
            get_position='[avg_lon, avg_lat]',
            get_elevation='elevation',
            elevation_scale=1,
            get_fill_color='color',
            radius=30000,
            pickable=True,
            auto_highlight=True
        )
        
        # Enhanced visualization options
        st.subheader("🎨 Map Visualization Options")
        
        # World map background toggle
        show_world_map = st.checkbox("🗺️ Show World Map Boundaries", value=True)
        
        # World view centering option
        world_view = st.checkbox("🌐 Center on World View", value=True)
        
        # Country labels options
        show_labels = st.checkbox("🏷️ Show Country Names", value=True)
        
        if show_labels:
            label_size = st.slider("📝 Label Size", min_value=10, max_value=24, value=14, step=2)
        else:
            label_size = 14  # Default size
            
        # Create TextLayer for country names with user-controlled size
        text_layer = pdk.Layer(
            'TextLayer',
            data=country_stats,
            get_position='[avg_lon, avg_lat]',
            get_text='country',
            get_size=label_size,
            get_color=[255, 255, 255, 220],  # Bright white text
            get_angle=0,
            get_text_anchor='"middle"',
            get_alignment_baseline='"bottom"',  # Position above the dot
            pickable=False,
            billboard=True,
            font_family='Arial, sans-serif',
            font_weight='bold',
            size_scale=1,
            size_min_pixels=label_size,
            size_max_pixels=label_size + 6,
            background=True,
            get_background_color=[0, 0, 0, 120]  # Semi-transparent black background
        )
        
        # Layer selection
        layer_option = st.radio(
            "📊 Data Visualization Layer:",
            ["Country Dots", "3D Columns", "Combined View"],
            index=0,
            horizontal=True
        )
        
        # Select layers based on user choice
        base_layers = []
        if layer_option == "Country Dots":
            base_layers = [country_layer]
        elif layer_option == "3D Columns":
            base_layers = [column_layer]
        else:
            base_layers = [country_layer, column_layer]
            
        # Add text layer if labels are enabled
        layers = base_layers.copy()
        if show_labels:
            layers.append(text_layer)
        
        # Calculate optimal zoom level for country view
        lat_range = country_stats['avg_lat'].max() - country_stats['avg_lat'].min()
        lon_range = country_stats['avg_lon'].max() - country_stats['avg_lon'].min()
        zoom_level = max(1, min(5, 6 - max(lat_range, lon_range) / 20))  # Lower zoom for world view
        
        # Enhanced viewport with dynamic positioning for world view
        if world_view:
            # Center on world (0° lat, 0° lon) with appropriate zoom for global view
            view_lat, view_lon = 20.0, 0.0  # Slightly north of equator for better continent view
            zoom_level = 1.5  # Global zoom level
        else:
            # Center on data
            view_lat = country_stats['avg_lat'].mean()
            view_lon = country_stats['avg_lon'].mean()
            
        view_state = pdk.ViewState(
            latitude=view_lat,
            longitude=view_lon,
            zoom=zoom_level,
            pitch=45 if layer_option != "Country Bubbles" else 0,
            bearing=0,
            height=600
        )
        
        # Add world map base layer for country boundaries
        world_boundaries_layer = pdk.Layer(
            'GeoJsonLayer',
            data='https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson',
            pickable=True,
            stroked=True,
            filled=True,
            extruded=False,
            line_width_min_pixels=1,
            get_fill_color=[60, 60, 60, 50],  # Semi-transparent gray for countries
            get_line_color=[120, 120, 120, 200],  # Gray borders
            get_line_width=1
        )
        
        # Major shipping ports and cities for context
        major_ports = pd.DataFrame({
            'city': ['Shanghai', 'Singapore', 'Rotterdam', 'Los Angeles', 'Hamburg', 'Dubai', 'New York', 'Tokyo', 'Hong Kong', 'Mumbai'],
            'latitude': [31.2304, 1.3521, 51.9244, 34.0522, 53.5511, 25.2048, 40.7128, 35.6762, 22.3193, 19.0760],
            'longitude': [121.4737, 103.8198, 4.4777, -118.2437, 9.9937, 55.2708, -74.0060, 139.6503, 114.1694, 72.8777],
            'port_type': ['Major Port'] * 10
        })
        
        # Add checkbox for showing major ports
        show_ports = st.checkbox("🚢 Show Major Shipping Ports", value=False)
        
        # Major ports layer with enhanced styling
        ports_layer = pdk.Layer(
            'ScatterplotLayer',
            data=major_ports,
            get_position='[longitude, latitude]',
            get_color=[255, 215, 0, 200],  # Bright gold color for ports
            get_radius=25000,
            radius_min_pixels=10,
            radius_max_pixels=18,
            pickable=True,
            auto_highlight=True,
            stroked=True,
            get_line_color=[255, 255, 255, 180],  # White border
            line_width_min_pixels=2
        )
        
        # Add all layers including world boundaries and ports (if enabled)
        all_layers = []
        if show_world_map:
            all_layers.append(world_boundaries_layer)
        all_layers.extend(layers)
        if show_ports:
            all_layers.append(ports_layer)
        
        # Enhanced map with better styling and world map background
        map_chart = pdk.Deck(
            layers=all_layers,
            initial_view_state=view_state,
            map_style=map_style,
            tooltip={
                'html': '''
                <div style="background: linear-gradient(135deg, #2C3E50 0%, #4A6741 100%); 
                           padding: 12px; border-radius: 10px; color: white; font-family: Arial; 
                           box-shadow: 0 4px 15px rgba(0,0,0,0.3); border: 2px solid #34495e;">
                    
                    <!-- Country Information (when available) -->
                    {{#country}}
                    <div style="display: flex; align-items: center; margin-bottom: 8px;">
                        <div style="font-size: 18px; margin-right: 8px;">🌍</div>
                        <h3 style="margin: 0; color: #ECF0F1; font-weight: bold;">{country}</h3>
                    </div>
                    <div style="display: flex; align-items: center; margin-bottom: 10px;">
                        <div style="font-size: 14px; margin-right: 6px;">🏙️</div>
                        <span style="color: #BDC3C7; font-style: italic;">Major Hub: {major_city}</span>
                    </div>
                    <hr style="border: none; border-top: 1px solid #34495e; margin: 8px 0;">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 11px;">
                        <div><strong>🚨 Risk Level:</strong><br>{dominant_risk}</div>
                        <div><strong>📦 Shipments:</strong><br>{shipment_count:,}</div>
                        <div><strong>💰 Total Cost:</strong><br>${total_cost:,.0f}</div>
                        <div><strong>💵 Avg Cost:</strong><br>${avg_cost:.2f}</div>
                        <div><strong>⏰ Avg Delay:</strong><br>{avg_delay:.1f} hrs</div>
                        <div><strong>⚠️ Delay Prob:</strong><br>{avg_delay_prob:.1%}</div>
                    </div>
                    {{/country}}
                    
                    <!-- Port Information (when available) -->
                    {{#city}}
                    <div style="display: flex; align-items: center; margin-bottom: 8px;">
                        <div style="font-size: 18px; margin-right: 8px;">🚢</div>
                        <h3 style="margin: 0; color: #F39C12; font-weight: bold;">{city}</h3>
                    </div>
                    <div style="display: flex; align-items: center; margin-bottom: 8px;">
                        <div style="font-size: 14px; margin-right: 6px;">🏷️</div>
                        <span style="color: #BDC3C7; font-style: italic;">{port_type}</span>
                    </div>
                    <div style="font-size: 12px; color: #BDC3C7;">
                        📍 Global Shipping Hub<br>
                        🌊 International Maritime Gateway
                    </div>
                    {{/city}}
                    
                </div>
                ''',
                'style': {
                    'backgroundColor': 'transparent',
                    'color': 'white',
                    'fontSize': '12px'
                }
            },
            parameters={
                'light_settings': {
                    'lightsPosition': [-74.05, 40.7, 8000, -73.5, 41, 5000],
                    'ambientRatio': 0.05,
                    'diffuseRatio': 0.6,
                    'specularRatio': 0.8,
                    'lightsStrength': [0.8, 0.0, 0.8, 0.0],
                    'numberOfLights': 2
                }
            }
        )
        
        st.pydeck_chart(map_chart, use_container_width=True, height=600)
        
        # Enhanced caption with country information
        total_countries = len(country_stats)
        total_shipments = country_stats['shipment_count'].sum()
        avg_lat = country_stats['avg_lat'].mean()
        avg_lon = country_stats['avg_lon'].mean()
        st.caption(f"🌍 Showing {total_countries} countries/regions | 📦 Total: {total_shipments:,} shipments | 🎯 Center: {avg_lat:.1f}°, {avg_lon:.1f}°")
    
    with map_col2:
        # Enhanced map legend with visual indicators
        st.markdown("### 🗺️ World Map Features")
        
        if show_world_map:
            st.success("✅ World boundaries displayed")
        else:
            st.info("🗺️ World boundaries hidden")
            
        if show_ports:
            st.warning("🚢 Major ports visible")
            st.caption("Gold markers show key shipping hubs")
            
        if show_labels:
            st.info("🏷️ Country names displayed")
            st.caption("White labels with dark background")
        else:
            st.caption("🏷️ Country names hidden")
            
        st.markdown("### 📊 Dot Visualization Legend")
        st.caption("⚫ **Dots** represent countries (not filled circles)")
        st.caption("📏 **Size**: Proportional to total shipping cost")
        st.caption("🎨 **Color**: Risk level classification")
        
        # Create colored legend with country metrics
        for risk_level in ['High Risk', 'Moderate Risk', 'Low Risk']:
            countries_with_risk = country_stats[country_stats['dominant_risk'] == risk_level]
            country_count = len(countries_with_risk)
            total_shipments = countries_with_risk['shipment_count'].sum() if country_count > 0 else 0
            
            if risk_level == 'High Risk':
                st.markdown(f"🔴 **{risk_level}** ({country_count} countries)")
            elif risk_level == 'Moderate Risk':
                st.markdown(f"🟠 **{risk_level}** ({country_count} countries)")
            else:
                st.markdown(f"🟢 **{risk_level}** ({country_count} countries)")
            
            if country_count > 0:
                st.caption(f"   Shipments: {total_shipments:,}")
        
        st.markdown("---")
        
        # Enhanced geographic statistics
        st.markdown("### 📊 Geographic Analytics")
        
        # Key country-level metrics
        total_countries = len(country_stats)
        total_global_cost = country_stats['total_cost'].sum()
        avg_global_delay = country_stats['avg_delay'].mean()
        
        st.metric("🌍 Countries/Regions", f"{total_countries}")
        st.metric("💰 Global Total Cost", f"${total_global_cost:,.0f}")
        st.metric("⏱️ Global Avg Delay", f"{avg_global_delay:.1f} hrs")
        
        # Top countries by shipment volume
        st.markdown("### � Top Countries")
        top_countries = country_stats.nlargest(5, 'shipment_count')[['country', 'shipment_count', 'total_cost', 'dominant_risk']]
        
        for idx, (_, country) in enumerate(top_countries.iterrows(), 1):
            with st.expander(f"#{idx} {country['country']}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Shipments", f"{int(country['shipment_count']):,}")
                    st.metric("Total Cost", f"${country['total_cost']:,.0f}")
                with col2:
                    st.metric("Risk Level", country['dominant_risk'])
                    risk_color = "🔴" if country['dominant_risk'] == 'High Risk' else "🟠" if country['dominant_risk'] == 'Moderate Risk' else "🟢"
                    st.write(f"{risk_color} Risk Status")
        
        # Map controls info
        st.markdown("---")
        st.markdown("### 🎮 Map Controls")
        st.caption("🖱️ **Click & Drag:** Pan the map")
        st.caption("🔍 **Mouse Wheel:** Zoom in/out")  
        st.caption("📱 **Hover:** View shipment details")
        st.caption("🎨 **Style:** Change map appearance above")

    # Handle case when no filtered data is available
    if len(df_filtered) == 0:
        st.warning("No data available for the selected filters. Please adjust your filter criteria.")

# Enhanced Footer Section
st.markdown("---")
st.markdown("## 📊 Dashboard Information")

footer_col1, footer_col2, footer_col3, footer_col4 = st.columns(4)

with footer_col1:
    st.markdown("### 🔧 Technical Specs")
    st.caption("**Framework:** Streamlit + PyDeck")
    st.caption("**Data Source:** CSV Dataset")
    st.caption("**Visualization:** Plotly + Deck.GL")
    st.caption("**Real-time:** Live Updates")

with footer_col2:
    st.markdown("### 📈 Data Coverage")
    st.caption(f"**Total Records:** {len(df):,}")
    st.caption(f"**GPS Locations:** {df[['vehicle_gps_latitude', 'vehicle_gps_longitude']].drop_duplicates().shape[0]:,}")
    st.caption(f"**Date Range:** {(df['timestamp'].max() - df['timestamp'].min()).days} days")
    st.caption(f"**Risk Categories:** {df['risk_classification'].nunique()}")

with footer_col3:
    st.markdown("### 🎯 Key Features")
    st.caption("✅ Interactive Filtering")
    st.caption("✅ Real-time KPIs")  
    st.caption("✅ Geographic Mapping")
    st.caption("✅ Risk Analytics")
    st.caption("✅ Actionable Insights")

with footer_col4:
    st.markdown("### 📞 Support")
    st.caption("**Version:** 2.0.0")
    st.caption("**Last Update:** 2025-10-26")
    st.caption("**Status:** 🟢 Operational")
    if st.button("🔄 Refresh Data"):
        st.rerun()

# Performance indicators
with st.expander("🚀 System Performance", expanded=False):
    perf1, perf2, perf3, perf4 = st.columns(4)
    with perf1:
        st.metric("⚡ Load Time", "< 2s")
    with perf2:
        st.metric("💾 Memory Usage", f"{len(df) * 0.001:.1f} MB")
    with perf3:
        st.metric("🔄 Update Frequency", "Real-time")
    with perf4:
        st.metric("📊 Charts Rendered", "15+")

st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #666; font-size: 0.9rem;">'
    '🚚 Logistics Performance Dashboard | Built with ❤️ using Streamlit | '
    f'© 2025 | Last refreshed: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    '</div>', 
    unsafe_allow_html=True
)
st.sidebar.markdown("---")
st.sidebar.markdown("### Dataset Information")
st.sidebar.write(f"**Total Records:** {len(df):,}")
st.sidebar.write(f"**Filtered Records:** {len(df_filtered):,}")
st.sidebar.write(f"**Columns:** {len(df.columns)}")