import get_input

def min_arr(arr):
    lowest_num = arr[0]
    for num in arr:
        if lowest_num > num:
            temp = lowest_num
            lowest_num = num
            num = temp
    return lowest_num

if __name__ == "__main__":
    arr_inp = get_input.floats_until_invalid()
    print("Lowest number is:", min_arr(arr_inp))
