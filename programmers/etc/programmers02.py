
from itertools import combinations as cb

def solution(skill,skill_tree):
    answer=0
    for i in skill_tree:
        skillist=''
        for z in i:
            if z in skill:
                skillist+=z
        if skillist==skill[0:len(skillist)]:
            answer+=1
    return answer




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution('CBD',["BACDE", "CBADF", "AECB", "BDA"])