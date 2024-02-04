from collections import deque
def solution(n, m, section):
    answer = 0
    section = deque(section)
    if m == 1:
        answer = len(section)
    elif max(section)-min(section)+1 <= m:
        answer = 1
    else:
        while section:
            start = section.popleft()
            while section and start + m > section[0]:
                section.popleft()
            answer += 1
    return answer