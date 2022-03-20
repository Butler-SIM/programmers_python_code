def solution(str):
    n = len(str)

    if 'b' not in str:
        return True

    for i in range(n):
        if (str[i] != 'a'):
            break
    for j in range(i, n):
        if (str[j] != 'b'):
            return False

    return True





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution("aaa"))

