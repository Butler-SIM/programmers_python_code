
from itertools import combinations as cb

def solution(nums):

    answer = 0
    for i in cb(nums, 3):
        cand = sum(i)
        for j in range(2, cand):
            if cand % j==0:
                break
        else:
            answer += 1
    return answer




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution(3,5)