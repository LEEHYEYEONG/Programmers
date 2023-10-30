# def solution(dirs):
#     dirs = list(dirs.strip(' /" '))

#     point = [0, 0]
#     point_list = []
#     point_same_list = []

#     def up():
#         if(point[1] < 5):
#             point[1] += 1
#             point_list.append([point[0], point[1]])

#     def down():
#         if(point[1] > -5):
#             point[1] -= 1
#             point_list.append([point[0], point[1]])

#     def right():
#         if(point[0] < 5):
#             point[0] += 1
#             point_list.append([point[0], point[1]])

#     def left():
#         if(point[0] > -5):
#             point[0] -= 1
#             point_list.append([point[0], point[1]])

#     for i in dirs:
#         if(i == "U"):
#             up()
#         if(i == "D"):
#             down()
#         if(i == "R"):
#             right()
#         if(i == "L"):
#             left()

#     print(point_list)

#     for i in range(len(point_list)):
#         point_xy = []
#         if(i != len(point_list) - 1):
#             point_xy.extend(point_list[i])
#             point_xy.extend(point_list[i+1])
#             if point_xy not in point_same_list:
#                 point_same_list.append(point_xy)
#     print(point_same_list)
#     return len(point_same_list) + 1

def solution(dirs):
    answer = 0
    x = 5
    y = 5
    
    s = set()
    move = {'U':(0,-1),'D':(0,1),'R':(1,0),'L':(-1,0)}
    for i in range(len(dirs)):
        (dy,dx) = move[dirs[i]]
        if not (0 <= x+dx and x+dx <=10 and 0<=y+dy and y+dy<=10):
            continue
        s.add((x,y,x+dx,y+dy))
        s.add((x+dx,y+dy,x,y))
        x = x + dx
        y = y + dy
    answer=len(s)//2

    return answer