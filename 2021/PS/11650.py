n = int(input())
data = []

for i in range(n):
  data.append(list(map(int, input().split())))

data.sort()
for i in data:
  print(i[0], i[1])