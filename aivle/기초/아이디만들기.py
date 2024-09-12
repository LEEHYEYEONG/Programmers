import sys 

id = sys.stdin.readline().strip()

print("I" if len(id)>20 else "P")