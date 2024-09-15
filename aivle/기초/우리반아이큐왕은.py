import sys 

n = int(sys.stdin.readline()) 
iq_list = []

for i in range(n):
    name, iq = map(str, sys.stdin.readline().split())
    iq_list.append([name, int(iq)])

iq_list.sort(key = lambda x:-x[1])

for i in range(3):
    print(iq_list[i][0])