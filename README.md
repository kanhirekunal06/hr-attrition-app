# 📊 HR Attrition Analytics & Prediction Dashboard

An end-to-end Machine Learning web application designed to analyze employee data, track key performance indicators (KPIs), and predict employee turnover (attrition) risk in real-time. This solution empowers HR professionals to make data-driven decisions and implement proactive retention strategies.

🚀 **[Live Demo Link](https://hr-attrition-app-hlah7mc5mh6cj3tsnsckw8.streamlit.app/)**

---

## 🌟 Key Features

- **Real-Time Data Pipeline:** Integrated with **Snowflake Data Cloud** to securely extract and process live tenant and workforce data.
- **Predictive Analytics:** Features a custom-trained **Machine Learning Model** that evaluates multiple workforce features (e.g., department, business travel, tenure) to predict attrition risk (Yes/No).
- **Interactive UI Dashboard:** Built using **Streamlit** to offer dynamic filtering by department, clear visualizations of attrition rates, and individual employee scoring.
- **Business Insights:** Highlights major churn indicators to help management take actionable steps before critical talent departs.

---

## 🛠️ Tech Stack & Architecture

- **Frontend & App Interface:** Streamlit (Python UI Framework)
- **Data Warehousing & Querying:** Snowflake (Cloud Data Platform)
- **Machine Learning & Processing:** Scikit-Learn, Pandas, NumPy
- **Deployment & Security:** Streamlit Community Cloud (hosted with encrypted environment secrets)
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
hr-attrition-app/
│
├── app.py                  # Main Streamlit dashboard application
├── requirements.txt        # Required python packages for cloud environment
├── models/
│   └── attrition_model.pkl # Pre-trained ML model binaries
├── src/
│   └── data_loader.py      # Script to handle Snowflake database connections
└── README.md               # Project documentation (This file)
```

---

## ⚙️ Local Setup Instructions

To run this application locally on your machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd hr-attrition-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure local environment secrets:**
   Create a `.env` or Streamlit `.streamlit/secrets.toml` file containing your database credentials:
   ```toml
   SNOWFLAKE_USER = "your_user"
   SNOWFLAKE_PASSWORD = "your_password"
   SNOWFLAKE_ACCOUNT = "your_account"
   SNOWFLAKE_WAREHOUSE = "your_warehouse"
   SNOWFLAKE_DATABASE = "your_database"
   SNOWFLAKE_SCHEMA = "your_schema"
   ```

4. **Launch the Streamlit App:**
   ```bash
   streamlit run app.py
   ```
