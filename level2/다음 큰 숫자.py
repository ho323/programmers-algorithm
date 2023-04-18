def solution(n):
    answer = 0
    nc = bin(n).count('1')
    a=n+1
    while True:
        if bin(a).count('1') == nc:
            break
        a+=1
    return a
