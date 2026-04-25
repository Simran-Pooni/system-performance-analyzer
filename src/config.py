# Central configuration for the application

# Page configuration
PAGE_CONFIG = {
    "page_title": "System Performance Analyzer",
    "page_icon": "📊",
    "layout": "wide"
}

# Available metrics
AVAILABLE_METRICS = ["temperature", "cpu_usage", "response_time", "load"]
DEFAULT_METRICS = ["cpu_usage", "temperature"]

# UI Emojis
EMOJIS = {
    "title": "📊",
    "filter": "⚙️",
    "apply": "🔄",
    "records": "📈",
    "date": "📅",
    "metrics": "📊",
    "time": "⏱️",
    "table": "📋",
    "timeseries": "📈",
    "stats": "📊",
    "histogram": "📊",
    "anomaly": "⚠️",
    "correlation": "🔗"
}

# Anomaly detection threshold (Z-score)
ANOMALY_Z_THRESHOLD = 2

# Display precision for floats
FLOAT_PRECISION = 2

# Colors
COLOR_SCHEME = {
    "default": "#1f77b4",
    "correlation": "RdBu"
}

# Histogram bins
HISTOGRAM_BINS = 30

# Plot height
PLOT_HEIGHT = {
    "timeseries": 450,
    "histogram": 350,
    "correlation": 400
}
