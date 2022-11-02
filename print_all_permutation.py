def print_all_permutation(permutation, array, selected_index):
    if len(permutation) == len(array):
        print(permutation)
        return

    for index in range(0, len(array)):
        if selected_index.get(index) == 1:
            continue

        permutation.append(array[index])
        selected_index[index] = 1
        print_all_permutation(permutation, array, selected_index)
        permutation.remove(array[index])
        selected_index.pop(index)


if __name__ == '__main__':
    array = [1, 2, 3]
    print_all_permutation([], array, {})