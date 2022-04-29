import heapq
def solution(operations):
    min_heap = []
    max_heap = []
    for op in operations:
        if op[0] == "I":
            heapq.heappush(min_heap, int(op[2:]))
            heapq.heappush(max_heap, (-1) * int(op[2:]))
        if min_heap and op[0] == "D":
            if op[2] == "-":
                num = heapq.heappop(min_heap)
                max_heap.remove((-1)*num)
            else:
                num2 = heapq.heappop(max_heap)
                min_heap.remove((-1)*num2)

    if not min_heap:
        return [0,0]
    else:
        return [max(min_heap), min(min_heap)]
