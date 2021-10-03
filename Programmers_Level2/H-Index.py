import numpy as np

def solution(citations):
    for i in range(len(citations), -1, -1):
        if sum(np.array(citations) >= i) >= i:   
            return i
