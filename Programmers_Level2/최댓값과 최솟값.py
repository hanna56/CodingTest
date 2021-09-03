def solution(s):
    return " ".join([str(min(list(map(int, s.split(" "))))),str(max(list(map(int, s.split(" ")))))])
