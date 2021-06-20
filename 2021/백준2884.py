h, m = map(int, input().split())
if h == 0 and m < 45:
    h = 24

remainder = m - 45
if remainder < 0:
    h -= 1
    m = 60 + remainder
else:
    m = remainder

print(h, m)