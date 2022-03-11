import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    complete = deque()
    for i, progress in enumerate(progresses):
        complete.append(math.ceil((100-progress)/speeds[i]))

    while complete:
        answer.append(1)
        num = complete.popleft()
        while complete and num >= complete[0]:
            answer[-1]+=1
            complete.popleft()

    return answer
