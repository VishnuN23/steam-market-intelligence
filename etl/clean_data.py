import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/merged_data.csv")

# Keep only useful columns
columns_to_keep = [
    "Title",
    "Original Price",
    "Discounted Price",
    "Release Date",
    "All Reviews Summary",
    "All Reviews Number",
    "Developer",
    "Publisher",
    "Popular Tags"
]

df = df[columns_to_keep]

# Remove duplicate games
df = df.drop_duplicates()

# Fill missing values
df = df.fillna("Unknown")

# Save cleaned data
df.to_csv(
    "data/processed/steam_games_cleaned.csv",
    index=False
)

print("Cleaning completed!")
print(df.shape)