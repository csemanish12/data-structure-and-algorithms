def print_subsequence(index, sequence_array, array_size, subsequence_array, current_sum, k):
    if index == array_size:
        if current_sum == k:
            print(subsequence_array)
            return True

        return False

    subsequence_array.append(sequence_array[index])
    current_sum += sequence_array[index]
    if print_subsequence(index + 1, sequence_array, array_size, subsequence_array, current_sum, k):
        return True

    subsequence_array.remove(sequence_array[index])
    current_sum -= sequence_array[index]
    if print_subsequence(index + 1, sequence_array, array_size, subsequence_array, current_sum, k):
        return True

    return False


if __name__ == '__main__':
    k = 2
    sequence = [1, 2, 1]
    print_subsequence(0, sequence, len(sequence), [], 0, k)