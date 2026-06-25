prices = {
    "AAPL": 182,
    "TSLA": 248,
    "GOOGL": 175,
    "MSFT": 415,
    "AMZN": 195,
    "NVDA": 875
}

portfolio = {}
print("\n📈 Stock Tracker  |  Stocks:", ", ".join(prices))
print("Type 'done' to finish.\n")

while True:
    stock = input("Stock symbol: ").upper().strip()
    if stock == "DONE":
        break
    if stock not in prices:
        print(f"  ❌ Not found! Choose from: {', '.join(prices)}\n")
        continue
    qty = input(f"  How many shares? ").strip()
    if not qty.isdigit():
        print("  ⚠️  Numbers only!\n")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + int(qty)
    print(f"  ✅ {qty} × {stock} @ ${prices[stock]} added!\n")

if not portfolio:
    print("Nothing added. Bye! 👋")
else:
    print("\n" + "─" * 35)
    total = 0
    for stock, qty in portfolio.items():
        value = qty * prices[stock]
        total += value
        print(f"  {stock:6}  {qty} shares  →  ${value:,}")
    print("─" * 35)
    print(f"  💰 Total invested: ${total:,}")
    print("─" * 35 + "\n")
