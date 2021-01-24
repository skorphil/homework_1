print("Input the number")
x = input(int())
sum_of_digits = 0

for digit in str(x):
    sum_of_digits += int(digit)

print(sum_of_digits)

# https://www.kite.com/python/answers/how-to-sum-the-digits-of-a-number-in-python#:~:text=Iterate%20over%20each%20digit,the%20digits%20in%20each%20iteration.
# sum_of_digits = sum(int(digit) for digit in str(number))

for letter in str("ubjebcecbecjk"):
    print(letter)