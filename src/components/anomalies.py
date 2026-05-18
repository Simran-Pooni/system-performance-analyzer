# Anomalies component

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats
from src.config import EMOJIS, ANOMALY_Z_THRESHOLD, HISTOGRAM_BINS, PLOT_HEIGHT, COLOR_SCHEME
from src.utils.helpers import format_metric_name, calculate_anomaly_percentage


def render_anomalies(df_filtered: pd.DataFrame, selected_metrics: list):
    """Render distribution histograms and anomaly detection.
    
    Args:
        df_filtered: Filtered DataFrame
        selected_metrics: List of selected metrics
    """
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"{EMOJIS['histogram']} Distribution (Histograms)")
        for metric in selected_metrics:
            fig_hist = px.histogram(
                df_filtered,
                x=metric,
                nbins=HISTOGRAM_BINS,
                title=f"Distribution of {format_metric_name(metric)}",
                labels={metric: format_metric_name(metric)},
                color_discrete_sequence=[COLOR_SCHEME['default']]
            )
            fig_hist.update_layout(height=PLOT_HEIGHT['histogram'], showlegend=False)
            st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        st.subheader(f"{EMOJIS['anomaly']} Anomaly Detection (Z-Score)")
        anomaly_summary = []
        
        for metric in selected_metrics:
            z_scores = np.abs(stats.zscore(df_filtered[metric]))
            anomaly_count = (z_scores > ANOMALY_Z_THRESHOLD).sum()
            anomaly_percentage = calculate_anomaly_percentage(anomaly_count, len(df_filtered))
            
            anomaly_summary.append({
                "Metric": format_metric_name(metric),
                "Anomalies": anomaly_count,
                "Percentage": f"{anomaly_percentage:.2f}%"
            })
            
            # Visual indicator
            if anomaly_count == 0:
                st.success(f"**{format_metric_name(metric)}**: No anomalies detected")
            elif anomaly_percentage < 2:
                st.info(f"{EMOJIS['anomaly']} **{format_metric_name(metric)}**: {anomaly_count} anomalies ({anomaly_percentage:.2f}%)")
            else:
                st.warning(f"**{format_metric_name(metric)}**: {anomaly_count} anomalies ({anomaly_percentage:.2f}%)")
        
        st.divider()
        st.markdown("#### Anomaly Summary Table")
        anomaly_df = pd.DataFrame(anomaly_summary)
        st.dataframe(anomaly_df, use_container_width=True, hide_index=True)
    
    st.divider()
