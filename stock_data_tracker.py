import yfinance as yf
import pandas as pd
from datetime import datetime

# Define random stock symbols
random_stocks = [
    "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ITC.NS",
    "SBIN.NS", "WIPRO.NS", "BHARTIARTL.NS", "LT.NS", "SEPC.NS",
    "MARUTI.NS", "TITAN.NS", "BAJAJFINSV.NS", "ICICIBANK.NS", "ASIANPAINT.NS",
    "SUNPHARMA.NS", "ULTRACEMCO.NS", "TATAMOTORS.NS", "HINDUNILVR.NS", "TECHM.NS",
    "ONGC.NS", "NTPC.NS", "AXISBANK.NS", "POWERGRID.NS", "ADANIENT.NS",
    "ADANIGREEN.NS", "ADANIPORTS.NS", "COALINDIA.NS", "JSWSTEEL.NS", "INDUSINDBK.NS",
    "DIVISLAB.NS", "GRASIM.NS", "HINDALCO.NS", "DRREDDY.NS", "BAJAJ-AUTO.NS",
    "EICHERMOT.NS", "HEROMOTOCO.NS", "BPCL.NS", "BRITANNIA.NS", "UPL.NS",
    "SHREECEM.NS", "DLF.NS", "VEDL.NS", "GAIL.NS", "M&M.NS",
    "NMDC.NS", "PEL.NS", "BANDHANBNK.NS", "BIOCON.NS"
]
nifty50 = ["^NSEI"]  # Nifty 50 index

# Step 1: Function to fetch stock data
# def fetch_historical_data(stock_list, start_date="2020-01-01", end_date=None):
#     all_data = []
#     for stock in stock_list:
#         try:
#             ticker = yf.Ticker(stock)
#             print(f"Fetching data for {stock}...")
#             history = ticker.history(start=start_date, end=end_date, interval="1d")
#             history["Ticker"] = stock
#             history.reset_index(inplace=True)
#             all_data.append(history)
#         except Exception as e:
#             print(f"Error fetching data for {stock}: {e}")
#     return pd.concat(all_data, ignore_index=True)

# # Step 2: Update data for all stocks and index
# def update_data():
#     # Fetch updated portfolio data
#     today = datetime.now().strftime("%Y-%m-%d")
#     portfolio_data = fetch_historical_data(random_stocks, start_date="2020-01-01", end_date=today)
    
#     # Fetch updated index data
#     nifty_data = fetch_historical_data(nifty50, start_date="2020-01-01", end_date=today)

#     # Save the updated data
#     portfolio_data.to_excel("portfolio_data.xlsx", index=False)
#     nifty_data.to_excel("nifty50_data.xlsx", index=False)
#     print(f"Data updated and saved on {today}.")

# def fetch_historical_data(stock_list, start_date="2020-01-01", end_date=None):
#     if isinstance(stock_list, str):  # Allow single stock as string input
#         stock_list = [stock_list]

#     all_data = []
#     for stock in stock_list:
#         try:
#             ticker = yf.Ticker(stock)
#             print(f"Fetching data for {stock}...")
#             history = ticker.history(start=start_date, end=end_date, interval="1d")
#             if not history.empty:  # Only append if data is not empty
#                 history["Ticker"] = stock
#                 history.reset_index(inplace=True)
#                 all_data.append(history)
#             else:
#                 print(f"No data available for {stock}.")
#         except Exception as e:
#             print(f"Error fetching data for {stock}: {e}")

#     if all_data:  # Check if data exists before concatenation
#         return pd.concat(all_data, ignore_index=True)
#     else:
#         print("No valid data fetched for any stock.")
#         return pd.DataFrame()  # Return an empty DataFrame

# def update_data():
#     today = datetime.now().strftime("%Y-%m-%d")
    
#     # Fetch updated portfolio data
#     portfolio_data = fetch_historical_data(random_stocks, start_date="2020-01-01", end_date=today)
#     if not portfolio_data.empty:
#         # Convert timezone-aware datetimes to naive
#         if "Date" in portfolio_data.columns:
#             portfolio_data["Date"] = portfolio_data["Date"].dt.tz_localize(None)
        
#         portfolio_data.to_excel("portfolio_data.xlsx", index=False)
#         print("Portfolio data updated successfully.")
#     else:
#         print("Portfolio data update failed: No data available.")

#     # Fetch updated index data
#     nifty_data = fetch_historical_data(nifty50, start_date="2020-01-01", end_date=today)
#     if not nifty_data.empty:
#         # Convert timezone-aware datetimes to naive
#         if "Date" in nifty_data.columns:
#             nifty_data["Date"] = nifty_data["Date"].dt.tz_localize(None)
        
#         nifty_data.to_excel("nifty50_data.xlsx", index=False)
#         print("Nifty 50 data updated successfully.")
#     else:
#         print("Nifty 50 data update failed: No data available.")

import time
import logging

# Setup logging
logging.basicConfig(filename="stock_data_log.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_historical_data(stock_list, start_date="2020-01-01", end_date=None):
    if isinstance(stock_list, str):  # Allow single stock as string input
        stock_list = [stock_list]

    all_data = []
    for stock in stock_list:
        try:
            ticker = yf.Ticker(stock)
            logging.info(f"Fetching data for {stock}...")
            history = ticker.history(start=start_date, end=end_date, interval="1d")
            
            if not history.empty:  # Only append if data is not empty
                history["Ticker"] = stock
                history.reset_index(inplace=True)
                all_data.append(history)
            else:
                logging.warning(f"No data available for {stock}.")
            
            time.sleep(1)  # Add delay to avoid rate-limiting issues
        except Exception as e:
            logging.error(f"Error fetching data for {stock}: {e}")

    if all_data:  # Check if data exists before concatenation
        return pd.concat(all_data, ignore_index=True)
    else:
        logging.error("No valid data fetched for any stock.")
        return pd.DataFrame()  # Return an empty DataFrame

def update_data():
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Fetch updated portfolio data
    portfolio_data = fetch_historical_data(random_stocks, start_date="2020-01-01", end_date=today)
    if not portfolio_data.empty:
        # Convert timezone-aware datetimes to naive
        if "Date" in portfolio_data.columns:
            portfolio_data["Date"] = portfolio_data["Date"].dt.tz_localize(None)
        
        try:
            portfolio_data.to_excel("portfolio_data.xlsx", index=False)
            logging.info("Portfolio data updated and saved successfully.")
        except Exception as e:
            logging.error(f"Failed to save portfolio data: {e}")
    else:
        logging.warning("Portfolio data update failed: No data available.")

    # Fetch updated index data
    nifty_data = fetch_historical_data(nifty50, start_date="2020-01-01", end_date=today)
    if not nifty_data.empty:
        # Convert timezone-aware datetimes to naive
        if "Date" in nifty_data.columns:
            nifty_data["Date"] = nifty_data["Date"].dt.tz_localize(None)
        
        try:
            nifty_data.to_excel("nifty50_data.xlsx", index=False)
            logging.info("Nifty 50 data updated and saved successfully.")
        except Exception as e:
            logging.error(f"Failed to save Nifty 50 data: {e}")
    else:
        logging.warning("Nifty 50 data update failed: No data available.")

# Run update function
if __name__ == "__main__":
    update_data()
    print ("Update complete")
else:
    print ("Error please check")    