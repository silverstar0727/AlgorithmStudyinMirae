def print_max(arr):
    candidate = []
    candidate.append(abs(arr[0] - arr[1]))
    candidate.append(abs(arr[-1] - arr[-2]))

    n = len(arr)
    for i in range(n - 2):
        candidate.append(abs(arr[i] - arr[i+2]))

    print(max(candidate))

T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    print_max(arr)

# 핵심 아이디어는 작은 것 부터 양쪽 끝에서 i번째에 배치되는 배열이 우리가 찾는 배열이라는 것
# 그것이 '차'의 '최대'가 '최소'가 되는 경우