def solution(skill, skill_trees):
    answer = len(skill_trees)
    skill = skill[::-1]
    for tree in skill_trees:
        check_ = False
        for i in range(len(skill)):
            if check_ == True:
                break
            s = skill[i]
            if s in tree:
                for j in skill[i+1:]:
                    if j not in tree[:tree.index(s)]:
                        answer -= 1
                        check_ = True
                        break

    return answer

    
    
