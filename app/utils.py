import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(country):
    filename = {
        "Benin": "../cleaned_data/benin_cleaned.csv",
        "Sierra Leone": "../cleaned_data/sierraleone_cleaned_data.csv",
        "Togo": "../cleaned_data/togo_cleaned_data.csv"
    }.get(country)
    
    return pd.read_csv(filename)

def plot_ghi_boxplot(df, country):
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(y=df['GHI'], color='skyblue', ax=ax)
    ax.set_title(f"GHI Boxplot – {country}")
    ax.set_ylabel("GHI (W/m²)")
    return fig
