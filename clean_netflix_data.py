import pandas as pd

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Strip whitespaces from column names
df.columns = df.columns.str.strip()

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing values
df['director'].fillna("No Director", inplace=True)
df['cast'].fillna("No Cast Info", inplace=True)
df['country'].fillna("Unknown Country", inplace=True)
df['date_added'].fillna("Unknown Date", inplace=True)
df['rating'].fillna("Unrated", inplace=True)
df['duration'].fillna("Unknown Duration", inplace=True)

# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Split 'duration' into numeric and type (e.g., 90, min)
df[['duration_int', 'duration_type']] = df['duration'].str.extract(r'(\d+)\s*(\w+)')
df['duration_int'] = pd.to_numeric(df['duration_int'], errors='coerce')

# Clean whitespace from string columns
text_columns = ['title', 'director', 'cast', 'country', 'rating', 'listed_in', 'description']
for col in text_columns:
    df[col] = df[col].str.strip()

# Save cleaned data to a new CSV file
df.to_csv("cleaned_netflix_data.csv", index=False)

print("Data cleaning completed. Cleaned file saved as 'cleaned_netflix_data.csv'")

