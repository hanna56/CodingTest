def solution(n):
    i=1
    while True:
        k=n+i
        if sum(list(map(int, (bin(n)[2:])))) == sum(list(map(int, (bin(k)[2:])))):
            return k
        i+=1
