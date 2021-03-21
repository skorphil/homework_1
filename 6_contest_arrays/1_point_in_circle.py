from math import sqrt

X, Y, R = map(str, input().split())
X, Y, R = int(X), int(Y), int(R)

print("YES" if R > sqrt(X ** 2 + Y ** 2) else "NO")


# Не работает, когда 3 числа в одной строке
# for i in range(3):
#     item = int(input("введите X Y R"))
#     A.append(item)