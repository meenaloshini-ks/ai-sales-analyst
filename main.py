from src.data_loader import load_data
from src.analyzer import analyze_data
from src.visualizer import (
    plot_sales_by_state,
    plot_category_sales,
    plot_daily_sales,
    plot_top_products,
)

# Load dataset
df = load_data("data/Indian_sales.csv")

# Analyze dataset
analyze_data(df)

# Generate visualizations
plot_sales_by_state(df)
plot_category_sales(df)
plot_daily_sales(df)
plot_top_products(df)