from string import ascii_uppercase


def solution():

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

