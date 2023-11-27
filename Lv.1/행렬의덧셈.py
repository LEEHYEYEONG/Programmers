def solution(arr1, arr2):
    answer = [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[i]))] for i in range(len(arr1))]
    return answer

# def solution(arr1, arr2):
#     answer = [[c + d for c, d in zip(a,b)] for a, b in zip(arr1, arr2)]
#     return answer

print(solution(arr1=[[1,2],[2,3]], arr2=[[3,4],[5,6]]))