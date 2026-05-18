# Summary metrics component

import streamlit as st
import pandas as pd
from datetime import datetime
from src.config import EMOJIS
from src.utils.helpers import get_time_span_days, format_metric_name


def render_summary(df_filtered: pd.DataFrame, start_date, end_date, selected_metrics: list):
    """Render summary KPI cards.
    
    Args:
        df_filtered: Filtered DataFrame
        start_date: Start date
        end_date: End date
        selected_metrics: List of selected metrics
    """
    col1, col2, col3, col4 = st.columns(4)
    
    end_datetime = pd.to_datetime(end_date)
    start_datetime = pd.to_datetime(start_date)
    time_span = get_time_span_days(start_datetime, end_datetime + pd.Timedelta(days=1))
    
    with col1:
        st.metric(f"{EMOJIS['records']} Total Records", len(df_filtered))
    
    with col2:
        st.metric(f"{EMOJIS['date']} Date Range", f"{start_date} to {end_date}")
    
    with col3:
        st.metric(f"{EMOJIS['metrics']} Metrics Shown", len(selected_metrics))
    
    with col4:
        st.metric(f"{EMOJIS['time']} Time Span", f"{time_span} days")
    
    st.divider()
