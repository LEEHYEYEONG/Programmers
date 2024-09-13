import sys 

a, b, c = map(int,sys.stdin.readline().split()) 

print("P" if (a+b+c) == 180 and (a>0 and b>0 and c>0) else "F")