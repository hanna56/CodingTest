import math

def solution(brown, yellow):
    total = brown+yellow
    for width in range(3, int(math.sqrt(total))+1):
        if total%width == 0:
            length = total//width
            if 2*(length-2)+2*width == brown and (length-2)*(width-2) == yellow:
                return [length, width]
