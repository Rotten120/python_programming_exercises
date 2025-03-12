import get_input

def max_arr(arr):
    highest_num = arr[0]
    for num in arr:
        if highest_num < num:
            temp = lowest_num
            lowest_num = num
            num = temp
    return highest_num

if __name__ == "__main__":
    arr_inp = get_input.nums_until_invalid()
    print("Highest number is:", max_arr(arr_inp))
