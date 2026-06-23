import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# MySQL Connection
engine = create_engine(
    "mysql+pymysql://root:Sreevalsam%40123@localhost/steam_market_intelligence"
)

st.title("🎮 Steam Market Intelligence Dashboard")
st.write(
    "Analyze Steam game pricing, publishers, developers and discounts using MySQL and Streamlit."
)

# Load data
query = """
SELECT title,
       original_price,
       discounted_price,
       publisher,
       developer
FROM steam_games
LIMIT 1000
"""

df = pd.read_sql(query, engine)

# Sidebar Filters
st.sidebar.header("Filters")

publisher = st.sidebar.selectbox(
    "Publisher",
    ["All"] + sorted(df["publisher"].dropna().unique())
)

if publisher != "All":
    df = df[df["publisher"] == publisher]

# Metrics
# Metrics
avg_price = pd.to_numeric(
    df["original_price"]
    .replace("Free", "0")
    .str.replace("$", "", regex=False),
    errors="coerce"
).mean()

col1, col2, col3 = st.columns(3)

col1.metric("Games Loaded", len(df))
col2.metric("Average Price", f"${avg_price:.2f}")
col3.metric("Publishers", df["publisher"].nunique())
st.subheader("Free vs Paid Games")

free_games = (df["original_price"] == "Free").sum()
paid_games = len(df) - free_games

fig, ax = plt.subplots()

ax.pie(
    [free_games, paid_games],
    labels=["Free", "Paid"],
    autopct="%1.1f%%"
)

st.pyplot(fig)
# Show data
st.subheader("Game Dataset")
search = st.text_input("Search Game")

if search:
    df = df[df["title"].str.contains(search, case=False, na=False)]
st.dataframe(df)
st.subheader("Top Publishers")

publisher_count = (
    df.groupby("publisher")
      .size()
      .reset_index(name="games")
      .sort_values("games", ascending=False)
      .head(10)
)

fig, ax = plt.subplots()

publisher_count.sort_values("games").plot(
    kind="barh",
    x="publisher",
    y="games",
    ax=ax
)

st.pyplot(fig)
st.subheader("Top Developers")

developer_count = (
    df.groupby("developer")
      .size()
      .reset_index(name="games")
      .sort_values("games", ascending=False)
      .head(10)
)


st.subheader("Price Statistics")

price_df = df.copy()

price_df["price_num"] = pd.to_numeric(
    price_df["original_price"]
    .replace("Free", "0")
    .str.replace("$", "", regex=False),
    errors="coerce"
)

st.subheader("Price Distribution")

fig, ax = plt.subplots()

ax.hist(
    price_df["price_num"].dropna(),
    bins=20
)

st.pyplot(fig)

# Top Publishers

st.subheader("Top 10 Most Expensive Games")
st.subheader("Top Discounts")

discount_df = df.copy()

discount_df["original_num"] = (
    discount_df["original_price"]
    .replace("Free", "0")
    .str.replace("$", "", regex=False)
    .astype(float)
)

discount_df["discounted_num"] = (
    discount_df["discounted_price"]
    .replace("Free", "0")
    .str.replace("$", "", regex=False)
    .astype(float)
)

discount_df["discount_amount"] = (
    discount_df["original_num"]
    - discount_df["discounted_num"]
)

top_discounts = discount_df.sort_values(
    "discount_amount",
    ascending=False
).head(10)

st.dataframe(
    top_discounts[
        ["title", "original_price",
         "discounted_price",
         "discount_amount"]
    ]
)

price_df = df.copy()

price_df["price_num"] = (
    price_df["original_price"]
    .replace("Free", "0")
    .str.replace("$", "", regex=False)
    .astype(float)
)

top_expensive = price_df.sort_values(
    "price_num",
    ascending=False
).head(10)

st.dataframe(
    top_expensive[
        ["title", "original_price", "publisher"]
    ]
)

st.markdown("---")
st.caption(
    "Steam Market Intelligence Dashboard | Python + MySQL + Streamlit"
)