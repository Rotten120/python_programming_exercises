import get_input

def is_not_equal(num1, num2):
    if num1 != num2: print("Not Equal")

if __name__ == "__main__":
    arr_inp = get_input.numbers()
    is_not_equal(arr_inp[0], arr_inp[1])
