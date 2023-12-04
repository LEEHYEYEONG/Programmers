import itertools

def solution(number):
    three_nums = list(itertools.combinations(number, 3))
    return len([three_nums[i] for i in range(len(three_nums)) if sum(three_nums[i]) == 0])

print(solution([-3, -2, -1, 0, 1, 2, 3]))