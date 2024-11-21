import requests
import pandas as pd

# URL to fetch data from CoinGecko API
url = 'https://api.coingecko.com/api/v3/coins/markets'
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',  # Order by market cap
    'per_page': 50,              # Fetch top 50
    'page': 1                    # Page number
}

# Send GET request to the CoinGecko API
response = requests.get(url, params=params)

# If the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Parse JSON data into Python list

    # Print the first entry of the data to inspect its structure
    print(data[0])  # This will show you the fields available for the first cryptocurrency

    # Create a DataFrame from the fetched data
    df = pd.DataFrame(data)
    
    # Display all columns in the DataFrame to see what's available
    print("Columns in the fetched data:", df.columns)

    # Select relevant columns for display (adjust if needed)
    df = df[['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']]  # Adjust field name

    # Rename columns to be more user-friendly
    df.columns = ['Cryptocurrency Name', 'Symbol', 'Current Price (USD)', 'Market Capitalization', '24-Hour Trading Volume (USD)', '24-Hour Price Change (%)']
    
    # Display the data
    print(df.head())  # Show first 5 rows
    
    # Save the data to an Excel file
    df.to_excel('cryptocurrency_data.xlsx', index=False)
else:
    print(f"Error: Unable to fetch data (status code {response.status_code})")
