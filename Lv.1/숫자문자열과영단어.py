def solution(s):
    result = ""
    # 숫자로만 이루어져 있는지 먼저 확인
    if(s.isdigit()):
        return int(s)
    num_dict = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    # 리스트로 변환
    s = list(s)
    print(s)
    
    while(s):
        while(len(s) > 0 and s[0].isdigit()):
            print(s)
            result += s[0]
            s.pop(0)

        word = ""
        while(len(s) > 0 and word not in num_dict):
            word += s[0]
            s.pop(0)
        if(word != ""):
            result += num_dict[word]
    
    return int(result)

def solution(s):
    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)

print(solution("123"))