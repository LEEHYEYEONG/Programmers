import sys 

n = int(sys.stdin.readline())

apt = []
distance = [[] for i in range(n)]
answer = 0

# 아파트 단지 입력
for i in range(n):
    d, a = map(int, sys.stdin.readline().split())
    apt.append([d, a])

min_distance = sys.maxsize

for i in range(n):
    now = apt[i][0]
    for j in range(n):
        now_distance = abs(now-apt[j][0])*apt[j][1]
        distance[i].append(now_distance)
    min_distance = min(min_distance, sum(distance[i]))
    if(min_distance == sum(distance[i])):
        answer = i

print(answer+1)