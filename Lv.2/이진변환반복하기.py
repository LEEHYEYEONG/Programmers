def solution(s):
    # 이진 변환 횟수
    bin_count = 0
    # 제거된 0의 개수
    zero_count = 0

    while(s != "1"):
        bin_count += 1
        # s 배열의 요소로 변환
        s = list(s) 

        # 0제거하기 전 s의 길이
        tmp = len(s)

        # 0제거
        s = [s[i] for i in range(len(s)) if s[i] == '1']

        zero_count += tmp - len(s)

        n = len(s) # c
        s = bin(n)[2:] # 앞에 "0b" 문자열 제거 
    
    answer = [bin_count, zero_count]

    return answer

print(solution("1111111"))

# 다른 풀이
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]