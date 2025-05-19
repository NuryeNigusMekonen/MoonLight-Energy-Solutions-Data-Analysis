import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def load_data(country):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "..", "cleaned_data")

    filename_map = {
        "Benin": "benin_cleaned_data.csv",
        "Sierra Leone": "sierraleone_cleaned_data.csv",
        "Togo": "togo_cleaned_data.csv"
    }

    filename = filename_map.get(country)
    if filename is None:
        st.warning(f"No data file defined for country: {country}")
        return pd.DataFrame()

    filepath = os.path.join(data_dir, filename)

    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        st.warning(f"Data file not found at {filepath}. "
                   "If running locally, please ensure the file exists. "
                   "If deployed without data, this is expected.")
        return pd.DataFrame()

def plot_ghi_boxplot(df, country):
    if df.empty or 'GHI' not in df.columns:
        st.warning("Dataframe is empty or missing 'GHI' column — cannot plot boxplot.")
        return None
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(y=df['GHI'], color='skyblue', ax=ax)
    ax.set_title(f"GHI Boxplot – {country}")
    ax.set_ylabel("GHI (W/m²)")
    return fig
