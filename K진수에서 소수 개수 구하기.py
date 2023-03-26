def solution(n, k):
    # 진법 변환
    word = ""
    while n:
        word = str(n%k) + word
        n = n//k
    # 변환된 숫자를 0을 기준으로 분할
    word = word.split("0")
    count = 0
    for w in word:
        if len(w) == 0:
            continue
        if int(w) < 2:
            continue
        sosu = True
        # 소수를 찾는다
        for i in range(2,int(int(w)**0.5 + 1)):
            if int(w) % i == 0:
                sosu = False
                break
        if sosu == True:
            count += 1
        
    return count