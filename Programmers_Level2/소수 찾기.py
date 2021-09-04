import math
from itertools import permutations

def is_prime(x):
    if x == 1 or x == 0:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        for perm in permutations(numbers, i):
            if int("".join(list(perm))) not in answer and is_prime(int("".join(list(perm)))):
                answer.append(int("".join(list(perm))))

    return len(answer)
