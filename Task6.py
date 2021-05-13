
start_distance = float(input('Введите начальную дистанцию: '))
target_distance = float(input('Введите целевую дистанцию: '))

distance_ = start_distance
day_counter = 1

while distance_ < target_distance:
    day_counter += 1
    distance_ *= 1.1

print(day_counter)
