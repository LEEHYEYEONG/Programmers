def solution(a, b, n):
    cola = 0
    while(n >= a):
        cola += (n // a) * b
        n = (n//a) * b + n % a

    return cola

print(solution(a = 3, b = 2, n = 10))