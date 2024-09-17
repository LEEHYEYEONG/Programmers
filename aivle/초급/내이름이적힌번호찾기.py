import sys 

n, name = map(str, sys.stdin.readline().split())
student = list(map(str, sys.stdin.readline().split()))

for i in range(int(n)):
    if name == student[i]:
        print(i+1)
        break