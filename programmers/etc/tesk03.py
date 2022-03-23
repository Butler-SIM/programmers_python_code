from datetime import datetime


def solution():

    user_input = input()
    date_split = user_input.split(" ",2)
    date1 = datetime.strptime(date_split[0], "%Y%m%d")
    date2 = datetime.strptime(date_split[1], "%Y%m%d")

    result_date = date1 - date2

    if result_date.days < 0:
        print(abs(result_date.days))
        return abs(result_date.days)
    else:
        print(result_date.days)
        return result_date.days


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution())

