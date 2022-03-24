def solution(n):
    result = 1
    for i in range(1, (n+1)//2):
        temp = 0
        for j in range(i, (n+3)//2):
            temp+=j
            if temp == n:
                result+=1
                break
            elif temp > n:
                break
            
    return result
