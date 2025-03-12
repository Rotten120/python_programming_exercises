import get_input

if __name__ == "__main__":
    arr_inp = get_input.floats_until_invalid()
    arr_inp.sort()
    print("Sorted array:", arr_inp)
