import sys 

a, b, n = map(int, sys.stdin.readline().split())

day = 0
num = 0

while(num < n):
    num += a
    day += 1
    if n <= num:
        break
    num -= b

print(day)