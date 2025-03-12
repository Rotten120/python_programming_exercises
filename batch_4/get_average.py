import get_input

def get_average(arr):
    total = 0
    for num in arr:
        total += num
    return total / len(arr)

if __name__ == "__main__":
    arr_inp = get_input.nums_until_invalid()
    print("Average is:", get_average(arr_inp))
