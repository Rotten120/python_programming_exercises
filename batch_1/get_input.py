def get_input(arr_size = 2):
    arr_input = []
    for idx in range(arr_size):
        try:
            inp_num = [float(input("Enter number: ")]
            arr_input = inp_num
        except:
            continue
    return arr_input
