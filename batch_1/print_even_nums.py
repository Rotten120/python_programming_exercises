def print_even(start = 0, stop = 100):
    for num in range(start, stop // 2 + 1):
        print(num * 2)

if __name__ == "__main__":
    print_even()
