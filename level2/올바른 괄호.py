def solution(s):
    answer = True
    arr = []
    for i in range(len(s)):
        if s[0] == ')':
            answer = False
            break
        elif s[i] == '(':
            arr.append(s[i])
        elif s[i] == ')':
            if arr and arr[-1] == '(':
                arr.pop()
                            
    if arr:
        answer = False
    
    return answer
