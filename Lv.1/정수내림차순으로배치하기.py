def solution(n):
    num_list = [i for i in str(n)]
    num_list.sort(reverse=True)
    answer = int("".join(num_list))
    return answer