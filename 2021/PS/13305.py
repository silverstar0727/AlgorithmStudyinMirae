N = int(input())
edge = list(map(int, input().split()))
node = list(map(int, input().split()))

ans = 0
i = 0
while(i < N-1):
    price = node[i]
    length = 0
    sub_sum = 0
    for j in range(i+1, N):
        length += edge[j-1]
        if price > node[j] or j == N-1: # 2번재 케이스가 안맞아서 j == N - 1을 추가
            sub_sum = length * price
            break
    ans += sub_sum
    i = j

print(ans)

# 핵심 아이디어는 현재 수보다 작은수가 나올때까지 거리를 모두 더하기