import streamlit as st
from ai.sentiment_model import predict_sentiment
from db_config import get_connection


def assign_agent(issue_type):
    issue_department_map = {
        "Payment Failure": "Billing",
        "Invoice Request": "Billing",
        "Refund Request": "Refund",
        "Subscription Issue": "Refund",
        "Technical Bug": "Technical",
        "App Crash": "Technical",
        "Login Issue": "Customer Care",
        "Password Reset": "Customer Care",
        "Account Locked": "Customer Care",
        "Delivery Delay": "Customer Care"
    }

    department = issue_department_map.get(issue_type, "Customer Care")

    conn = get_connection()
    cursor = conn.cursor()

    # ✅ MySQL: %s instead of ?
    cursor.execute("""
        SELECT agent_id
        FROM agents
        WHERE department = %s
        LIMIT 1
    """, (department,))

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return "A01"


def create_ticket_ui():
    st.subheader("Create New Ticket")

    customer_id = st.text_input("Customer ID")
    issue_type = st.selectbox(
        "Issue Type",
        [
            "Payment Failure", "Login Issue", "Refund Request",
            "Delivery Delay", "Technical Bug", "Password Reset",
            "Account Locked", "Subscription Issue", "Invoice Request", "App Crash"
        ]
    )

    priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
    issue_description = st.text_area("Describe the Issue")

    if st.button("Create Ticket"):
        sentiment = predict_sentiment(issue_description)
        st.write("Predicted Sentiment:", sentiment)

        conn = get_connection()
        cursor = conn.cursor()

        # ✅ MySQL: %s instead of ?
        cursor.execute("SELECT COUNT(*) FROM tickets")
        total_tickets = cursor.fetchone()[0]

        new_ticket_id = f"T{total_tickets + 1:04d}"
        assigned_agent = assign_agent(issue_type)
        status = "Open"

        cursor.execute("""
            INSERT INTO tickets
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            new_ticket_id, customer_id, issue_type, priority,
            issue_description, sentiment, status, assigned_agent
        ))

        conn.commit()
        conn.close()

        st.info(f"AI Sentiment Analysis: {sentiment}")
        st.success(f"Ticket {new_ticket_id} created successfully!")


def view_tickets_ui():
    st.subheader("Recent Tickets")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tickets
        ORDER BY ticket_id DESC
        LIMIT 10
    """)

    tickets = cursor.fetchall()
    conn.close()

    st.table(tickets)


def update_ticket_status_ui():
    st.subheader("Update Ticket Status")

    ticket_id = st.text_input("Enter Ticket ID")

    new_status = st.selectbox(
        "Select New Status",
        ["Open", "In Progress", "Resolved", "Closed"]
    )

    if st.button("Update Status"):
        conn = get_connection()
        cursor = conn.cursor()

        # ✅ MySQL: %s instead of ?
        cursor.execute("""
            UPDATE tickets
            SET status = %s
            WHERE ticket_id = %s
        """, (new_status, ticket_id))

        conn.commit()
        conn.close()

        st.success(f"Ticket {ticket_id} updated to {new_status}")
