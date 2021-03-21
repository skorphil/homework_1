def insert_sort(a):
    """insert sorting of a given list a"""
    N = len(a)
    for top in range(1, N):
        k = top
        while k > 0 and a[k - 1] > a[k]:
            a[k], a[k - 1] = a[k - 1], a[k]
            k -= 1


list_len = int(input())
number_list = []

# collect all numbers in array
for i in range(list_len):
    number_list.append(int(input()))

# count length of rows and append them in array
counter = 0
lengths = []

for i in number_list:
    if i == 1:
        counter += 1  # length of current row

    else:
        lengths.append(counter)  # store length of previos row (when 0 appears)
        counter = 0

lengths.append(
    counter
)  # store length of previos row (if the last number in a given list was 1)

# sort list of lengths
insert_sort(lengths)
# print the largest value in a list(longest row of 1)
print(lengths[len(lengths) - 1])
