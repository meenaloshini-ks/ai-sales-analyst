from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.analyzer import analyze_data
from src.visualizer import (
    plot_sales_by_state,
    plot_category_sales,
    plot_daily_sales,
    plot_top_products,
)
from src.ai_assistant import ask_ai


# Load dataset
df = load_data("data/Indian_sales.csv")


# Clean data
df = clean_data(df)


# Analysis
summary = analyze_data(df)


# Generate charts only when needed
create_charts = False


if create_charts:
    plot_sales_by_state(df)
    plot_category_sales(df)
    plot_daily_sales(df)
    plot_top_products(df)


# AI Assistant
question = input("\nAsk your sales question: ")

answer = ask_ai(
    question,
    summary
)

print("\n🤖 AI Analyst:")
print(answer)