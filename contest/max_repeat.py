series = []

while True:
    n = int(input())
    if n != 0:
        series.append(n)
    else:
        break
max_n = max(series)
print(series.count(max_n))
