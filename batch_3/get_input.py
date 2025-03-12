def numbers(arr_size = 2):
    arr_input = []
    for idx in range(arr_size):
        try:
            inp_num = [int(input("Enter number: "))]
            arr_input += inp_num
        except:
            continue
    return arr_input

def floats_until_invalid():
    arr_input = []
    while True:
        try:
            inp_num = [float(input("Enter number: "))]
            arr_input += inp_num
        except:
            break
    return arr_input
