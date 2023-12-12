def solution(s):
    if(s[0] == ')' or s[-1] == '('):
        return False
    left, right = 0, 0

    for i in range(len(s)):
        if(s[i] == '('):
            left+= 1
        else:
            right += 1

        if(left < right): 
            return False
    
    if(left != right):
        return False 

    return True

def solution(s):
    stack = []
    for i in s:
        # 스택이 비어있는데 닫힌괄호 들어오는 경우 False return
        if len(stack) == 0 and i == ')':
            return False

        # 스택 맨 위에 열린괄호 있는데 닫힌괄호 들어오는 경우: pop
        if i == ')' and stack[-1] == '(':
            stack.pop()

        # 열린 괄호 들어오는 경우 stack에 append
        if i == '(':
            stack.append('(')

    # 다 끝났는데 남아있으면 False return
    return False if len(stack) != 0 else True

def solution(s):
    wt = 0
    for c in s :
        if c == '(' : wt += 1
        elif c == ')' : wt -= 1
        if wt < 0 : return False
    return wt == 0

print(solution("())((()))(()"))