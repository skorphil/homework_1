# import math

# print("Input number:")
# n = int(input())
# k = 1

# while k < math.log(n, 2):
#     k += 1
# else:
#     print(k)

n = int(input())
power = 2
k = 1

while power < n:
    k += 1
    power *= 2
else:
    print(k)

