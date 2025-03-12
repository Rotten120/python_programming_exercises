import get_input

def get_mode(arr):
    num_list = []
    num_count = []
    
    for num in arr:
        if num not in num_list:
            num_list += [num]
            num_count += [1]
        else:
            idx = num_list.index(num)
            num_count[idx] += 1

    max_num_count = 0
    max_num_count_idx = 0
    
    for idx, num in enumerate(num_count):
        if max_num_count < num:
            max_num_count_idx = idx
            temp = max_num_count
            max_num_count = num
            num = temp
            
    return num_list[max_num_count_idx]

if __name__ == "__main__":
    arr_inp = get_input.nums_until_invalid()
    print("The Mode is:", get_mode(arr_inp))
