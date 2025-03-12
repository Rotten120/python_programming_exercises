import get_input

def sums(arr):
    total = 0
    for num in arr:
        total += num
    return total

if __name__ == "__main__":
    print("Sum is:", sums(get_input.numbers(10)))
