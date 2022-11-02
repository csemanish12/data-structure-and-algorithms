def get_nth_fibonacci_number(n):
    if n <= 1:
        return n

    return get_nth_fibonacci_number(n-1) + get_nth_fibonacci_number(n-2)


if __name__ == '__main__':
    n = 0
    print(f"{n}th fibonacci number is {get_nth_fibonacci_number(n)}")