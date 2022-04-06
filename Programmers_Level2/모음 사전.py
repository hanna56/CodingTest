from itertools import product
def solution(word):
    lst = []
    for i in range(1,6):
        lst.extend(list(map(list, (product(['A','E','I','O','U'],repeat=i)))))
    lst.sort()
    return lst.index(list(word))+1
    
