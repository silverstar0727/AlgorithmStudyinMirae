n = int(input())

for i in range(n):
    ans = 0
    arr = list(input())
    for j in range(len(arr)):
        if ans < 0:
            print('NO')
            break
        if arr[j] == ')':
            ans -= 1
        else:
            ans += 1
        
        if j == len(arr)-1:
            if ans == 0:
                print('YES')
            else:
                print('NO')
            