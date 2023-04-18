def solution(s):
    l = list(map(int, s.split(' ')))
    answer = f'{min(l)} {max(l)}'
    return answer
