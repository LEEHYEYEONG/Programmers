import sys 

money = int(sys.stdin.readline()) 

num = 0

coupon = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i in range(len(coupon)):
    num += (money // coupon[i])
    money = money % coupon[i]

print(num)