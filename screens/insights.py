import streamlit as st
import plotly.express as px
import pandas as pd

def render():
    st.header("Mood Insights")

    data = {
        "Day": ["Day 1", "Day 2", "Day 3", "Day 4"],
        "Mood Level": [2, 3, 1, 4],
    }

    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x="Day",
        y="Mood Level",
        title="Recent Mood Reflection",
    )

    st.plotly_chart(fig, use_container_width=True)

    st.caption("This is a reflection tool, not a diagnosis.")

    st.button("Clear my data")
