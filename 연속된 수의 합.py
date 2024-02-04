def solution(num, total):
    answer = []
    result = total/num
    if result.is_integer() == True:
        answer.append(result)
        again = int((num - 1)/2)
        for i in range(1,again + 1):
            answer.append(result + i)
            answer.append(result - i)         
    else:
        answer = [int(result), int(result) + 1]
        again = int((num - 2)/2)
        for i in range(1,again + 1):
            answer.append(int(result) + 1 + i)
            answer.append(int(result) - i)
    return sorted(answer)