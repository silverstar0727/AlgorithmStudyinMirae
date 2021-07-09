N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key = lambda x:(x[1], x[0]))

ans = 0
start = 0

for time in arr:
    if(time[0] >= start):
        start = time[1]
        ans += 1
        
print(ans)