import get_input

def count_odd(arr):
    odd_count = 0
    for num in arr:
        if num & 1 == 1:
            odd_count += 1
    return odd_count

if __name__ == "__main__":
    arr_inp = get_input.numbers(10)
    print("There are", count_odd(arr_inp), "odd numbers")
