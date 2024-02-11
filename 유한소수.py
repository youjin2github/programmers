def solution(a, b):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x
    
    g = gcd(a, b)
    b = b // g  

    while b % 2 == 0:
        b = b // 2
    
    while b % 5 == 0:
        b = b // 5
    
    if b == 1:
        return 1 
    else:
        return 2 