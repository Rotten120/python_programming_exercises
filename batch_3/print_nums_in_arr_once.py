import get_input

def print_nums_once(arr):
    nums_in_arr = []

    for num in arr:
        #checks if there are no duplicates
        #of num in nums_in_arr
        if num not in nums_in_arr:
            nums_in_arr += [num]
            
    print(nums_in_arr)
    
if __name__ == "__main__":
    arr_inp = get_input.floats_until_invalid()
    print("List of numbers inputted: ", end = '')
    print_nums_once(arr_inp)
