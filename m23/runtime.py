import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import requests
import os

# -----------------------------
# Safe CSV save
# -----------------------------
def save_csv(df, path):
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(path), exist_ok=True)
        df.to_csv(path, index=False)
        print(f"[INFO] Saved CSV to {path}")
    except Exception as e:
        print(f"[ERROR] Failed to save CSV: {e}")

# -----------------------------
# Plot bar / line chart
# -----------------------------
def plot(df, x, y, chart_type="line", title=None):
    try:
        if chart_type.lower() == "line":
            df.plot(x=x, y=y, kind="line", title=title)
        elif chart_type.lower() == "bar":
            df.plot(x=x, y=y, kind="bar", title=title)
        else:
            print(f"[WARN] Unknown chart type '{chart_type}', defaulting to line")
            df.plot(x=x, y=y, kind="line", title=title)
        plt.show()
    except Exception as e:
        print(f"[ERROR] Plot failed: {e}")

# -----------------------------
# Fetch JSON API safely
# -----------------------------
def fetch_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status
        data = response.json()
        # If API returns a dict with nested data, try to convert to list of dicts
        if isinstance(data, dict):
            data = [data]
        return data
    except Exception as e:
        print(f"[ERROR] Failed to fetch API data: {e}")
        return []

# -----------------------------
# Example helper: train LinearRegression
# -----------------------------
def train_linear_regression(X, y):
    try:
        model = LinearRegression()
        model.fit(X.values.reshape(-1,1), y.values)
        print("[INFO] Trained LinearRegression model")
        return model
    except Exception as e:
        print(f"[ERROR] Model training failed: {e}")
        return None
