# 스택을 사용하기

# 만약에 스택이 (로 시작해서 )로 끝나면 pop을 해서 공란을 만들고, 전부 공란이면 true 아니면 false를 리턴
def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack == []:
                return False
            else:
                stack.pop()
                
    return stack == []