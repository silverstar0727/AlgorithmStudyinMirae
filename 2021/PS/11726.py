from math import factorial
n = int(input())

# 세로짝대기의 수 = a
# 가로짝대기의 수 = b
a = n
b = 0
ans = 0
while (a >= 0):
    ans += factorial(a + b) // (factorial(a) * factorial(b))
    a -= 2
    b += 1

print(ans%10007)