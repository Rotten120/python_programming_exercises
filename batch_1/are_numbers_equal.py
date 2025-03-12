import get_input

def is_equal(num1, num2):
    if num1 == num2: print("Equal")

if __name__ == "__main__":
    arr_inp = get_input.numbers()
    is_equal(arr_inp[0], arr_inp[1])
