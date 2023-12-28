def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin_arr1 = format(arr1[i], 'b').zfill(n)
        bin_arr2 = format(arr2[i], 'b').zfill(n)
        str = ''
        for j in range(n):
            if(bin_arr1[j] == bin_arr2[j] == '0'):
                str += ' '
            else:
                str += '#'
        answer.append(str)
    return answer

print(solution(n=5, arr1=[9, 20, 28, 18, 11], arr2=	[30, 1, 21, 17, 28]))