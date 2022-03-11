from collections import deque

def solution(priorities, location):
    answer = []
    queue = deque()
    for i, priority in enumerate(priorities):
        queue.append([i, priority])

    loc = queue[location]

    while queue:
        doc, prior = queue.popleft()
        if len(queue) == 0:
            answer.append([doc, prior])
        elif queue and prior >= max((map(lambda x:x[1], list(queue)))):
            answer.append([doc, prior])
        else:
            queue.append([doc, prior])

    return answer.index(loc)+1
