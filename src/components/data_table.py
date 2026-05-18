# Data table component

import streamlit as st
import pandas as pd
from src.config import EMOJIS


def render_data_table(df_filtered: pd.DataFrame, selected_metrics: list):
    """Render data table with selected metrics.
    
    Args:
        df_filtered: Filtered DataFrame
        selected_metrics: List of selected metrics to display
    """
    st.subheader(f"{EMOJIS['table']} Data Table")
    
    # Select columns: timestamp + selected metrics
    display_df = df_filtered[['timestamp'] + selected_metrics].sort_values(
        'timestamp', ascending=False
    )
    
    st.dataframe(
        display_df,
        use_container_width=True,
        height=250
    )
    
    st.divider()
