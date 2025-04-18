import streamlit as st
import pandas as pd
import plotly.express as px

# Simulated KPI data for visuals
data = {
    'KPI': ['Automated Resolution Rate', 'First Contact Resolution', 'Average Handling Time',
            'ROI', 'Cost per Resolution', 'NPS', 'CSAT', 'Precision', 'Recall', 'F1-Score'],
    'Value': [87, 78, 3.5, 1.6, 4.2, 72, 88, 0.91, 0.89, 0.90],
    'Category': ['Operational', 'Operational', 'Operational',
                 'Financial', 'Financial', 'Customer', 'Customer',
                 'AI Model', 'AI Model', 'AI Model']
}
kpi_df = pd.DataFrame(data)

# --- PAGE SETUP ---
st.set_page_config(page_title="AIVS Co. KPI Dashboard", layout="wide")

# --- SEARCH & FILTERS ---
st.title("AIVS Co. KPI Dashboard")
search_query = st.text_input("🔍 Search for a KPI", "")
col1, col2 = st.columns(2)

with col1:
    timeline = st.selectbox("📅 Select Timeline", ["Last 7 days", "Last 30 days", "Quarter", "Year"])

with col2:
    project_filter = st.multiselect("📂 Filter by Project", ["Expert Finder", "Lead Generator"])

# --- TAB SETUP ---
tabs = st.tabs(["📊 Overview", "🏢 Company KPIs", "🚀 Project KPIs"])

# --- TAB 1: Overview ---
with tabs[0]:
    st.subheader("📊 High-Level Overview")

    # Chart Section
    chart = px.bar(kpi_df, x='KPI', y='Value', color='Category', title="Company & Project KPI Overview")
    st.plotly_chart(chart, use_container_width=True)

    # KPI Containers
    st.markdown("""<div style='background-color:#f0f0f5; padding:20px; border-radius:15px'>
    <h3 style='color:#333'>📌 Company-Level KPIs</h3>
    <ul><li>ROI: 1.6x</li><li>Avg Handling Time: 3.5 mins</li><li>Net Promoter Score: 72</li></ul>
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div style='background-color:#e8f9f3; padding:20px; border-radius:15px; margin-top:20px;'>
    <h3 style='color:#333'>📂 Project KPIs</h3>
    <div style='background-color:#d9f1ff; padding:15px; border-radius:10px;'>
    <b>Expert Finder</b>: Precision: 0.91 | Recall: 0.89 | F1: 0.90
    </div><br>
    <div style='background-color:#fcebd7; padding:15px; border-radius:10px;'>
    <b>Lead Generator</b>: NPS: 68 | CSAT: 84 | Res Time: 2.8 mins
    </div>
    </div>""", unsafe_allow_html=True)

# --- TAB 2: Company KPIs ---
with tabs[1]:
    st.subheader("🏢 Company KPI Breakdown")

    st.markdown("""<div style='background-color:#f0f0f5; padding:20px; border-radius:15px'>
    <h4 style='color:#333'>📌 Company-Level KPIs</h4>
    <ul><li>Automated Resolution Rate: 87%</li><li>First Contact Resolution: 78%</li><li>Average Handling Time: 3.5 mins</li><li>ROI: 1.6x</li></ul>
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div style='background-color:#eaf5ff; padding:20px; border-radius:15px; margin-top:20px;'>
    <h4>📂 Project KPI Overview</h4>
    <div style='background-color:#d9f1ff; padding:15px; border-radius:10px;'>
    <b>Expert Finder</b>: Precision: 0.91 | Recall: 0.89 | F1-Score: 0.90
    </div><br>
    <div style='background-color:#fcebd7; padding:15px; border-radius:10px;'>
    <b>Lead Generator</b>: Resolution Time: 2.8 mins | NPS: 68 | CSAT: 84
    </div>
    </div>""", unsafe_allow_html=True)

# --- TAB 3: Project KPIs ---
with tabs[2]:
    st.subheader("🚀 Project KPI Breakdown")

    st.markdown("""<div style='background-color:#f0fff0; padding:20px; border-radius:15px'>
    <h4>📌 General Project KPIs</h4>
    <ul><li>Market Penetration Rate: 22%</li><li>Customer Acquisition Cost: $120</li></ul>
    </div>""", unsafe_allow_html=True)

    st.markdown("""<div style='background-color:#f5f5f5; padding:20px; border-radius:15px; margin-top:20px;'>
    <h4>📂 Detailed Project KPIs</h4>
    <div style='background-color:#d9f1ff; padding:15px; border-radius:10px;'>
    <b>Expert Finder</b>: Model Accuracy: 91% | Time to Deploy: 2 weeks
    </div><br>
    <div style='background-color:#fcebd7; padding:15px; border-radius:10px;'>
    <b>Lead Generator</b>: Conversion Rate: 7.2% | Avg Lead Time: 1.4 days
    </div>
    </div>""", unsafe_allow_html=True)
