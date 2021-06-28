n, k = map(int, input().split())

arr = [i for i in range(2, n+1)]
count = 0
while True:
    minimum = min(arr)
    for j in range(1, (n//minimum) + 1):
        if minimum*j in arr:
            count += 1
            if count == k:
                print(minimum*j)
                exit()
            arr.remove(minimum*j)