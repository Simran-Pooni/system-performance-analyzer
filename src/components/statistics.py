# Statistics component

import streamlit as st
import pandas as pd
from src.config import EMOJIS, FLOAT_PRECISION
from src.utils.helpers import format_metric_name, format_float


def render_statistics(df_filtered: pd.DataFrame, selected_metrics: list):
    """Render statistical summary for selected metrics.
    
    Args:
        df_filtered: Filtered DataFrame
        selected_metrics: List of selected metrics
    """
    st.subheader(f"{EMOJIS['stats']} Statistical Summary")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Descriptive Statistics")
        stats_data = []
        
        for metric in selected_metrics:
            stats_dict = {
                "Metric": format_metric_name(metric),
                "Mean": format_float(df_filtered[metric].mean(), FLOAT_PRECISION),
                "Std Dev": format_float(df_filtered[metric].std(), FLOAT_PRECISION),
                "Min": format_float(df_filtered[metric].min(), FLOAT_PRECISION),
                "Max": format_float(df_filtered[metric].max(), FLOAT_PRECISION)
            }
            stats_data.append(stats_dict)
        
        stats_df = pd.DataFrame(stats_data)
        st.dataframe(stats_df, use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("#### Detailed Stats")
        for metric in selected_metrics:
            with st.expander(f"📌 {format_metric_name(metric)} Details"):
                col_a, col_b = st.columns(2)
                
                with col_a:
                    st.metric("Mean", format_float(df_filtered[metric].mean(), FLOAT_PRECISION))
                    st.metric("Median", format_float(df_filtered[metric].median(), FLOAT_PRECISION))
                
                with col_b:
                    st.metric("Std Dev", format_float(df_filtered[metric].std(), FLOAT_PRECISION))
                    range_val = df_filtered[metric].max() - df_filtered[metric].min()
                    st.metric("Range", format_float(range_val, FLOAT_PRECISION))
    
    st.divider()
