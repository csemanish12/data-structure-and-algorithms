def reverse_array(left_index, array, array_size):
    right_index = array_size - left_index - 1

    if left_index >= right_index:
        return

    array[left_index], array[right_index] = array[right_index], array[left_index]
    reverse_array(left_index + 1, array, array_size)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print("before reversal:", numbers)
    reverse_array(0, numbers, len(numbers))
    print("after reversal:", numbers)


