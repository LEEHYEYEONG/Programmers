# def solution(s):
#     num_list = [i for i in s]
#     str = False
#     if(num_list[0] == "-"):
#         str = True
#         del num_list[0]
#     elif(num_list[0] == "+"):
#         del num_list[0]

#     answer = int("".join(num_list))
#     return answer * -1 if str else answer

def solution(s):
    answer = int(s)
    #함수를 완성하세요
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution("-1234"));