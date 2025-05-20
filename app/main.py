import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data

# Set wide layout and custom title
st.set_page_config(page_title=" Solar Insights Dashboard by Nurye Nigus", layout="wide")

# Sidebar 
st.sidebar.title(" Control ")

country = st.sidebar.selectbox(" Select Country", ["Benin", "Sierra Leone", "Togo"])
metric = st.sidebar.radio(" Select Metric", ["GHI", "DNI", "DHI"])
top_n = st.sidebar.slider(" Show Top N Values(5-50)", min_value=5, max_value=50, value=10)

# Main Title 
st.title(" Solar Irradiance Analysis Dashboard done by Nurye Nigus")
st.markdown("Explore cleaned solar irradiance data across the three contries given")

# Load Data
df = load_data(country)

if df.empty:
    st.error("No data available.")
    st.stop()

#  Metrics Summary 
st.subheader(f" Summary Statistics for {country}")
st.dataframe(df[[metric]].describe().T)

# Plot & Table Layout for displaying top 10 ghi radings based on side bar
col1, col2 = st.columns([2, 1])

#  Boxplot 
with col1:
    st.subheader(f" Boxplot of {metric}")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.boxplot(y=df[metric], color='mediumseagreen', ax=ax)
    ax.set_ylabel(f"{metric} (W/m²)")
    st.pyplot(fig)

# Top N Table
with col2:
    st.subheader(f" Top {top_n} Highest {metric} Readings")
    st.dataframe(df[[metric]].sort_values(by=metric, ascending=False).head(top_n).reset_index(drop=True))

# Expander for Raw Data Preview
with st.expander(" View Raw Data Sample"):
    st.dataframe(df.head(20))

#  Footer 
st.markdown("---")
st.markdown("Made with by Nurye Nigus | [GitHub](https://github.com/NuryeNigusMekonen)")
