def solution(A,B):
    result = 0
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        result += A[i] * B[i]
    
    return result 

def solution(A,B):
		return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])

print(solution(A=[1,2], B=[3,4]))