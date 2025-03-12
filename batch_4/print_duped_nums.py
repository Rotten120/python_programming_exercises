import get_input

def print_duped_nums(arr):
    nums_in_arr = []
    duped_nums = []

    for num in arr:
        #there are also no multiple instances of
        #a single number in duped nums
        #i.e. [1, 1, 2] cant exist
        #num not in duped_nums manage that
        if num in nums_in_arr and num not in duped_nums:
            duped_nums += [num]
        elif num not in nums_in_arr:
            nums_in_arr += [num]

    print(duped_nums)

if __name__ == "__main__":
    arr_inp = get_input.numbers(10)
    print("Numbers with duplicates: ", end = '')
    print_duped_nums(arr_inp)
