def print_subsequence(index, sequence_array, array_size, subsequence_array):
    if index >= array_size:
        print(subsequence_array)
        return

    subsequence_array.append(sequence_array[index])
    print_subsequence(index + 1, sequence_array, array_size, subsequence_array)
    subsequence_array.remove(sequence_array[index])
    print_subsequence(index + 1, sequence_array, array_size, subsequence_array)


if __name__ == '__main__':
    sequence = [3, 1, 2, 0]
    print_subsequence(0, sequence, len(sequence), [])