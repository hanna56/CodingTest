from itertools import permutations
def solution(k, dungeons):
    for i in range(len(dungeons), 0, -1):
        for dungeon_perm in permutations(dungeons, i):
            rate = k
            check = 0
            for dungeon in dungeon_perm:
                if dungeon[0] <= rate:
                    rate-=dungeon[1]
                else:
                    check = 1
                    break
            if check == 0:
                return i
