import random
import time

class Stock:
    def __init__(self, name, initial_price):
        self.name = name
        self.price = initial_price

    # Random price fluctuation to simulate market movement
    def update_price(self):
        fluctuation = random.uniform(-0.05, 0.05)  # Price change between -5% to +5%
        self.price += self.price * fluctuation
        self.price = round(self.price, 2)  # Round price to 2 decimal places

    def __str__(self):
        return f"{self.name}: ${self.price}"

class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.portfolio = {}

    def buy_stock(self, stock, quantity):
        total_cost = stock.price * quantity
        if total_cost <= self.balance:
            self.balance -= total_cost
            if stock.name in self.portfolio:
                self.portfolio[stock.name] += quantity
            else:
                self.portfolio[stock.name] = quantity
            print(f"Bought {quantity} shares of {stock.name} for ${total_cost}.")
        else:
            print("Insufficient balance to complete the purchase.")

    def sell_stock(self, stock, quantity):
        if stock.name in self.portfolio and self.portfolio[stock.name] >= quantity:
            total_income = stock.price * quantity
            self.portfolio[stock.name] -= quantity
            self.balance += total_income
            print(f"Sold {quantity} shares of {stock.name} for ${total_income}.")
        else:
            print("You do not have enough shares to sell.")

    def portfolio_summary(self):
        print(f"\nPortfolio for {self.name}:")
        print(f"Balance: ${self.balance}")
        if not self.portfolio:
            print("No stocks in your portfolio.")
        else:
            for stock_name, quantity in self.portfolio.items():
                print(f"{stock_name}: {quantity} shares")

    def get_total_value(self, stock_market):
        total_value = self.balance
        for stock_name, quantity in self.portfolio.items():
            stock = stock_market.get(stock_name)
            total_value += stock.price * quantity
        return total_value

class StockMarket:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, stock):
        self.stocks[stock.name] = stock

    def get(self, stock_name):
        return self.stocks.get(stock_name)

    def update_prices(self):
        for stock in self.stocks.values():
            stock.update_price()

def display_menu():
    print("\n--- Virtual Stock Market Simulator ---")
    print("1. View Available Stocks")
    print("2. Buy Stock")
    print("3. Sell Stock")
    print("4. View Portfolio")
    print("5. View Total Portfolio Value")
    print("6. Update Stock Prices")
    print("7. Exit")

def run_simulation():
    # Initialize stock market and add some stocks
    market = StockMarket()
    market.add_stock(Stock("AAPL", 150.0))
    market.add_stock(Stock("GOOG", 2700.0))
    market.add_stock(Stock("AMZN", 3300.0))
    market.add_stock(Stock("TSLA", 750.0))

    # Create a user with initial balance
    user = User("John Doe", 10000.0)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nAvailable Stocks:")
            for stock in market.stocks.values():
                print(stock)

        elif choice == '2':
            stock_name = input("Enter stock name to buy (e.g., AAPL, GOOG): ").upper()
            quantity = int(input("Enter quantity to buy: "))
            stock = market.get(stock_name)
            if stock:
                user.buy_stock(stock, quantity)
            else:
                print("Stock not found.")

        elif choice == '3':
            stock_name = input("Enter stock name to sell (e.g., AAPL, GOOG): ").upper()
            quantity = int(input("Enter quantity to sell: "))
            stock = market.get(stock_name)
            if stock:
                user.sell_stock(stock, quantity)
            else:
                print("Stock not found.")

        elif choice == '4':
            user.portfolio_summary()

        elif choice == '5':
            total_value = user.get_total_value(market)
            print(f"\nTotal Portfolio Value: ${total_value:.2f}")

        elif choice == '6':
            print("\nUpdating stock prices...")
            market.update_prices()
            time.sleep(1)  # Delay to simulate stock price change over time

        elif choice == '7':
            print("Exiting the simulation. Thank you for playing!")
            break

        else:
            print("Invalid choice, please try again.")

# Start the simulation
if __name__ == "__main__":
    run_simulation()