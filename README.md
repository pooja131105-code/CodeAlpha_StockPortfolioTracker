# CodeAlpha_StockPortfolioTracker

A simple Stock Portfolio Tracker developed using Python as part of the CodeAlpha Internship.

## Description

This project allows users to enter stock names and quantities and calculates the total investment value based on predefined stock prices.

The stock prices are stored in a Python dictionary, making the project simple and easy to use.

## Features

* Enter stock names and quantities
* Predefined stock prices
* Calculate investment for each stock
* Calculate total portfolio investment
* Handles invalid stock names
* Simple console-based interface

## Technologies Used

* Python

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or Command Prompt.
4. Run the following command:

```bash
python stock_tracker.py
```

## How It Works

1. The program stores predefined stock prices in a dictionary.
2. The user enters a stock name.
3. The program asks for the quantity of the stock.
4. It calculates the investment using:

```text
Stock Price × Quantity
```

5. The investment is added to the total portfolio value.
6. The user can enter multiple stocks.
7. Enter `done` to finish and display the total investment.

## Available Stocks

* AAPL
* TSLA
* GOOGL
* MSFT
* AMZN

## Project Structure

```text
CodeAlpha_StockPortfolioTracker
│
├── stock_tracker.py
└── README.md
```

## Internship Task

This project was developed as **Task 2 – Stock Portfolio Tracker** for the CodeAlpha Python Programming Internship.
