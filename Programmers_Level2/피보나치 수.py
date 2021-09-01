def solution(n):
    f_2 = 0 # F(0) = 0
    f_1 = 1 # F(1) = 1
    
    for _ in range(n-1):
        f_1, f_2 = f_2 + f_1, f_1
        
    return f_1 % 1234567
    
