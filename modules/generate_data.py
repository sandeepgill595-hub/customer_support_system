import random
from db_config import get_connection

first_names = [
    "Rahul", "Aman", "Priya", "Neha", "Rohan", "Simran", "Arjun", "Sneha",
    "Vikas", "Pooja", "Ankit", "Nisha", "Karan", "Meera", "Aditya", "Riya",
    "Sanjay", "Kavya", "Mohit", "Divya"
]

last_names = [
    "Sharma", "Singh", "Gupta", "Verma", "Mehta", "Kapoor", "Jain", "Yadav",
    "Mishra", "Agarwal", "Bansal", "Chopra", "Malhotra", "Saxena", "Arora"
]

cities = [
    "Delhi", "Mumbai", "Bangalore", "Hyderabad", "Pune",
    "Chennai", "Kolkata", "Ahmedabad", "Jaipur", "Lucknow",
    "Noida", "Gurgaon", "Indore", "Bhopal", "Patna",
    "Chandigarh", "Nagpur", "Surat", "Kanpur", "Ghaziabad"
]

departments = ["Technical", "Billing", "Refund", "Customer Care"]

issue_types = [
    "Payment Failure", "Login Issue", "Refund Request", "Delivery Delay",
    "Technical Bug", "Password Reset", "Account Locked",
    "Subscription Issue", "Invoice Request", "App Crash"
]

priorities = ["Low", "Medium", "High", "Critical"]
statuses = ["Open", "In Progress", "Resolved", "Closed"]


def insert_customers():
    conn = get_connection()
    cursor = conn.cursor()

    for i in range(1, 501):
        customer_id = f"C{i:03d}"
        name = random.choice(first_names) + " " + random.choice(last_names)
        email = name.lower().replace(" ", "") + "@gmail.com"
        phone = str(random.randint(9000000000, 9999999999))
        city = random.choice(cities)

        # ✅ MySQL uses %s instead of ? and INSERT IGNORE instead of INSERT OR IGNORE
        cursor.execute("""
            INSERT IGNORE INTO customers
            VALUES (%s, %s, %s, %s, %s)
        """, (customer_id, name, email, phone, city))

    conn.commit()
    conn.close()
    print("✅ Customers inserted!")


def insert_agents():
    conn = get_connection()
    cursor = conn.cursor()

    for i in range(1, 16):
        agent_id = f"A{i:02d}"
        name = f"Agent_{i}"
        department = random.choice(departments)

        cursor.execute("""
            INSERT IGNORE INTO agents
            VALUES (%s, %s, %s)
        """, (agent_id, name, department))

    conn.commit()
    conn.close()
    print("✅ Agents inserted!")


def insert_tickets():
    conn = get_connection()
    cursor = conn.cursor()

    for i in range(1, 5001):
        ticket_id = f"T{i:04d}"
        customer_id = f"C{random.randint(1, 500):03d}"
        issue_type = random.choice(issue_types)
        priority = random.choice(priorities)
        status = random.choice(statuses)
        assigned_agent = f"A{random.randint(1, 15):02d}"
        issue_description = f"Sample issue related to {issue_type}"
        sentiment = "Neutral"

        cursor.execute("""
            INSERT IGNORE INTO tickets
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            ticket_id, customer_id, issue_type, priority,
            issue_description, sentiment, status, assigned_agent
        ))

    conn.commit()
    conn.close()
    print("✅ Tickets inserted!")
