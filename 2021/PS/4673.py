arr = [i for i in range(1, 10001)]

for i in range(1, 10000):
    sum = i
    for j in (list(str(i))):
        sum += int(j)
    try:
        arr.remove(sum)
    except:
        continue

for i in arr:
    print(i)