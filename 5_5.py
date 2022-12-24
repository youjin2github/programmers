# 재귀함수 종료조건 만들기 
## ver1
def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
## ver2
def factorial_iterative1(n):
    if n <= 1:
        return 1
    return n*factorial_iterative1(n-1)

print(factorial_iterative(5))
print(factorial_iterative1(5))
