def solution(s):
    s = s.split(" ")
    answer = []
    for i in range(len(s)):
        word = ''.join([s[i][j].upper() if j%2 == 0 else s[i][j].lower() for j in range(len(s[i]))])
        answer.append(word)
    
    return ' '.join(answer)

print(solution("  TRy HElLo  WORLD "))