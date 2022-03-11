from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    
    queue.append([-numbers[0], 1])
    queue.append([+numbers[0], 1])
    
    while queue:
        num, count = queue.popleft()
        if count == len(numbers):
            if num == target:
                answer+=1
        else:
            queue.append([num-numbers[count], count+1])
            queue.append([num+numbers[count], count+1])        
    
    return answer
