income = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
profit = int(income - costs)

if income > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / income}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers}")
elif income == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")
