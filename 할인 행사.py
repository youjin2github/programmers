from collections import Counter
def solution(want, number, discount):
    # discount를 튜플 형식으로 변경
    first = {}
    answer = 0
    for w, n in zip(want, number):
        first[w] = n
    
    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        if c == first:
            answer += 1

    return answer