import get_input

def dif(num1, num2):
    return num1 - num2

if __name__ == "__main__":
    arr_inp = get_input.numbers()
    print("Difference is:", dif(arr_inp[0], arr_inp[1]))
