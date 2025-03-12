import get_input

def pro(num1, num2):
    return num1 * num2

if __name__ == "__main__":
    arr_inp = get_input.numbers()
    print("Product is:", pro(arr_inp[0], arr_inp[1]))
