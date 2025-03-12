import get_input

if __name__ == "__main__":
    arr_inp = get_input.nums_until_invalid()
    arr_inp.sort(reverse=True)
    print("Sorted array:", arr_inp)
