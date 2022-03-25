def solution():


    arr = ['20','30','10','50','40']
    arr= list(map(int,arr))
    count = 0

    arr.sort()

    print("arr sort :", arr)
    for i in range(1,len(arr)):
        #100 100 200 200
        if arr[i-1] == arr[i] :
            for j in range(1,len(arr)):
                if arr[i-1] < arr[j] :
                    count += 1
                    break
        elif arr[i-1] != arr[i]:

            count += 1

    return count





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution())

