def solution(s):
    # s = s.split()
    s = list(map(int,s.split()))
    # min_num = str(min([int(i) for i in s]))
    # max_num = str(max([int(i) for i in s]))
    # answer = " ".join([min_num, max_num])
    # return answer
    return str(min(s)) + " " + str(max(s))

print(solution("-1 -1"))