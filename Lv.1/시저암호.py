def add(el, n):
    # 대문자인 경우
    if(65<=ord(el) <= 90):
        if(ord(el) + n > 90):
            return chr(ord(el) + n - 26)
        return chr(ord(el) + n)
    # 소문자인 경우
    elif(97 <= ord(el) <= 122):
        if(ord(el) + n > 122):
            return chr(ord(el) + n - 26)
        return chr(ord(el) + n)
    # 공백인 경우
    elif(el == " "):
        return " "

def solution(s, n):
    s = list(s)
    result = []
    for i in s:
        result.append(add(i, n))
    
    return "".join(result) 

def solution(s, n):
    result = ""

    for i in s:
        if i == " ":
            result += " "
        elif i.islower():
            result += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        else:
            result += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
    
    return result

print(solution(s="ABCDEFGHIJKLMNOPQRSTUVWXYZ", n=25))