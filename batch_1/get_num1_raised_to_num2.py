import get_input

def exp(num1, num2):
	return num1 ** num2
	
if __name__ == "__main__":
	arr_inp = get_input.numbers()
	print(arr_inp[0], "raised to", arr_inp[1], "is equal to", exp(arr_inp[0], arr_inp[1]))