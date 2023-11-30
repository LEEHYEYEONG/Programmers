def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        answer.append(arr[i])
    return answer
    
def solution(arr):
    result = []
    for i in arr:
        if len(result) == 0 or result[-1] != i:
            result.append(i)

    return result

print(solution([4,4,4,3,3]))