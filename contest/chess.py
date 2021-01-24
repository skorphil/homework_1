# Шахматный ферзь может ходить на любое число клеток по горизонтали, по вертикали или по диагонали. Даны две различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом. Для простоты можно не рассматривать случай, когда данные клетки совпадают.

# Формат входных данных
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.

# Формат выходных данных
# Программа должна вывести YES, если из первой клетки ходом ферзя можно попасть во вторую. В противном случае - NO.

print("Input 4 numbers 1-8")
move_coordinates = input(int())
current_x = int(move_coordinates[0])
current_y = int(move_coordinates[1])
planned_x = int(move_coordinates[2])
planned_y = int(move_coordinates[3])

if current_x == planned_x or current_y == planned_y:
    print("YES")

elif current_x < planned_x:
    x_difference = planned_x - current_x
elif current_x > planned_x:
    x_difference = current_x - planned_x

elif current_y - planned_y == x_difference or planned_y - current_y == x_difference:
    print("YES")
else:
    print("NO")
