# 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
#
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.

# n	   result
# 10	 4 [2,3,5,7,]
# 5	     3 [2,3,5]

def solution(n):
    answer = 0
    for i in range(2,n+2):
        print(i)
        for j in range(2,n+2):
            if i % j == 1 :


                answer += 1

            else:
                break




    print(answer)
    return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution(10)