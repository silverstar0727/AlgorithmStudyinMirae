n = int(input())
arr = list(map(int, input().split()))
m = int(input())
num_list = list(map(int, input().split()))
for i in range(m):
    if num_list[i] in arr:
        print(1)
    else:
        print(0)