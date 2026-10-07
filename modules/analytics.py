import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from db_config import get_connection


def analytics_dashboard():
    st.subheader("Analytics Dashboard")

    # ✅ MySQL: use get_connection() instead of sqlite3.connect()
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM tickets", conn)
    conn.close()

    # ---------------- Export CSV ----------------
    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="Export Tickets to CSV",
        data=csv,
        file_name="tickets_export.csv",
        mime="text/csv"
    )

    st.divider()

    # ---------------- Two Column Layout ----------------
    col1, col2 = st.columns(2)

    # -------- Chart 1: Status --------
    with col1:
        st.write("Tickets by Status")
        status_counts = df["status"].value_counts()

        fig1, ax1 = plt.subplots(figsize=(4, 3))
        ax1.bar(status_counts.index, status_counts.values)
        plt.xticks(rotation=30)
        st.pyplot(fig1)

    # -------- Chart 2: Priority --------
    with col2:
        st.write("Tickets by Priority")
        priority_counts = df["priority"].value_counts()

        fig2, ax2 = plt.subplots(figsize=(4, 3))
        ax2.bar(priority_counts.index, priority_counts.values)
        plt.xticks(rotation=30)
        st.pyplot(fig2)

    st.divider()

    # -------- Chart 3: Issue Types --------
    st.write("Top 5 Issue Types")
    issue_counts = df["issue_type"].value_counts().head(5)

    fig3, ax3 = plt.subplots(figsize=(8, 3.5))
    ax3.bar(issue_counts.index, issue_counts.values)
    plt.xticks(rotation=30)
    st.pyplot(fig3)
