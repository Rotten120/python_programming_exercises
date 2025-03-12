import get_input

def is_num_unique_or_dupli(arr):
    nums_in_arr = []
    duped_nums = []

    for num in arr:
        if num in nums_in_arr: duped_nums += [num]
        else: nums_in_arr += [num]

    for num in arr:
        num_identifier = "Duplicate" if num in duped_nums else "Unique"
        print(num, num_identifier)

if __name__ == "__main__":
    arr_inp = get_input.nums_until_invalid()
    print("\nResults")
    is_num_unique_or_dupli(arr_inp)
