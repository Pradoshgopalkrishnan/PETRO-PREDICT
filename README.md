# Petro Predict – Fuel Price Prediction System

A robust AI-powered fuel price analytics and forecasting toolkit built in **Python**, **Tkinter**, and **MySQL**. Petro Predict leverages linear regression and historical datasets to provide future price predictions and insights for petrol, diesel, and speed petrol fuels.

---

## 📖 Table of Contents
- Features
- Tech Stack
- Setup & Usage
- Database & Data Import
- Output
- File Structure
- Security Guidelines
- References

---

## ✨ Features

- **AI Predictions:** Use machine learning to forecast petrol, diesel, and speed petrol prices based on historical and market data.
- **Interactive GUI:** Tkinter dashboard for running predictions, adding/training data, and viewing visual analytics.
- **Database Integration:** Fast MySQL storage and retrieval for fuel volumes, prices, and user actions.
- **Graphical Analysis:** Built-in cost/volume graphs, yearly trend visualization, and insights.
- **Secure Credentials:** Sensitive info managed through `.env` files only; never uploaded.

---

## 🛠️ Tech Stack

- Python 3.x
- Tkinter (GUI)
- MySQL
- mysql-connector-python
- python-dotenv
- pandas, matplotlib, scikit-learn

---

## 🚀 Setup & Usage

1. **Clone the Repository**
    ```
    git clone <your_repository_url>
    cd petro-predict
    ```

2. **Install Dependencies**
    ```
    pip install mysql-connector-python python-dotenv pandas matplotlib scikit-learn
    ```

3. **Set up the MySQL Database**
    - Start your MySQL service.
    - Import the provided database schema:
      ```
      mysql -u your_mysql_user -p < PETROPREDICT.sql
      ```
    - Tables created include:
      - `petrol`, `diesel`, `speed` (fuel volumes and cost)
      - `pet`, `dies`, `speed_p` (annual rate)
      - `petrol_prices` (date, price, type)
      - `yearly` (yearly fuel summary)
      - `entries` (login records)

4. **Configure Environment Variables**
    - Create a `.env` file (do **not** upload or share this file):
      ```
      DB_HOST=localhost
      DB_USER=your_mysql_user
      DB_PASS=your_mysql_password
      DB_NAME=petro_predict
      ```
    - Ensure `.env` is in `.gitignore` (never version it).

---

## 📊 Database & Data Import

- Place CSV files (e.g., `petrol price.csv`, `diesel price.csv`, `speed petrol.csv`, `pet.csv`, `dies.csv`, `speed_p.csv`, `petrol price.csv`, `yearly.csv`) in your project folder.
- Import data to respective tables using MySQL commands:

    ```
    LOAD DATA INFILE '/absolute/path/petrol price.csv'
    INTO TABLE petrol
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES;
    ```

- Or with pandas in Python:

    ```
    import pandas as pd
    import mysql.connector

    df = pd.read_csv('petrol price.csv')
    conn = mysql.connector.connect(
        host='localhost', user='your_user', password='your_password', database='petro_predict'
    )
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute('INSERT INTO petrol (volume, cost) VALUES (%s, %s)', (row['volume'], row['cost']))
    conn.commit()
    ```

- Repeat import for all tables based on their schema and relevant CSV.

---

## 📷 Output

- Fuel price predictions by volume/cost/year.
- GUI confirmation dialogs of successful data insertions.
- Graphs representing volume, cost, and other analytics.
- Secure login window for database connection and entry logging.

---

## 🗂️ File Structure

petro-predict/  
├── .env # Private (not tracked)  
├── PETROPREDICT.sql # Database schema  
├── Source-code-mysql.py # Main backend/GUI code  
├── *.csv # Data files for table population  
└── README.md # Project info (this file)

---

## 🔒 Security Guidelines

- Always keep `.env` and passwords private; never upload or share.
- Provide only `.env.example` with placeholder variables for others.
- Ensure sensitive credentials are excluded from source control and any public upload.

---

## 📚 References

- Official Python, Tkinter, MySQL documentation
- Online textbooks and tutorials for machine learning and database setup
