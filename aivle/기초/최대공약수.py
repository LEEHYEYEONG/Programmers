import sys 

a, b = map(int, sys.stdin.readline().split())

max_num = max(a, b)
answer = 1

for i in range(2, max_num//2):
    if(a%i == 0 and b%i == 0):
        answer = i
    
print(answer)

# 유클리드 호제법
def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

# 라이브러리 사용
import math
math.gcd(a, b)