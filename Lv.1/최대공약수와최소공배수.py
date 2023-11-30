import math

def solution(n, m):
    n, m = min(n, m), max(n, m)
    if(m % n == 0):
        return [n, m]
    
    max_division = max([i for i in range(1, n+1) if m % i == 0 and n % i == 0])
    min_multiple = n // max_division * m
    
    return [max_division, min_multiple]


def solution(n, m):
		return [math.gcd(n, m), n*m // math.gcd(n, m)]

print(solution(n=2, m=5))