import streamlit as st
from db_config import get_connection


def view_customers_ui():
    st.subheader("Customer Management")

    # ✅ MySQL: use get_connection() instead of sqlite3.connect()
    conn = get_connection()
    cursor = conn.cursor()

    # ---------- Add Customer ----------
    st.write("Add New Customer")

    new_name = st.text_input("Customer Name")
    new_email = st.text_input("Email")
    new_city = st.text_input("City")

    if st.button("Add Customer"):
        # ✅ MySQL: %s instead of ?
        cursor.execute("""
            INSERT INTO customers (name, email, city)
            VALUES (%s, %s, %s)
        """, (new_name, new_email, new_city))
        conn.commit()
        st.success("Customer added successfully!")

    # ---------- Search Customer ----------
    st.write("---")
    search_name = st.text_input("Search Customer by Name")

    if search_name:
        # ✅ MySQL: %s instead of ?
        cursor.execute("""
            SELECT customer_id, name, city
            FROM customers
            WHERE name LIKE %s
        """, ('%' + search_name + '%',))
    else:
        cursor.execute("""
            SELECT customer_id, name, city
            FROM customers
            LIMIT 10
        """)

    customers = cursor.fetchall()
    st.write("Customer List")
    st.table(customers)

    # ---------- Customer Ticket History ----------
    st.write("---")
    st.subheader("Customer Ticket History")

    history_customer_id = st.text_input("Enter Customer ID to View Tickets")

    if st.button("View Ticket History"):
        # ✅ MySQL: %s instead of ?
        cursor.execute("""
            SELECT ticket_id, issue_type, priority, status, assigned_agent
            FROM tickets
            WHERE customer_id = %s
        """, (history_customer_id,))

        ticket_history = cursor.fetchall()

        if ticket_history:
            st.table(ticket_history)
        else:
            st.warning("No tickets found for this customer.")

    conn.close()
