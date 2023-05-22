def solution(name, yearning, photo):
    answer = []
    for num in range(len(photo)):
        score = 0
        for i in range(len(photo[num])):
            for j in range(len(name)):
                if name[j] == photo[num][i]:
                    score += yearning[j]
        answer.append(score)