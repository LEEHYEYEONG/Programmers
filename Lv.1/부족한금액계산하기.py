def solution(price, money, count):
    init_price = price
    for i in range(1, count+1):
        price = init_price * i
        money -= price

    if(money < 0):
        return -money
    
    return 0

# 등차수열을 이용한 코드 
# def solution(price, money, count):
#     total = (price * (1+count) * count / 2)
#     return total - money if total > money else 0

# 음수일 경우 -> 절댓값 반환, 양수일 경우 0
# def solution(price, money, count):
#     return abs(min(money - sum([price*i for i in range(1,count+1)]),0))

# def solution(price, money, count):
#     return max(0,price*(count+1)*count//2-money)

print(solution(price=3, money=20, count=4))