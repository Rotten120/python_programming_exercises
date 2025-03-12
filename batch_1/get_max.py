import get_input

def max(num1, num2):
    return num1 if num1 > num2 else num2

if __name__ == "__main__":
    arr_inp = get_input.numbers()
    print("Bigger number is", max(arr_inp[0], arr_inp[1]))
