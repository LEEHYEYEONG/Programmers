import sys 

n = int(sys.stdin.readline()) 

def fib(n):
    a,b = 1,1
    if n==1 or n==2:
        return 1
        
    for i in range(1,n):
        a,b = b, a+b

    return a

print(fib(n+1)%796796)