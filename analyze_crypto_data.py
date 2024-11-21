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

    # Create a DataFrame from the fetched data
    df = pd.DataFrame(data)
    
    # Print the columns to inspect the data structure
    print("Columns in the fetched data:", df.columns)

    # Now, filter the necessary columns and rename them
    df = df[['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']]

    # Rename the columns for better readability
    df.columns = ['Cryptocurrency Name', 'Symbol', 'Current Price (USD)', 
                  'Market Capitalization', '24-Hour Trading Volume (USD)', '24-Hour Price Change (%)']

    # Step 2.1: Identifying the top 5 cryptocurrencies by market cap
    top_5_by_market_cap = df.sort_values('Market Capitalization', ascending=False).head(5)
    print("Top 5 Cryptocurrencies by Market Cap:")
    print(top_5_by_market_cap[['Cryptocurrency Name', 'Market Capitalization']])

    # Step 2.2: Calculate the average price of the top 50 cryptocurrencies
    average_price = df['Current Price (USD)'].mean()
    print(f"\nAverage Price of the Top 50 Cryptocurrencies: ${average_price:.2f}")

    # Step 2.3: Find the highest and lowest 24-hour price change
    highest_price_change = df.loc[df['24-Hour Price Change (%)'].idxmax()]
    lowest_price_change = df.loc[df['24-Hour Price Change (%)'].idxmin()]

    print("\nCryptocurrency with the Highest 24-Hour Price Change:")
    print(highest_price_change[['Cryptocurrency Name', '24-Hour Price Change (%)']])

    print("\nCryptocurrency with the Lowest 24-Hour Price Change:")
    print(lowest_price_change[['Cryptocurrency Name', '24-Hour Price Change (%)']])

else:
    print(f"Error: Unable to fetch data (status code {response.status_code})")
