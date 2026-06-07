# Мини-проект
# Калькулятор рентабельности бизнеса

def calculate_profit(revenue, expenses):
    return revenue - expenses

def calculate_profitability(profit, expenses):
    if expenses == 0:
        return 0
    return (profit / expenses) * 100

print("КАЛЬКУЛЯТОР РЕНТАБЕЛЬНОСТИ БИЗНЕСА")
print("-" * 40)

number_of_months = int(input("Введите количество месяцев для анализа: "))

profits = []

for month in range(1, number_of_months + 1):
    print(f"\nМесяц {month}")

    revenue = float(input("Введите выручку: "))
    expenses = float(input("Введите расходы: "))

    profit = calculate_profit(revenue, expenses)
    profitability = calculate_profitability(profit, expenses)

    profits.append(profit)

    print(f"Прибыль: {profit:.2f} руб.")
    print(f"Рентабельность: {profitability:.2f}%")

    if profit > 0:
        print("Статус: Прибыльный месяц")
    elif profit < 0:
        print("Статус: Убыточный месяц")
    else:
        print("Статус: Безубыточность")

print("\n" + "-" * 40)

total_profit = sum(profits)
average_profit = total_profit / len(profits)

print("ИТОГОВЫЙ ОТЧЁТ")
print(f"Общая прибыль: {total_profit:.2f} руб.")
print(f"Средняя прибыль: {average_profit:.2f} руб.")

if total_profit > 0:
    print("Общий результат: Бизнес прибыльный")
elif total_profit < 0:
    print("Общий результат: Бизнес убыточный")
else:
    print("Общий результат: Безубыточность")