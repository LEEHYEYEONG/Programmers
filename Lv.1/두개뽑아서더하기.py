from itertools import combinations

def solution(numbers):
    answer = []
    two_nums = list(combinations(numbers,2))
    for i in two_nums:
        if(sum(i) not in answer):
            answer.append(sum(i))
    answer.sort()
    return answer

def solution(numbers):
    return sorted(set(sum(i) for i in list(combinations(numbers, 2))))

# combinations 사용하지 않고 
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))


print(solution([2,1,3,4,1]))