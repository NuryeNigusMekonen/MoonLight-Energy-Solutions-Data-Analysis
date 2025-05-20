import os
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
        st.warning(f" File not found: {filename}")
        return pd.DataFrame()
