# def solution(s):
#     answer = s[len(s)//2 - 1]+s[len(s)//2] if len(s) % 2 == 0 else s[len(s)//2]
#     return answer 

def solution(s):
    return s[(len(s)-1)//2 : len(s)//2 + 1]

print(solution("abcde"))