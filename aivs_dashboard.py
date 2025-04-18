import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="AIVS KPI Dashboard", layout="wide")

# --- MOCK DATA ---
date_range = pd.date_range(end=datetime.today(), periods=30)
kpi_df = pd.DataFrame({
    "Date": date_range,
    "ROI": np.random.uniform(10, 30, size=30),
    "Model Accuracy": np.random.uniform(70, 95, size=30),
    "Lead Conversion Rate": np.random.uniform(5, 20, size=30),
    "Client Satisfaction": np.random.uniform(60, 100, size=30)
})

project_data = {
    "Expert Finder": pd.DataFrame({
        "Date": date_range,
        "Active Users": np.random.randint(100, 500, size=30),
        "Matching Accuracy": np.random.uniform(70, 95, size=30),
        "Avg Response Time": np.random.uniform(1, 5, size=30),
        "Automated Resolution Rate": np.random.uniform(50, 90, size=30)
    }),
    "Lead Generator": pd.DataFrame({
        "Date": date_range,
        "Leads Captured": np.random.randint(50, 300, size=30),
        "Lead Quality Score": np.random.uniform(60, 100, size=30),
        "Email Open Rate": np.random.uniform(10, 50, size=30),
        "Conversion Rate": np.random.uniform(5, 25, size=30)
    })
}

section_colors = {
    "overview": "#DCFCE7",       # light green
    "project_a": "#E0F2FE",      # light blue
    "project_b": "#E9D5FF",      # light yellow
    "danger_red": "#FECACA",
    "danger_yellow": "#FEF9C3",
    "title_expert": "#38BDF8",   # sky blue
    "title_lead": "#E9D5FF"      # amber
}

def colored_pie_chart(name, value, color_hex, key=None):
    return px.pie(
        names=["Current", "Remaining"],
        values=[value, 100 - value],
        color_discrete_sequence=[color_hex, "#E5E7EB"]
    )

# --- APP HEADER ---
st.title("📊 AI Venture Studio KPI Dashboard")
tabs = st.tabs(["Overview", "Projects"])

# --- OVERVIEW TAB ---
with tabs[0]:
    st.markdown(
        """<div style='background-color:#F3F4F6; padding:10px; border-radius:12px; margin-bottom: 15px'>
        <h3 style='color:#1F2937;'>📈 Company-Wide Overview</h3>
        </div>""",
        unsafe_allow_html=True
    )

    timeline = st.slider("Select Time Range:", min_value=kpi_df["Date"].min().date(), max_value=kpi_df["Date"].max().date(), value=(kpi_df["Date"].min().date(), kpi_df["Date"].max().date()), key="timeline_slider")
    filtered_df = kpi_df[(kpi_df["Date"].dt.date >= timeline[0]) & (kpi_df["Date"].dt.date <= timeline[1])]

    overview_cols = st.columns(4)
    kpi_list = [
        ("💰 ROI", "Return on investment from AI initiatives."),
        ("🎯 Model Accuracy", "Overall accuracy across deployed ML models."),
        ("🔄 Lead Conversion Rate", "Rate of converting generated leads into clients."),
        ("😊 Client Satisfaction", "Average client rating from feedback surveys.")
    ]

    for i, (kpi_name, description) in enumerate(kpi_list):
        column_name = kpi_name.split(" ", 1)[1]
        with overview_cols[i]:
            st.subheader(kpi_name)
            chart = colored_pie_chart(column_name, filtered_df[column_name].iloc[-1], section_colors["overview"], key=f"overview_{column_name}")
            st.plotly_chart(chart, use_container_width=True)
            st.markdown(f"*{description}*")

    st.markdown("### 📈 KPI Trends Over Time")
    fig_line = px.line(filtered_df, x="Date", y=[k.split(" ", 1)[1] for k, _ in kpi_list], markers=True)
    fig_line.update_layout(legend_title_text='KPIs')
    st.plotly_chart(fig_line, use_container_width=True)

    st.markdown("---")
    st.markdown(
        """<div style='background-color:#F87171; padding:10px; border-radius:12px; margin-bottom: 15px'>
        <h4 style='color:white;'>🚨 Danger Zone</h4>
        </div>""",
        unsafe_allow_html=True
    )

    danger_cols = st.columns(3)
    mock_kpis = {
        "❌ Critical AI Failures": 65,
        "📉 Low Engagement Rate": 45,
        "🌪️ Model Drift Frequency": 30
    }

    for i, (label, value) in enumerate(mock_kpis.items()):
        with danger_cols[i]:
            st.markdown(f"**{label}**")
            color = section_colors["danger_red"] if "❌" in label else section_colors["danger_yellow"]
            fig = colored_pie_chart(label, value, color, key=f"danger_{i}")
            st.plotly_chart(fig, use_container_width=True)
            recommendation = {
                0: "🔴 Urgent: Increase AI system monitoring & failover mechanisms.",
                1: "🟡 Consider improving UX through personalized user flows.",
                2: "🟡 Retrain using more diverse and up-to-date datasets."
            }
            st.markdown(recommendation[i])

    st.markdown("### 📚 Recommendations to Improve AIVS KPIs")
    st.markdown("**1. Implement Active Learning Pipelines**")
    st.markdown("- According to *Settles (2010)*, incorporating user feedback into the retraining cycle significantly boosts model relevance and performance.")
    st.markdown("**2. Personalize AI Interfaces via Behavioral Data**")
    st.markdown("- Studies (*Cai et al., 2019*) show personalized AI systems improve user trust and engagement, leading to higher retention rates.")

# --- PROJECTS TAB ---
with tabs[1]:
    st.header("🧩 Project KPIs")

    for i, (project_name, df_project) in enumerate(project_data.items()):
        theme_color = section_colors["title_expert"] if "Expert" in project_name else section_colors["title_lead"]
        section_color = section_colors["project_a"] if i == 0 else section_colors["project_b"]

        st.markdown(
            f"""<div style='background-color:{theme_color}; padding:10px; border-radius:12px'>
            <h4 style='color:#1F2937;'>📌 {project_name}</h4>
            </div>""",
            unsafe_allow_html=True
        )

        # If the project is "Expert Finder", adjust the Active Users data
        if "Expert Finder" in project_name:
            df_project["Active Users"] = np.clip(df_project["Active Users"] / 5, 0, 100)  # Normalize data

        project_cols = st.columns(4)
        icon_map = {
            "Active Users": "👥",
            "Matching Accuracy": "🤝",
            "Avg Response Time": "⏱️",
            "Automated Resolution Rate": "🤖",
            "Leads Captured": "📥",
            "Lead Quality Score": "📊",
            "Email Open Rate": "✉️",
            "Conversion Rate": "💼"
        }

        for j, col in enumerate(df_project.columns[1:]):
            with project_cols[j]:
                icon_label = f"{icon_map.get(col, '')} {col}"
                st.markdown(f"**{icon_label}**")
                fig = colored_pie_chart(col, df_project[col].iloc[-1], section_color, key=f"{project_name}_{col}")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown(f"*Latest data for {col.lower()}*")

        st.markdown("**📊 Timeline View**")
        fig_proj = px.line(df_project, x="Date", y=df_project.columns[1:], markers=True)
        fig_proj.update_layout(legend_title_text='KPIs')
        st.plotly_chart(fig_proj, use_container_width=True)

        # Project-specific Danger Zone
        st.markdown(
            f"""<div style='background-color:#F87171; padding:10px; border-radius:12px; margin-top: 25px; margin-bottom: 10px'>
            <h5 style='color:white;'>🚨 {project_name} Danger Zone</h5>
            </div>""",
            unsafe_allow_html=True
        )

        dz_cols = st.columns(2)

        if "Expert" in project_name:
            dz_data = {
                "📉 Low Matching Accuracy": 40,
                "❌ High Response Time": 70
            }
            dz_recs = [
                "🟡 Improve training data by adding more expert-user mappings.",
                "🔴 Optimize backend latency and routing logic for real-time answers."
            ]
        else:
            dz_data = {
                "📉 Low Lead Quality Score": 50,
                "❌ Low Conversion Rate": 20
            }
            dz_recs = [
                "🟡 Segment your leads and customize outreach.",
                "🔴 Run A/B tests on CTA placements and email language."
            ]

        for idx, (kpi_label, value) in enumerate(dz_data.items()):
            with dz_cols[idx]:
                color = section_colors["danger_red"] if "❌" in kpi_label else section_colors["danger_yellow"]
                fig = colored_pie_chart(kpi_label, value, color, key=f"{project_name}_dz_{idx}")
                st.markdown(f"**{kpi_label}**")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown(dz_recs[idx])

        st.markdown("---")
