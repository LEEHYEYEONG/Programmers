# n_list = [2**i for i in range(31)] 

# def add(x):
#     return x+1

# def solution(n):
#     ans = 1
#     result_list = [1, 2, 2, 3]
#     if(n == 1 or n in n_list):
#         ans = 1
#     elif(n == 3):
#         ans = 2
#     else:
#         for i in range(2, 31):
#             if(2**i < n < 2**(i+1)):
#                 result_i = i
#                 break
#         for i in range(3, result_i+2):
#             new_result_list = list(map(add, result_list))
#             result_list.extend(new_result_list)			
               
#         ans = result_list[n-2**result_i]

#     return ans

def solution(n):
    ans = 0
    if(n == 1):
        return ans + 1

    while (n != 0):
        if(n % 2 == 0):
            n = n//2
        else:
            n = (n-1) // 2
            ans += 1
   
    return ans
