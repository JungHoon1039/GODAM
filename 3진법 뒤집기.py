def solution(n):
    answer = 0
    lst = []
    while (n>0):
        lst.append(int(n%3))
        n = n//3
    for i in range(0,len(lst)): 
        answer += lst[i] * 3**(len(lst)-(i+1))
    return answer