def solution(food):
    first = ''
    end = ''
    for i in range(1,len(food)):
        if int(food[i]) > 1:
            first = first+str(i)*(int(food[i])//2)
            end = str(i)*(int(food[i])//2) + end
    return first + '0' + end