import math
from collections import Counter
def solution(str1, str2):
    l_1 = []
    l_2 = []
    str1 = str1.upper()
    str2 = str2.upper()
    for i in range(0,len(str1)):
        if str1[i:i+2].isalpha() == True and len(str1[i:i+2]) == 2:
            l_1.append(str1[i:i+2])
    for i in range(0,len(str2)):
        if str2[i:i+2].isalpha() == True and len(str2[i:i+2]) == 2:
            l_2.append(str2[i:i+2])
            
    Counter1 = Counter(l_1)
    Counter2 = Counter(l_2)
    
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)