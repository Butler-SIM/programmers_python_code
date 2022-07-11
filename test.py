import random

win_number = [10, 14, 16, 18, 29, 35]
number_list = []



count = 0
while True:
    my_number = random.sample(range(1, 46), 6)
    my_number.sort()
    count += 1
    print("win_number : ", win_number)
    print("my_number : ", my_number)
    print("count", count)
    if win_number == my_number:
        print("break count : ", count)
        break