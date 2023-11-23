def solution(numbers):
    not_match = [i for i in range(10) if i not in numbers]
    return sum(not_match)

# solution = lambda x: sum(range(10)) - sum(x)

# def solution(numbers):
#     return 45 - sum(numbers)

print(solution([5,8,4,0,6,7,9]))