<div align="center">

# 🎧 AI Customer Support Management System

**Manage customers and support tickets, analyse customer sentiment with AI, and track support performance, all in one app.**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?logo=mysql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black)

[Live Demo](#-live-demo) · [Features](#-features) · [Getting Started](#️-getting-started) · [Project Structure](#-project-structure)

</div>

---

## 📌 Overview

Support teams handle hundreds of tickets, and the unhappy customers are easy to miss. This project gives a support team one place to:

- keep customer and ticket records in a MySQL database,
- automatically score the **sentiment** of each ticket so frustrated customers can be prioritised,
- see ticket volume, status, and trends on an **analytics dashboard**,
- explore the same data in a **Power BI report**.

I built it to practise an end-to-end data workflow: database design → Python application → AI/NLP → analytics and reporting.

## 🖼️ Screenshots

<!-- Replace these with your own screenshots. Save images in a "screenshots" folder. -->
| Dashboard | Ticket Management |
|-----------|-------------------|
| ![Dashboard](screenshots/dashboard.png) | ![Tickets](screenshots/tickets.png) |

## 🚀 Live Demo

<!-- Add your Streamlit link after deploying, e.g. https://your-app-name.streamlit.app -->
🔗 **Coming soon**

## ✨ Features

| Feature | Description |
|---------|-------------|
| 👥 **Customer management** | Add and view customer records |
| 🎫 **Ticket management** | Create, update, and track support tickets through their lifecycle |
| 🤖 **AI sentiment analysis** | Classifies ticket text as positive, neutral, or negative to flag unhappy customers |
| 📊 **Analytics dashboard** | Ticket volume, status breakdown, and trends at a glance |
| 🧪 **Sample data generator** | Fills the database with realistic test data in one command |
| 📈 **Power BI report** | A business-intelligence dashboard built on the MySQL data |

## 🛠️ Tech Stack

| Area | Tools |
|------|-------|
| Language | Python 3 |
| App / UI | Streamlit |
| Database | MySQL (migrated from SQLite) |
| AI / NLP | Sentiment analysis (`ai/sentiment_model.py`) |
| BI & Reporting | Power BI, DAX |

## 🧩 How It Works

```
Customer / Ticket data ──► MySQL database ──► Python modules ──► Streamlit app
                                  │                  │
                                  │                  └──► Sentiment model scores each ticket
                                  │
                                  └──► Power BI report (connected to MySQL)
```

1. **`database_setup.py`** creates the tables in MySQL.
2. **`generate_data.py`** fills them with sample customers and tickets.
3. **`customer.py`** and **`ticket.py`** handle the create, read, and update operations.
4. **`sentiment_model.py`** scores the text of each ticket.
5. **`analytics.py`** and **`dashboard.py`** turn the data into metrics and charts shown in the app.

## 📁 Project Structure

```
customer_support_system/
├── app.py                    # Main Streamlit application
├── db_config.example.py      # Template for database settings
├── requirements.txt          # Python dependencies
├── ai/
│   └── sentiment_model.py    # Sentiment analysis
├── modules/
│   ├── analytics.py          # Metrics and reports
│   ├── customer.py           # Customer operations
│   ├── dashboard.py          # Dashboard views
│   ├── database_setup.py     # Creates database tables
│   ├── generate_data.py      # Generates sample data
│   └── ticket.py             # Ticket operations
├── Power BI/                 # Power BI dashboard (.pbix)
└── Customer_Support_System_Report.docx   # Full project report
```

## ⚙️ Getting Started

### Prerequisites

- Python 3.10 or newer
- MySQL Server, installed and running
- Git

### 1. Clone the repository

```bash
git clone https://github.com/sandeepgill595-hub/customer_support_system.git
cd customer_support_system
```

### 2. Create and activate a virtual environment

**Windows (PowerShell)**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

Copy the example config and add your own MySQL details:

```bash
# Windows
copy db_config.example.py db_config.py

# macOS / Linux
cp db_config.example.py db_config.py
```

Then edit `db_config.py`:

```python
DB_HOST = "localhost"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "customer_support"
```

> 🔒 `db_config.py` is listed in `.gitignore`, so your credentials are never uploaded to GitHub.

### 5. Create the tables and load sample data

```bash
python modules/database_setup.py
python modules/generate_data.py
```

### 6. Run the app

```bash
streamlit run app.py
```

The app opens at **http://localhost:8501**.

## 📈 Power BI Dashboard

1. Open the `.pbix` file in the `Power BI/` folder with **Power BI Desktop**.
2. Go to **Transform data → Data source settings**.
3. Point the source to your own MySQL server and database, then refresh.

## ☁️ Deployment

The app can be deployed on **Streamlit Community Cloud**. Because the cloud server cannot reach `localhost`, it needs a MySQL database hosted online. Add the database credentials in the app's **Secrets** settings instead of committing them:

```toml
DB_HOST = "your-host.example.com"
DB_PORT = 3306
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "customer_support"
```

## 🩺 Troubleshooting

| Problem | Fix |
|---------|-----|
| `Access denied for user` | Check the username and password in `db_config.py` |
| `Can't connect to MySQL server` | Make sure MySQL is running and the host and port are correct |
| `ModuleNotFoundError` | Activate the virtual environment and run `pip install -r requirements.txt` |
| PowerShell blocks `Activate.ps1` | Run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` once |

## 🔮 Future Improvements

- [ ] User login with agent and manager roles
- [ ] Email alerts for high-priority or negative-sentiment tickets
- [ ] Automatic ticket categorisation
- [ ] Docker setup for one-command installation

## 👤 Author

**Sandeep**
Data analyst | Python · SQL · Power BI · Streamlit
GitHub: [@sandeepgill595-hub](https://github.com/sandeepgill595-hub)

---

<div align="center">
⭐ If you found this project useful, consider giving it a star.
</div>
