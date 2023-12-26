def solution(s):
    word_dict = {}
    answer = []

    for i in range(len(s)):
        # s[i]가 키 값으로 존재하지 않는다면 정답 배열에 -1 추가
        if s[i] not in word_dict:
            answer.append(-1)
        # 존재한다면 현재 인덱스에서 딕셔너리 키 값을 빼기 
        else:
            answer.append(i - word_dict[s[i]])

        # 현재 인덱스를 딕셔너리 value로 저장
        word_dict[s[i]] = i

    return answer

print(solution("foobar"))