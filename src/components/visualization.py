# Visualization component (Time Series)

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from src.config import EMOJIS, PLOT_HEIGHT
from src.utils.helpers import format_metric_name


def render_visualization(df_filtered: pd.DataFrame, selected_metrics: list):
    """Render time series visualization.
    
    Args:
        df_filtered: Filtered DataFrame
        selected_metrics: List of selected metrics to plot
    """
    st.subheader(f"{EMOJIS['timeseries']} Time Series Visualization")
    
    if not selected_metrics:
        st.info("Please select at least one metric to display.")
        return
    
    fig = go.Figure()
    
    for metric in selected_metrics:
        fig.add_trace(go.Scatter(
            x=df_filtered['timestamp'],
            y=df_filtered[metric],
            mode='lines',
            name=format_metric_name(metric),
            hovertemplate='<b>%{fullData.name}</b><br>Time: %{x}<br>Value: %{y:.2f}<extra></extra>'
        ))
    
    fig.update_layout(
        title="Performance Metrics Over Time",
        xaxis_title="Timestamp",
        yaxis_title="Value",
        hovermode='x unified',
        height=PLOT_HEIGHT['timeseries'],
        template="plotly_white"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.divider()
