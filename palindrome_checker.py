def palindrome_checker(left_index, array, array_size):
    right_index = array_size - left_index - 1

    if left_index >= right_index:
        return True

    if array[left_index] != array[right_index]:
        return False

    return palindrome_checker(left_index+1, array, array_size)


if __name__ == '__main__':
    array_string = "neven"
    is_palindrome = palindrome_checker(0, array_string, len(array_string))

    if is_palindrome:
        print(f"{array_string} is palindrome")
    else:
        print(f"{array_string} is not palindrome")