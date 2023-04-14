from itertools import permutations

# 소수를 판별
def sosu(x):
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
   
# 순열 수 조합 모두 만들기 
def solution(numbers):
    answer = 0
    num = []
    for i in range(1,len(numbers)+1):
        num.append(list(set(map("".join,permutations(numbers,i)))))
    per = list(set(map(int, set(sum(num, [])))))
        
    for p in per :
        if sosu(p) == True :
            answer += 1

    return answer