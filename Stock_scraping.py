import pandas as pd
from datetime import datetime
from nsetools import Nse
import requests
from bs4 import BeautifulSoup

# Initialize NSE object
nse = Nse()

# Define random stock symbols and Nifty 50 index
random_stocks = [
    "RELIANCE", "TCS", "HDFCBANK", "INFY", "ITC",
    "SBIN", "WIPRO", "BHARTIARTL", "LT", "HDFC",
    "MARUTI", "TITAN", "BAJAJFINSV", "ICICIBANK", "ASIANPAINT",
    "SUNPHARMA", "ULTRACEMCO", "TATAMOTORS", "HINDUNILVR", "TECHM",
    "ONGC", "NTPC", "AXISBANK", "POWERGRID", "ADANIENT",
    "ADANIGREEN", "ADANIPORTS", "COALINDIA", "JSWSTEEL", "INDUSINDBK",
    "DIVISLAB", "GRASIM", "HINDALCO", "DRREDDY", "BAJAJ-AUTO",
    "EICHERMOT", "HEROMOTOCO", "BPCL", "BRITANNIA", "UPL",
    "SHREECEM", "DLF", "VEDL", "GAIL", "M&M",
    "NMDC", "PEL", "BANDHANBNK", "BIOCON"
]
nifty50 = ["NIFTY 50"]

# Scrape sector mapping from NSE website
def scrape_sector_mapping():
    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    data = response.json()

    sector_mapping = {}
    for stock in data["data"]:
        ticker = stock["symbol"]
        sector = stock.get("sector", "Unknown")
        sector_mapping[ticker] = sector

    return sector_mapping

# Fetch stock data from NSE
def fetch_stock_data(stock_list):
    stock_data = []
    for stock in stock_list:
        try:
            quote = nse.get_quote(stock)
            data = {
                "Date": datetime.now().strftime("%Y-%m-%d"),
                "Ticker": stock,
                "Sector": "Unknown",  # Placeholder until mapped
                "Close": quote["lastPrice"],
                "Volume": quote["quantityTraded"],
            }
            stock_data.append(data)
        except Exception as e:
            print(f"Error fetching data for {stock}: {e}")
    return pd.DataFrame(stock_data)

# Get sector mapping
sector_mapping = scrape_sector_mapping()

# Fetch data and map sectors
random_stock_data = fetch_stock_data(random_stocks)
random_stock_data["Sector"] = random_stock_data["Ticker"].map(sector_mapping).fillna("Unknown")

# Fetch Nifty 50 data
nifty50_data = fetch_stock_data(nifty50)
nifty50_data["Sector"] = "Index"

# Save data to Excel
random_stock_data.to_excel("random_stocks_data.xlsx", index=False)
nifty50_data.to_excel("nifty50_data.xlsx", index=False)

print("Data scraping and cleaning complete.")