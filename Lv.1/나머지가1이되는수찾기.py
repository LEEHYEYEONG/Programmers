def solution(n):
    for i in range(1, n):
        if(n % i == 1):
            return i

# def solution(n):
#     return [x for x in range(1,n+1) if n%x==1][0]