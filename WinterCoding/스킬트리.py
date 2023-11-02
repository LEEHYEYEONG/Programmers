def solution(skill, skill_trees):
    skill = list(skill)
    answer = 0
    
    for i in range(len(skill_trees)):
        order_list = []
        for j in range(len(skill_trees[i])):
            if(skill_trees[i][j] in skill):
                order_list.append(skill_trees[i][j])
        
        if(len(skill) == len(order_list)):
            if(skill == order_list):
                answer+=1
        else:
            check = True
            for j in range(len(order_list)):
                if(skill[j] != order_list[j]):
                    check = False
                    break
            if(check):
                answer += 1
    
    return answer

# def solution(skill, skill_trees):
#     answer = 0

#     for skills in skill_trees:
#         skill_list = list(skill)

#         for s in skills:
#             if s in skill:
#                 if s != skill_list.pop(0):
#                     break
#         else:
#             answer += 1

#     return answer

# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))