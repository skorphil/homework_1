print("Input number:")
n = int(input())
num = 1
root = 1

while n >= root:
    print(root, end="  ")
    num += 1
    root = num ** 2
