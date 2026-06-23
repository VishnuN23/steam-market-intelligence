# Steam Market Intelligence Dashboard

## Project Overview
This project analyzes Steam game market data using an ETL pipeline built with Python, MySQL, and Streamlit.

## Technologies Used
- Python
- Pandas
- MySQL
- SQLAlchemy
- Streamlit
- Git & GitHub

## ETL Pipeline

### Extract
- Read Steam game dataset from CSV

### Transform
- Cleaned missing values
- Removed duplicates
- Standardized columns

### Load
- Loaded cleaned data into MySQL database

### Visualize
- Built interactive dashboard using Streamlit

## Dashboard Features
- Publisher filter
- Free vs Paid Games analysis
- Top Publishers chart
- Top Developers chart
- Price Distribution
- Most Expensive Games table

## Project Structure

```text
steam_market_intelligence/
│
├── dashboard/
│   └── app.py
│
├── etl/
│   ├── explore_data.py
│   ├── clean_data.py
│   └── load_to_mysql.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── sql/
├── requirements.txt
└── README.md
```

## Author
Vishnu Nanda kumar
