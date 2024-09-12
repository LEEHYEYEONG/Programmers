import sys 

a = int(sys.stdin.readline()) 

print(a % 5 if a % 5 >= a % 7 else a % 7)