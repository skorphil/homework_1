series = []

while True:
    n = int(input())
    if n != 0:
        series.append(n)
    else:
        break
print(max(series))
