import sys 
import math

a = int(sys.stdin.readline()) 

answer = 0

def prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    
    return True

for i in range(2, a+1):
    if prime(i):
        answer += 1

print(answer)