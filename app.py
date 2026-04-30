import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

from src.config import PAGE_CONFIG, EMOJIS
from src.db_loader import query_all_data
from src.components import (
    sidebar,
    summary,
    data_table,
    visualization,
    statistics,
    anomalies,
    correlation
)

# ==================== PAGE SETUP ====================
st.set_page_config(**PAGE_CONFIG)

st.title(f"{EMOJIS['title']} System Performance Analyzer")
st.markdown("Real-time analysis and monitoring of system performance metrics.")

# ==================== LOAD DATA ====================
@st.cache_data
def load_all_data():
    return query_all_data()


df = load_all_data()
df['timestamp'] = pd.to_datetime(df['timestamp'])

# ==================== SIDEBAR FILTERS ====================
filter_state = sidebar.render_sidebar(df)

start_date = filter_state["start_date"]
end_date = filter_state["end_date"]
selected_metrics = filter_state["selected_metrics"]

# ==================== FILTER DATA ====================
start_datetime = pd.to_datetime(start_date)
end_datetime = pd.to_datetime(end_date) + timedelta(days=1)

df_filtered = df[(df['timestamp'] >= start_datetime) & (df['timestamp'] < end_datetime)].copy()

if df_filtered.empty:
    st.warning("⚠️ No data found for the selected date range.")
    st.stop()

# ==================== RENDER COMPONENTS ====================
summary.render_summary(df_filtered, start_date, end_date, selected_metrics)
data_table.render_data_table(df_filtered, selected_metrics)
visualization.render_visualization(df_filtered, selected_metrics)
statistics.render_statistics(df_filtered, selected_metrics)
anomalies.render_anomalies(df_filtered, selected_metrics)
correlation.render_correlation(df_filtered, selected_metrics)

# ==================== FOOTER ====================
st.markdown("---")
st.markdown(
    f"""
    <div style='text-align: center'>
        <small>System Performance Analyzer • Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</small>
    </div>
    """,
    unsafe_allow_html=True
)
