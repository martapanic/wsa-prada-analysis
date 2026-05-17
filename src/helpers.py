import pandas as pd
import numpy as np
from datetime import datetime, timezone


def utc_to_datetime(utc_ts):
    """Convert Reddit UTC timestamp to datetime."""
    if pd.isna(utc_ts):
        return None
    return datetime.fromtimestamp(utc_ts, tz=timezone.utc)


def clean_deleted_authors(df, author_col="author"):
    """Remove deleted or missing authors."""
    return df[
        df[author_col].notna() &
        (df[author_col] != "[deleted]") &
        (df[author_col] != "AutoModerator")
    ].copy()


def basic_text_cleaning(text):
    """Basic cleaning for Reddit comments."""
    if pd.isna(text):
        return ""
    text = str(text)
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = " ".join(text.split())
    return text