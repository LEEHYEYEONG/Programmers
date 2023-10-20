def solution(d, budget):
	answer = 0
	d.sort()
	d_sum = 0

	for i in range(len(d)):
		if(d_sum + d[i] > budget):
			break
		d_sum += d[i]
		answer += 1
	return answer

# def solution(d, budget):
#     d.sort()
#     while budget < sum(d):
#         d.pop()
#     return len(d)