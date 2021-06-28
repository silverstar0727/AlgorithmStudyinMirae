n = int(input())

l = []
left = n
right = n
for i in range(n):
    l.append(int(input()))
    
for i in range(n):
    for j in range(i):
        if l[j] >= l[i]:
            left -= 1
            break
    for k in range(i+1, n):
        if l[k] >= l[i]:
            right -= 1
            break

print(left)
print(right)