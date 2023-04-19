def solution(brown, yellow):
    a = brown + yellow
    x = (brown - 4) / 2
    
    ms = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            ms.append(i)
    y=[]
    if len(ms) == 1:
        y.append(1)
        y.append(1)
    else:
        for i in range(len(ms)):
            for j in range(len(ms)):
                if ms[i] + ms[j] == x and ms[i] * ms[j] == yellow:
                    print(ms[i], ms[j])
                    y.append(ms[i])
                    y.append(ms[j])
                    break
            if y:
                break
    print(y)
    answer = [y[1]+2, y[0]+2]
    
    return answer
