n, k = map(int, input().split())

circle = [i for i in range(1, n+1)]
ans = []
target_idx = 0
while True:
    if len(circle) == 0:
        break
    target_idx = ((target_idx + k-1) % len(circle))
    target = circle[target_idx]
    ans.append(target)
    circle.remove(target)

print('<', end='')
for i in range(len(ans) - 1):
    print(ans[i], end=', ')
print(ans[-1], end='>')
