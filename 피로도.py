from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for per in permutations(dungeons, len(dungeons)):
        pk = k
        count = 0
        for pm in per:
            if pk >= pm[0]:
                count += 1
                pk -= pm[1]
        if count > answer:
            answer = count
    return answer