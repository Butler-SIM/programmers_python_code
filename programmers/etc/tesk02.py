def solution():
    print("count :")
    count_input = input()


    que = ''
    result =''
    for i in range(int(count_input)):
        print("check : ")
        check = input()
        if check == 'd' :
            if que == "":
                print("underflow")
                result += "underflow\n"
        elif check == 'e' :
            print("que_result :")
            que_result = input()
            que = que_result
            print(que)
            result += que+" "
            que = ''
    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution())

