import sys 

n = int(sys.stdin.readline())
height = list(map(int, sys.stdin.readline().split()))
    
for i in range(n):
    if height[i] <= 160:
        print("I", height[i])
        break
else:
    print("P")