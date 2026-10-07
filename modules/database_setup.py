import mysql.connector
from db_config import get_connection


def create_mysql_database():
    # Step 1: Connect WITHOUT selecting a database (to create it first)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dsggsg@123"  # ✅ Same password as in db_config.py
    )
    cursor = conn.cursor()

    # Create the database if it does not exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS customer_support_db")
    conn.commit()
    cursor.close()
    conn.close()


def create_database():
    # Step 1: Make sure the database exists
    create_mysql_database()

    # Step 2: Now connect to it and create tables
    conn = get_connection()
    cursor = conn.cursor()

    # Customers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id VARCHAR(20) PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        phone VARCHAR(20),
        city VARCHAR(50)
    )
    """)

    # Agents table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agents (
        agent_id VARCHAR(20) PRIMARY KEY,
        name VARCHAR(100),
        department VARCHAR(50)
    )
    """)

    # Tickets table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        ticket_id VARCHAR(20) PRIMARY KEY,
        customer_id VARCHAR(20),
        issue_type VARCHAR(100),
        priority VARCHAR(20),
        issue_description TEXT,
        sentiment VARCHAR(20),
        status VARCHAR(30),
        assigned_agent VARCHAR(20)
    )
    """)

    conn.commit()
    conn.close()
    print("✅ MySQL Database and Tables created successfully!")
