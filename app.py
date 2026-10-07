from modules.ticket import (
    create_ticket_ui,
    view_tickets_ui,
    update_ticket_status_ui
)
from modules.customer import view_customers_ui
from modules.analytics import analytics_dashboard

import streamlit as st
from db_config import get_connection          # ✅ NEW: central connection
from modules.database_setup import create_database
from modules.generate_data import (
    insert_customers,
    insert_agents,
    insert_tickets
)

# ---------------- Database Setup ----------------
create_database()
# insert_customers()   # Uncomment once to load sample data, then comment again
# insert_agents()
# insert_tickets()

# ---------------- Dashboard Metrics ----------------
# ✅ MySQL: use get_connection() instead of sqlite3.connect()
conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM customers")
total_customers = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM agents")
total_agents = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM tickets")
total_tickets = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM tickets WHERE status='Open'")
open_tickets = cursor.fetchone()[0]

conn.close()

# ---------------- App UI ----------------
st.set_page_config(page_title="Customer Support System", layout="wide")

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Go to",
    [
        "🏠 Dashboard",
        "🎫 Tickets",
        "👥 Customers",
        "📊 Analytics"
    ]
)

st.title("Customer Support System")

# ---------------- Dashboard ----------------
if menu == "🏠 Dashboard":
    st.subheader("Executive Dashboard")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    col1.metric("Total Customers", total_customers)
    col2.metric("Total Agents", total_agents)
    col3.metric("Total Tickets", total_tickets)
    col4.metric("Open Tickets", open_tickets)

# ---------------- Tickets ----------------
elif menu == "🎫 Tickets":
    create_ticket_ui()
    st.divider()
    view_tickets_ui()
    st.divider()
    update_ticket_status_ui()

# ---------------- Customers ----------------
elif menu == "👥 Customers":
    view_customers_ui()

# ---------------- Analytics ----------------
elif menu == "📊 Analytics":
    analytics_dashboard()
