def format_currency(value):

    if value >= 10000000:
        return f"₹{value/10000000:.2f} Crore"

    elif value >= 100000:
        return f"₹{value/100000:.2f} Lakh"

    else:
        return f"₹{value:,.0f}"


def analyze_data(df):

    print("\n========== SALES ANALYSIS ==========")


    # Total Revenue
    total_sales = df["Sales_INR"].sum()
    total_revenue = format_currency(total_sales)

    print("\n💰 Total Revenue:", total_revenue)


    # Total Orders
    total_orders = len(df)

    print("📦 Total Orders:", total_orders)


    # Average Order Value
    avg_sales = df["Sales_INR"].mean()
    average_order = format_currency(avg_sales)

    print("📊 Average Order Value:", average_order)


    # Best State
    state_sales = (
        df.groupby("State")["Sales_INR"]
        .sum()
        .sort_values(ascending=False)
    )

    top_state = state_sales.index[0]

    print("📍 Best Performing State:", top_state)


    # Best Category
    category_sales = (
        df.groupby("Category")["Sales_INR"]
        .sum()
        .sort_values(ascending=False)
    )

    top_category = category_sales.index[0]

    print("🏆 Best Category:", top_category)


    # Best Product
    product_sales = (
        df.groupby("Product")["Sales_INR"]
        .sum()
        .sort_values(ascending=False)
    )

    top_product = product_sales.index[0]

    print("🥇 Best Selling Product:", top_product)


    # Best Month
    df["Month"] = df["Date"].dt.month_name()

    monthly_sales = (
        df.groupby("Month")["Sales_INR"]
        .sum()
        .sort_values(ascending=False)
    )

    best_month = monthly_sales.index[0]

    print("📅 Best Sales Month:", best_month)


    print("\n====================================")


    # Return AI summary
    summary = {

        "Total Revenue": total_revenue,

        "Total Orders": total_orders,

        "Average Order Value": average_order,

        "Best Performing State": top_state,

        "Best Category": top_category,

        "Best Selling Product": top_product,

        "Best Sales Month": best_month
    }


    return summary