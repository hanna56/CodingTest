def solution(n, computers):
    answer = 0
    visited = [0] * (n)
    
    def dfs(computer, i):
        for idx in range(len(computer)):
            if computer[idx] and not visited[idx]:
                visited[idx] = 1
                dfs(computers[idx], idx)
                
    for i in range(n):
        if not visited[i]:
            answer+=1
            visited[i] = 1
            dfs(computers[i], i)
    
    return answer
        
