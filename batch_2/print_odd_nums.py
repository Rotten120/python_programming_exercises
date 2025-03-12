def print_odd(start = 0, stop = 100):
    count = start
    while count <= stop:
        if count & 1 == 1:
            print(count)
        count += 1

if __name__ == "__main__":
    print_odd()
