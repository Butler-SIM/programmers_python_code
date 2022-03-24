from string import ascii_uppercase

#구름 오늘의 업무
def solution():
    #5 3
    #BA
    #DA
    #BD

    #result BDCAE
    user_input = input()
    input_split = user_input.split(" ",2)
    result = ''
    alpha_list = list(ascii_uppercase)

    if input_split[1] != '0':
        pass
    else:
        for i in range(int(input_split[0])):
            result += alpha_list[i]

    return result




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution())

