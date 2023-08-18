# bfs로 문제를 푼다 -> 일단 모듈부터 먼저 불러오기 
from collections import deque

# 시작, 끝, 전체     
def solution(begin, target, words):
    # 두개의 단어가 차이가 1개만 나는지 확인하기 
    ## 1이면 True 아니면 False
    def bfs(word1, word2):
        # 만약에 다르면 +1
        not_same = 0
        for w1, w2 in zip(word1, word2):
            if w1 != w2:
                not_same += 1
        return not_same == 1
    
    # 큐를 초기화하자 bfs는 큐
    queue = deque([(begin,0)])
    # 방문한 단어는 여기에 입력 
    visited = set()
    
    # 큐가 비어있을때까지 반복
    while queue:
        current, depth = queue.popleft()
        # 만약에 타겟이랑 똑같으면 정답 리턴
        if current == target:
            return depth
        # words에 있는 단어 하나하나 current랑 대조해보기 
        for word in words:
            if word not in visited and bfs(current, word) == True:
                visited.add(word)
                queue.append((word, depth + 1))
    # 암것도 없으면 0
    return 0