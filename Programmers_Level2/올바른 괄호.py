def solution(s):
    stack = []
    for k in s:
        if k == "(":
            stack.append(k)
        else:
            if stack:
                stack.pop()
            else:
                return False

    return False if stack else True
                
