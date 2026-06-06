# Упражнение 1. Карточка сотрудника

employee_name = "Никита"
employee_age = 20
employee_salary = 50000.0
employee_is_working = True

print("Имя:", employee_name)
print("Возраст:", employee_age)
print("Зарплата:", employee_salary)
print("Работает:", employee_is_working)

print("-" * 40)

# Упражнение 2. Приветствие

employee_name_input = input("Введите имя сотрудника: ")
employee_city = input("Введите город: ")

print(f"Сотрудник {employee_name_input} работает в офисе {employee_city}")

print("-" * 40)

# Упражнение 3. Стоимость заказа

product_price = float(input("Введите цену товара: "))
product_quantity = int(input("Введите количество товара: "))

total_cost = product_price * product_quantity

print(f"Итоговая стоимость заказа: {total_cost:.2f} руб.")

print("-" * 40)

# Упражнение 4. Доход по вкладу

deposit_amount = float(input("Введите сумму вклада: "))
interest_rate = float(input("Введите процентную ставку: "))

annual_income = deposit_amount * interest_rate / 100

print(f"Доход по вкладу за год составит: {annual_income:.2f} руб.")

print("-" * 40)

# Упражнение 5. Конвертер валюты

dollar_rate = float(input("Введите курс доллара: "))
rub_amount = float(input("Введите сумму в рублях: "))

usd_amount = round(rub_amount / dollar_rate, 2)

print(f"Сумма в долларах: {usd_amount}")