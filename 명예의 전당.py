
def solution(k, score_list):
    answer = []
    
    top = []
    
    for score in score_list:
        top.append(score)
        top = sorted(top, reverse=True)[:k]     
        answer.append(min(top))
    return answer