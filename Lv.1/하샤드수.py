def solution(x):
    x_sum = sum(map(int, str(x)))
    return x % x_sum == 0