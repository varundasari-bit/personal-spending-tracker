def detect_anomaly(df):
    mean = df["amount"].mean()
    std = df["amount"].std()
    df["anomaly"] = df["amount"] > (mean + 2 * std)
    return df
