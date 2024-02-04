def solution(l, r):
    answer = []
    for i in range(l, r+1):
        for j in str(i):
            if all(j) in ['0','5']:
                answer.append(i)
    return answer