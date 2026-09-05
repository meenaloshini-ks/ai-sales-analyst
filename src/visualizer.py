import os
import matplotlib.pyplot as plt


# Create charts folder
os.makedirs("charts", exist_ok=True)


def format_currency(value):
    """
    Convert numbers into Indian currency format
    """

    if value >= 10000000:
        return f"₹{value / 10000000:.2f} Cr"

    elif value >= 100000:
        return f"₹{value / 100000:.2f} L"

    else:
        return f"₹{value:,.0f}"


def plot_sales_by_state(df):

    sales = (
        df.groupby("State")["Sales_INR"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))

    bars = sales.plot(kind="bar")

    plt.title("Sales by State")
    plt.xlabel("State")
    plt.ylabel("Revenue (₹)")

    # Add labels
    for bar, value in zip(bars.patches, sales):
        plt.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height(),
            format_currency(value),
            ha="center",
            va="bottom",
            fontsize=8
        )

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        "charts/sales_by_state.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()



def plot_category_sales(df):

    sales = (
        df.groupby("Category")["Sales_INR"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 6))

    bars = sales.plot(kind="bar")

    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue (₹)")

    for bar, value in zip(bars.patches, sales):

        plt.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height(),
            format_currency(value),
            ha="center",
            va="bottom",
            fontsize=8
        )

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        "charts/category_sales.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()



def plot_daily_sales(df):

    daily_sales = (
        df.groupby("Date")["Sales_INR"]
        .sum()
    )

    plt.figure(figsize=(12, 6))

    plt.plot(
        daily_sales.index,
        daily_sales.values
    )

    plt.title("Daily Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Revenue (₹)")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        "charts/daily_sales.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()



def plot_top_products(df):

    products = (
        df.groupby("Product")["Sales_INR"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 6))

    bars = products.plot(kind="bar")

    plt.title("Top 10 Products by Sales")
    plt.xlabel("Product")
    plt.ylabel("Revenue (₹)")

    for bar, value in zip(bars.patches, products):

        plt.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height(),
            format_currency(value),
            ha="center",
            va="bottom",
            fontsize=8
        )

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        "charts/top_products.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()