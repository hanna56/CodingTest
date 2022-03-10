def solution(clothes):
    dict = {}
    for cloth in clothes:
        if cloth[1] in dict:
            dict[cloth[1]]+=1
        else:
            dict[cloth[1]]=1

    temp=1
    for i in dict:
        temp*=(dict[i]+1)
    return temp-1
