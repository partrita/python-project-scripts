import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


# Function to get a list of tickers for analysis
def get_ticker_list():
    while True:
        try:
            option = int(
                input(
                    "You have 2 options:\n1. Analyze top stocks in S&P index\n2. Specific Stocks\nEnter option (1/2): "
                )
            )

            if option == 1:
                stocknum = int(
                    input("How many stocks do you want to analyze? Enter a number: ")
                )
                toptickers = pd.read_html(
                    "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
                )[0]
                return toptickers.head(stocknum).Symbol.to_list()
            elif option == 2:
                inputstr = input(
                    "Enter comma-separated ticker symbols of interested stocks: "
                )
                return inputstr.upper().split(",")
            else:
                print("Please enter a valid option (1/2).")
        except ValueError:
            print("Please input a valid integer only.")


# Function to get the time period for analysis
def get_time_period():
    try:
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        return start_date, end_date
    except ValueError:
        print("Invalid date format. Please use the format YYYY-MM-DD.")


# Main function
def main():
    tickerlist = get_ticker_list()

    start_date, end_date = get_time_period()  # Get time period for analysis

    data = pd.DataFrame()

    # Loop through each ticker to fetch data
    for ticker in tickerlist:
        try:
            y = yf.Ticker(ticker)
            df = y.history(period="1d", start=start_date, end=end_date)
            if not df.empty:
                data[ticker] = df["Close"]
            else:
                print("No data found for", ticker)
        except Exception as e:
            print("An error occurred while fetching data for", ticker, ":", str(e))

    if not data.empty:
        # Plotting the data
        data.plot(title="Stock Price Analysis")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.show()

        print(data.head())
    else:
        print("No data available for analysis.")


# Entry point of the program
if __name__ == "__main__":
    main()
