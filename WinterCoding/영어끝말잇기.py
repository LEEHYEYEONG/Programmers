def solution(n, words):
    word_list = [[] for _ in range(n)]
    for i in range(len(words)):
        for j in range(n):
            print(len(word_list[j-1])+1)
            if(((i > 0) and (words[i-1][-1] != words[i][0])) or (words[i] in word_list[j])):
                # 반례 찾으면 추가 
                #return [i%n + 1, len(word_list[j-1])+1]
                return [i%n + 1, i//n + 1]
        word_list[i%n].append(words[i])
    return [0, 0]
