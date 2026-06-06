# Упражнение 1. Результат периода

monthly_profit = float(input("Введите прибыль за месяц: "))

if monthly_profit > 0:
    print("Результат: Прибыль")
elif monthly_profit < 0:
    print("Результат: Убыток")
else:
    print("Результат: Безубыточность")

print("-" * 40)

# Упражнение 2. Категория бизнеса

revenue = float(input("Введите выручку компании: "))

if revenue < 1_000_000:
    print("Категория: Микробизнес")
elif revenue < 10_000_000:
    print("Категория: Малый бизнес")
elif revenue < 100_000_000:
    print("Категория: Средний бизнес")
else:
    print("Категория: Крупный бизнес")

print("-" * 40)

# Упражнение 3. Расчёт НДФЛ

salary = float(input("Введите зарплату: "))

if salary <= 50000:
    tax_rate = 0.13
else:
    tax_rate = 0.15

tax_amount = salary * tax_rate
salary_after_tax = salary - tax_amount

print(f"Налог: {tax_amount:.2f} руб.")
print(f"На руки: {salary_after_tax:.2f} руб.")

print("-" * 40)

# Упражнение 4. Таблица умножения ставки

interest_rate = float(input("Введите процентную ставку: "))

for multiplier in range(1, 13):
    result = interest_rate * multiplier
    print(f"{interest_rate} × {multiplier} = {result}")

print("-" * 40)

# Упражнение 5. Анализ цен

prices = [120, 450, 280, 700, 310]

for price in prices:
    if price > 300:
        print(f"{price} руб. - ДОРОГО")
    else:
        print(f"{price} руб.")