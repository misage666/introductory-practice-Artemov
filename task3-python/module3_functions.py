# Упражнение 1. calculate_profit()

def calculate_profit(revenue, costs):
    return revenue - costs

print("Прибыль 1:", calculate_profit(100000, 70000))
print("Прибыль 2:", calculate_profit(250000, 180000))
print("Прибыль 3:", calculate_profit(500000, 320000))

print("-" * 40)

# Упражнение 2. calculate_vat()

def calculate_vat(price, vat_rate=20):
    return price * vat_rate / 100

print("НДС (20%):", calculate_vat(1000))
print("НДС (10%):", calculate_vat(1000, 10))

print("-" * 40)

# Упражнение 3. get_category()

def get_category(revenue):
    if revenue < 1_000_000:
        return "Микробизнес"
    elif revenue < 10_000_000:
        return "Малый бизнес"
    elif revenue < 100_000_000:
        return "Средний бизнес"
    else:
        return "Крупный бизнес"

print(get_category(500000))
print(get_category(5000000))
print(get_category(50000000))
print(get_category(500000000))

print("-" * 40)

# Упражнение 4. compound_interest()

def compound_interest(capital, rate, years):
    return capital * (1 + rate / 100) ** years

start_capital = 100000
annual_rate = 10

print("Через 3 года:", round(compound_interest(start_capital, annual_rate, 3), 2))
print("Через 5 лет:", round(compound_interest(start_capital, annual_rate, 5), 2))
print("Через 10 лет:", round(compound_interest(start_capital, annual_rate, 10), 2))

print("-" * 40)

# Упражнение 5. apply_discount()

def apply_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)

product_prices = [1000, 2500, 3200, 4500, 6000]

for price in product_prices:
    discounted_price = apply_discount(price, 15)
    print(f"Цена {price} руб. -> {discounted_price:.2f} руб.")