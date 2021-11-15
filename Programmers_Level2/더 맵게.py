import heapq

def solution(scoville, K):
    num = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) >=2:
            min1 = heapq.heappop(scoville)
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1+2*min2)
            num+=1
        else:
            return -1
        
    return num
