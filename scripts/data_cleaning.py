# scripts/data_cleaning.py

import numpy as np
import pandas as pd
from scipy import stats

def clean_mod_columns(df):
    """Replace 0s in ModA/ModB with NaN, then fill with median."""
    mod_cols = ['ModA', 'ModB']
    df[mod_cols] = df[mod_cols].mask(df[mod_cols] == 0, np.nan)
    df[mod_cols] = df[mod_cols].fillna(df[mod_cols].median())
    return df

def remove_outliers(df, cols, z_thresh=3):
    """Remove rows where Z-score > threshold in any of the given columns."""
    z_scores = np.abs(stats.zscore(df[cols], nan_policy='omit'))
    return df[(z_scores < z_thresh).all(axis=1)]
