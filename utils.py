import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def load_data(country):
    filename = {
        "Benin": "cleaned_data/benin_cleaned_data.csv",
        "Sierra Leone": "cleaned_data/sierraleone_cleaned_data.csv",
        "Togo": "cleaned_data/togo_cleaned_data.csv"
    }.get(country)

    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        st.warning(f"Data file not found: {filename}")
        return pd.DataFrame()


def plot_ghi_boxplot(df, country):
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(y=df['GHI'], color='skyblue', ax=ax)
    ax.set_title(f"GHI Boxplot – {country}")
    ax.set_ylabel("GHI (W/m²)")
    return fig
