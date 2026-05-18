# Correlation component

import streamlit as st
import pandas as pd
import plotly.express as px
from src.config import EMOJIS, PLOT_HEIGHT, COLOR_SCHEME


def render_correlation(df_filtered: pd.DataFrame, selected_metrics: list):
    """Render correlation analysis heatmap.
    
    Args:
        df_filtered: Filtered DataFrame
        selected_metrics: List of selected metrics
    """
    if len(selected_metrics) < 2:
        st.info("Select at least 2 metrics to see correlation analysis.")
        return
    
    st.subheader(f"{EMOJIS['correlation']} Correlation Analysis")
    
    correlation_matrix = df_filtered[selected_metrics].corr()
    
    fig_corr = px.imshow(
        correlation_matrix,
        labels=dict(x="Metric", y="Metric", color="Correlation"),
        x=correlation_matrix.columns,
        y=correlation_matrix.columns,
        color_continuous_scale=COLOR_SCHEME['correlation'],
        zmin=-1,
        zmax=1,
        text_auto=".2f"
    )
    fig_corr.update_layout(height=PLOT_HEIGHT['correlation'])
    st.plotly_chart(fig_corr, use_container_width=True)
    
    st.markdown("**Interpretation:**")
    st.write("- **Red**: Positive correlation (metrics move together)")
    st.write("- **Blue**: Negative correlation (metrics move opposite)")
    st.write("- **White**: No correlation")
    
    st.divider()
