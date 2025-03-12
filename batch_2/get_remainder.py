import get_input

def mod(num1, num2):
    return num1 % num2

if __name__ == "__main__":
    arr_inp = get_input.numbers()
    print("Remainder is:", mod(arr_inp[0], arr_inp[1]))
