def solution(n, words):
    w = len(words)
    x=y=0
    arr=[words[0]]
    z=1
    for i in range(1, w):
        if (words[i] in arr) or (words[i-1][-1] != words[i][0]):
            x=(i%n)+1
            y=(i//n)+1
            break
        arr.append(words[i])
    return [x,y]
