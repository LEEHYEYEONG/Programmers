def solution(s):
    if(len(s) != 4 and len(s) != 6):
        return False
    return s.isdigit()

# def solution(s):
#     return s.isdigit() and len(s) in [4,6]

print(solution("1234"))