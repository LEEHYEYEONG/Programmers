import math

def solution(n):
    sqrt_x = math.sqrt(n)
    return int((sqrt_x+1)**2) if sqrt_x== int(sqrt_x) else -1
