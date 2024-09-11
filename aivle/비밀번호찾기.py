import sys 

a = sys.stdin.readline() 

password = ""

for i in range(len(a)):
    password += a[i]
    if(a[i]=='c'):
        break

print(password)