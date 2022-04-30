def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]: 
            j = stack.pop()
            answer[j] = i-j
        stack.append(i)
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - j - 1
    return answer
            
            
# 다른풀이
def solution(prices):
    answer = []
    for i in range(len(prices)):
        t = 0
        for j in range(i+1, len(prices)):
            t+=1
            if prices[j] < prices[i]:
                break
        answer.append(t)
        
    return answer
                
