def solution(n):
    num = bin(n)[2:].count("1")
    answer = n + 1
    while True:
        if num == (bin(answer)[2:].count("1")):
            return answer
        else:
            answer += 1 

print(solution(78))
print(solution(15))