import get_input

def print_non_duped_nums(arr):
    nums_in_arr = []
    duped_nums = []
    non_duped_nums = []

    for num in arr:
        if num in nums_in_arr: duped_nums += [num]
        else: nums_in_arr += [num]

    for num in nums_in_arr:
        if num not in duped_nums:
            non_duped_nums += [num]

    print(non_duped_nums)

if __name__ == "__main__":
    arr_inp = get_input.floats_until_invalid()
    print("Numbers with no duplicates: ", end = '')
    print_non_duped_nums(arr_inp)
