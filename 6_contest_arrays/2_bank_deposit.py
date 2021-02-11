import math

input_numbers = []

years = 0

init_deposit, percent, target = map(str, input().split())
init_deposit, percent, target = int(init_deposit), int(percent), int(target)

# for i in range(3):
#     input_numbers.append(int(input()))

deposit = init_deposit

while deposit < target:
    # deposit += init_deposit * (percent / 100)
    deposit += deposit * (percent / 100)
    # Seems like correct way of calculating, but some tests not working
    years += 1
    deposit = float("{:.2f}".format(deposit))
    # print(deposit) for debug
else:
    print(years)