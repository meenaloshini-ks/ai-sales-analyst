# AI Data Analyst – Sales Analytics Dashboard

An AI-powered sales analytics application that cleans retail data, calculates business KPIs, and answers natural-language business questions using Google Gemini.

## Features

- Loads and cleans retail sales data
- Removes missing values and duplicate records
- Calculates total revenue, total orders, and average order value
- Identifies the best-performing state, category, product, and month
- Provides an interactive Streamlit dashboard
- Generates AI-powered business insights using Google Gemini
- Creates sales visualizations using Matplotlib

## Technologies

- Python
- Pandas
- Streamlit
- Matplotlib
- LangChain
- Google Gemini API

## Project Structure

```text
AI-Data-Analyst/
├── data/
│   └── Indian_sales.csv
├── src/
│   ├── __init__.py
│   ├── ai_assistant.py
│   ├── analyzer.py
│   ├── data_cleaning.py
│   ├── data_loader.py
│   └── visualizer.py
├── app.py
├── dashboard.py
├── main.py
├── requirements.txt
└── README.md