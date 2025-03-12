import get_input

def quo(num1, num2):
    return num1 / num2

if __name__ == "__main__":
    arr_inp = get_input.numbers()
    print("Quotient is:", quo(arr_inp[0], arr_inp[1]))
