def solution(s):
    s = s.split(" ")
    answer = []
    for i in range(len(s)):
        word = "".join([s[i][j].upper() if(j == 0 and s[i][0].isalpha()) else s[i][j].lower() for j in range(len(s[i]))])
        answer.append(word)
    
    return " ".join(answer)

def solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])

print(solution("3people unFollowed me"))