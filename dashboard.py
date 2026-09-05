import streamlit as st

from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.analyzer import analyze_data
from src.ai_assistant import ask_ai


# Page configuration
st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="📊",
    layout="wide"
)


st.title("📊 AI Data Analyst Dashboard")
st.write("Analyze sales data using AI 🤖")


# Load dataset
@st.cache_data
def get_data():

    df = load_data("data/Indian_sales.csv")

    df = clean_data(df)

    return df


df = get_data()


# Generate analysis summary
summary = analyze_data(df)


st.subheader("📄 Dataset Preview")

st.dataframe(df.head(10))


st.subheader("📈 Business Overview")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Total Revenue",
        summary["Total Revenue"]
    )


with col2:
    st.metric(
        "Total Orders",
        summary["Total Orders"]
    )


with col3:
    st.metric(
        "Average Order Value",
        summary["Average Order Value"]
    )


st.divider()




st.subheader("🏆 Business Insights")


st.write(
    "📍 Best Performing State:",
    summary["Best Performing State"]
)


st.write(
    "🏷️ Best Category:",
    summary["Best Category"]
)


st.write(
    "🥇 Best Selling Product:",
    summary["Best Selling Product"]
)


st.write(
    "📅 Best Sales Month:",
    summary["Best Sales Month"]
)





st.divider()

st.subheader("🤖 Ask AI Business Analyst")


question = st.text_input(
    "Ask your sales question"
)


if question:

    with st.spinner("Analyzing..."):

        answer = ask_ai(
            question,
            summary
        )


    st.success("AI Response")

    st.write(answer)