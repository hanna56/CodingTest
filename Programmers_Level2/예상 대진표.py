def solution(n,a,b):
    answer = 1
    while True:
        if min(a,b) % 2 == 1 and abs(a-b) == 1:
            break
        a = (a+1) // 2
        b = (b+1) // 2
        answer+=1

    return answer
