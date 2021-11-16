from collections import Counter
def solution(str1, str2):
    lst = []
    str1 = str1.lower()
    str2 = str2.lower()
    for s in (str1,str2):
        lst.append([s[i:i+2] for i in range(len(s)-1) if s[i:i+2].isalpha() ])

    interlst = sum((Counter(lst[0])&Counter(lst[1])).values())           
    sumlst = sum((Counter(lst[0])|Counter(lst[1])).values()) 
    
    if sumlst == 0 :
        answer = 65536
    else :
        answer = int((interlst/sumlst)*65536)
    return answer
