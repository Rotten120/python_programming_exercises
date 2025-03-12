import get_input

def print_range(start, stop):
    for num in range(start, stop + 1):
        print(num)

if __name__ == "__main__":
    arr_inp = get_input.numbers()
    print_range(arr_inp[0], arr_inp[1])
