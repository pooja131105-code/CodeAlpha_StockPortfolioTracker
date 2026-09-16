stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

print("===== Stock Portfolio Tracker =====")

total_investment = 0

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Stock Price:", stock_prices[stock_name])
        print("Investment:", investment)

    else:
        print("Stock not found. Please choose from:")
        print(", ".join(stock_prices.keys()))

print("\n===== Portfolio Summary =====")
print("Total Investment Value: $", total_investment)
print("Thank you for using Stock Portfolio Tracker!")