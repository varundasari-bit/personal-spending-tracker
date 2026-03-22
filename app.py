import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

from utils.categorizer import categorize
from utils.anomaly import detect_anomaly
from utils.insights import top_category

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["date","amount","category","desc"])

st.title("💸 Personal Spending Tracker")

amount = st.number_input("Enter amount")
desc = st.text_input("Enter description")

if st.button("Add Expense"):
    if amount > 0 and desc:
        category = categorize(desc)
        new_row = {
            "date": datetime.now(),
            "amount": amount,
            "category": category,
            "desc": desc
        }
        st.session_state.data = pd.concat(
            [st.session_state.data, pd.DataFrame([new_row])],
            ignore_index=True
        )
        st.success(f"Added under {category}")

df = st.session_state.data

if not df.empty:
    df = detect_anomaly(df)

    st.subheader("📊 Data")
    st.write(df)

    st.subheader("📈 Spending by Category")
    category_spend = df.groupby("category")["amount"].sum()

    fig, ax = plt.subplots()
    category_spend.plot(kind="bar", ax=ax)
    st.pyplot(fig)

    st.warning(f"Top spending: {top_category(df)}")
