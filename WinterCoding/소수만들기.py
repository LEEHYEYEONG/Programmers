from itertools import combinations

def solution(nums):
	answer = 0
	number_list = []
	for i in combinations(nums,3):
		number_list.append(list(i))
    
	for i in range(len(number_list)):
		prime = 0
		for j in range(2, sum(number_list[i])):
			if (sum(number_list[i]) % j) == 0:
				prime = 1
		if prime == 0:
			answer += 1     

	return answer