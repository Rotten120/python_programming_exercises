def numbers(arr_size = 2):
    arr_input = []
    print("Input", arr_size, "numbers")
    print("Float numbers are rounded")
    for idx in range(arr_size):
        try:
            inp_num = [int(input("Enter number: "))]
            arr_input += inp_num
        except:
            continue
    return arr_input

def floats_until_invalid():
    arr_input = []
    print("Input numbers")
    print("Invalid inputs stops inputting process")
    while True:
        try:
            inp_num = [float(input("Enter number: "))]
            arr_input += inp_num
        except:
            break
    return arr_input
