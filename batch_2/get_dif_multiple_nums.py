import get_input

def difs(arr):
    remaining = 2 * arr[0]
    for num in arr:
        remaining -= num
    return remaining

if __name__ == "__main__":
    arr_inp = get_input.numbers(10)
    print("What remains of the first number is:", difs(arr_inp))
