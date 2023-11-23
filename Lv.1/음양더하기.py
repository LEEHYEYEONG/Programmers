# def solution(absolutes, signs):
#     num_dict = {absolutes[i]: signs[i] for i in range(len(signs))}
#     num_list = [-i if num_dict[i] == False else i for i in num_dict]
#     return sum(num_list)

# def solution(absolutes, signs):
#     answer = 0
#     for i in range(len(absolutes)):
#         if(not signs[i]):
#             answer -= absolutes[i]
#         else:
#             answer += absolutes[i]
#     return answer

def solution(absolutes, signs):
    answer = 0

    for value, positive in zip(absolutes, signs):
        answer += value if positive else -value

    return answer

print(solution(absolutes=[4,7,12], signs=[True,False,True]))