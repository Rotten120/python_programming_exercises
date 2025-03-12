import get_input

def count_even(arr):
    even_count = 0
    for num in arr:
        if num & 1 == 0:
            even_count += 1
    return even_count

if __name__ == "__main__":
    arr_inp = get_input.numbers(10)
    print("There are", count_odd(arr_inp), "even numbers")
