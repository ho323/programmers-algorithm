def solution(s):
    x=y=0
    l = list(s)
    while len(l) != 1:
        z=0
        for i in range(len(l)):
            if l[i] == '0':
                y+=1
            else:
                z+=1
        l = list(bin(z))[2:]
        x+=1
    return [x,y]
