import sys 

n, a = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if num_list[i] == a:
        print(i+1)
        break
else:
    print(-1)