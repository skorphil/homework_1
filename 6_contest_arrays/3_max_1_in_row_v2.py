list_len = int(input())
row = 0
top = 0

# collect all numbers in array
for i in range(list_len):
    input_n = int(input())
    if input_n == 1:
        row += 1
    else:
        if row > top:
            top = row
            row = 0
        if row <= top:
            row = 0

if row > top:
    top = row

print(top)
