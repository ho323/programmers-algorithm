def solution(n):
    answer=a=0
    for i in range(1,n+1):
        a=0
        for j in range(i, n+1):
            a += j
            if a == n:
                answer+=1
                break
            elif a > n:
                break
    return answer
