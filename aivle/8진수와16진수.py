import sys 

alph = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F"}
a = int(sys.stdin.readline()) 
b = a

eight = ''
sixteen = ''

while(a>0):
    eight += str(a % 8)
    a //=8

while(b>0):
    tmp = b % 16
    if(tmp >= 10):
        tmp = alph[tmp%10]
    sixteen += str(tmp)
    b //= 16
        
print(eight[::-1], end=" ")
print(sixteen[::-1])

# oct, hex 함수 사용
print(oct(a)[2:], hex(a)[2:].upper())