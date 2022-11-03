def print_all_permutation(index, array):
    if index == len(array):
        print(array)
        return

    for i in range(index, len(array)):
        array[index], array[i] = array[i], array[index]
        print_all_permutation(index+1, array)
        array[index], array[i] = array[i], array[index]


if __name__ == '__main__':
    array = [1, 2, 3]
    print_all_permutation(0, array)


