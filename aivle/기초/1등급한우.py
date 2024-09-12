import sys 

a = int(sys.stdin.readline()) 

print("A" if a>=200 else "B" if a>=180 else "C" if a>= 150 else "D")

if(a>=200):
    print("A")
elif(a>=180):
    print("B")
elif(a>=150):
    print("C")
else:
    print("D")