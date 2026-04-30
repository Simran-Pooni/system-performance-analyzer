# Sidebar filters component

import streamlit as st
from datetime import timedelta
import pandas as pd
from src.config import EMOJIS, AVAILABLE_METRICS, DEFAULT_METRICS


def render_sidebar(df: pd.DataFrame) -> dict:
    """Render sidebar filters and return selected values.
    
    Args:
        df: DataFrame with timestamp column
        
    Returns:
        Dictionary with keys: start_date, end_date, selected_metrics, apply_filter
    """
    with st.sidebar:
        st.header(f"{EMOJIS['filter']} Filters")
        
        # Date range
        min_date = df['timestamp'].min().date()
        max_date = df['timestamp'].max().date()
        
        start_date = st.date_input(
            "Start Date",
            value=min_date,
            min_value=min_date,
            max_value=max_date
        )
        
        end_date = st.date_input(
            "End Date",
            value=max_date,
            min_value=min_date,
            max_value=max_date
        )
        
        # Metrics selection
        selected_metrics = st.multiselect(
            "Select Metrics",
            AVAILABLE_METRICS,
            default=DEFAULT_METRICS
        )
        
        apply_filter = st.button(f"{EMOJIS['apply']} Apply Filter", use_container_width=True)
    
    return {
        "start_date": start_date,
        "end_date": end_date,
        "selected_metrics": selected_metrics,
        "apply_filter": apply_filter
    }
