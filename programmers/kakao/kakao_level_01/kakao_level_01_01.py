# 프로그래머스 level_01 카카오 테스트 - 신규 아이디 추천

# 카카오에 입사한 신입 개발자 네오는 "카카오계정개발팀"에 배치되어,
# 카카오 서비스에 가입하는 유저들의 아이디를 생성하는 업무를 담당하게 되었습니다.
# "네오"에게 주어진 첫 업무는 새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때,
# 입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발하는 것입니다.
# 다음은 카카오 아이디의 규칙입니다.
#
# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.


import re


def solution():

    new_id = '...!@BaT#*..y.abcdefghijklm'
    answer = ''

    answer = re.sub('[^a-z\d\-\_\.]', '', new_id.lower())

    answer = re.sub('\.\.+', '.', answer)

    answer = re.sub('^\.|\.$', '', answer)

    if answer == '':
        answer = 'a'

    answer = re.sub('\.$', '', answer[0:15])

    while len(answer) < 3:
        answer += answer[-1:]

    print(answer)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution()

