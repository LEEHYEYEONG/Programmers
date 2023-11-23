def solution(phone_number):
    hidden_number = phone_number.replace(phone_number[:-4], '*'*len(phone_number[:-4])) 
    return hidden_number

# def solution(phone_number):
#     return "*"*(len(phone_number)-4)+phone_number[-4:]

print(solution("027778888"))