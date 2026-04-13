# 🧠 AI Natural Language to SQL Assistant
---

## 📌 Overview

**AI Natural Language to SQL Assistant** is an intelligent application that allows users to query structured databases using plain English. Instead of writing complex SQL queries manually, users can simply ask questions, and the system automatically generates and executes SQL queries using a Large Language Model (LLM).

The application retrieves the database schema, converts natural language into SQL, validates queries for safety, executes them on a SQLite database, and displays results with optional visualizations.

---

## ✨ Features

* 🗣️ Natural Language → SQL Conversion
* 🧠 LLM-powered query generation
* 🔐 SQL query safety validation
* 📊 Execute queries on SQLite database
* 📈 Automatic data visualization
* ⚡ Simple and interactive UI (Streamlit)

---

## 🧠 Tech Stack

* **Python**
* **Streamlit**
* **OpenAI API (LLM)**
* **SQLite**
* **Pandas**

---

## 🏗️ Architecture

```
User Query (Natural Language)
        ↓
LLM (Generate SQL Query)
        ↓
SQL Validator (Check safety)
        ↓
SQLite Database Execution
        ↓
Results (Pandas DataFrame)
        ↓
Streamlit UI (Table + Charts)
```

---

## 📂 Project Structure

```
ai-sql-assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── database.db
│
├── utils/
│   ├── db.py
│   ├── llm.py
│   └── validator.py
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ai-sql-assistant.git
cd ai-sql-assistant
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Set OpenAI API Key

#### 🔹 Mac/Linux:

```bash
export OPENAI_API_KEY=your_api_key
```

#### 🔹 Windows:

```bash
set OPENAI_API_KEY=your_api_key
```

---

### 4️⃣ Run Application

```bash
streamlit run app.py
```

---

## 💡 Example Queries

* Show total sales by city
* Top 3 customers by revenue
* Average sales per product
* Which product has highest sales?

---

## 📊 Sample Dataset

The project includes a sample **sales database** with fields:

* customer_name
* product
* amount
* city

You can modify or extend this database for testing.

---

## 🔐 Safety Features

* Blocks dangerous SQL queries (DROP, DELETE, UPDATE, etc.)
* Ensures safe execution environment

---

## 🚀 Future Improvements

* 📁 Upload custom CSV as database
* 🔗 Multi-table query support
* 💬 Chat-based interface
* 📊 Advanced visualizations (charts, dashboards)
* 🌐 Deployment (Streamlit Cloud / Render)
* 🧠 Query explanation (NL → SQL reasoning)

---

## 📬 AUTHOR

**JONCY KEDA - AI DEVELOPER**

