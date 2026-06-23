import pandas as pd
from sqlalchemy import create_engine

# Load cleaned CSV
df = pd.read_csv("data/processed/steam_games_cleaned.csv")
df.columns = [
    "title",
    "original_price",
    "discounted_price",
    "release_date",
    "review_summary",
    "review_count",
    "developer",
    "publisher",
    "popular_tags"
]

# Connect to MySQL
engine = create_engine(
    "mysql+pymysql://root:YOUR_PASSWORD@localhost/steam_market_intelligence"

# Load data into MySQL
df.to_sql(
    "steam_games",
    con=engine,
    if_exists="replace",
    index=False
)
