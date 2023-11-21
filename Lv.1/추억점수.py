# def solution(name, yearning, photo):
#     answer = []
#     yearning_dict = dict(zip(name,yearning))

#     for p in photo:
#         score=0
#         for name in p:
#             if name in yearning_dict:
#                 score += yearning_dict[name]
#         answer.append(score)
#     return answer

def solution(name, yearning, photo):
    answer = []
    name_dict = {}
    for i in range(len(name)):
        name_dict[name[i]] = yearning[i]
    for i in range(len(photo)):
        sum_point = 0
        for j in range(len(photo[i])):
            if(name_dict.get(photo[i][j])):
                sum_point += name_dict[photo[i][j]]
        answer.append(sum_point)
    return answer
