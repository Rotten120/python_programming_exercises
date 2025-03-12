import get_input

def min(num1, num2):
    return num1 if num1 < num2 else num2

if __name__ == "__main__":
    arr_inp = get_input.numbers()
    print("Smaller number is", min(arr_inp[0], arr_inp[1]))
