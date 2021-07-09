import sys

n = int(sys.stdin.readline())
candidate = []
for i in range(3):
    candidate.append(list(map(int, sys.stdin.readline().split())))

R, G, B = [candidate[0][0]], [candidate[0][1]], [candidate[0][2]]

for i in range(1, n):
    R.append(min(G[i-1], B[i-1]) + candidate[i][0])
    G.append(min(R[i-1], B[i-1]) + candidate[i][1])
    B.append(min(R[i-1], G[i-1]) + candidate[i][2])

print(min(R[-1], G[-1], B[-1]))

# 핵심은 dp