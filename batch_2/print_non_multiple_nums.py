def print_non_multiples(start = 0, stop = 100, multiple = 5):
    for num in range(start, stop + 1):
        if not(num % multiple == 0):
            print(num)

if __name__ == "__main__":
    print_non_multiples()
