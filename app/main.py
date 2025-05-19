import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import load_data, plot_ghi_boxplot

st.set_page_config(page_title="Solar Insights Dashboard", layout="wide")
st.title("Solar Potential Comparison Dashboard")

# Sidebar for country selection
country = st.sidebar.selectbox("Select Country", ["Benin", "Sierra Leone", "Togo"])

# Load dataset
df = load_data(country)

# Show basic stats
st.subheader(f"Summary Statistics – {country}")
st.dataframe(df.describe().round(2))

# Show GHI boxplot
st.subheader("GHI Distribution")
fig = plot_ghi_boxplot(df, country)
st.pyplot(fig)
