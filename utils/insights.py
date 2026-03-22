def top_category(df):
    return df.groupby("category")["amount"].sum().idxmax()
