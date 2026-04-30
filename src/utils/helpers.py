# Helper functions for data processing and formatting

def format_metric_name(metric: str) -> str:
    """Convert metric name to readable format.
    
    Examples:
        cpu_usage -> CPU Usage
        response_time -> Response Time
    """
    return metric.replace('_', ' ').title()


def get_time_span_days(start_datetime, end_datetime) -> int:
    """Calculate number of days between two datetime objects."""
    return (end_datetime - start_datetime).days


def format_float(value: float, precision: int = 2) -> str:
    """Format float value with specified precision."""
    return f"{value:.{precision}f}"


def calculate_anomaly_percentage(anomaly_count: int, total_count: int) -> float:
    """Calculate anomaly percentage."""
    if total_count == 0:
        return 0.0
    return (anomaly_count / total_count) * 100
