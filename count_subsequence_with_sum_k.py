def get_subsequence_count(index, sequence_array, array_size, current_sum, k):
    if index == array_size:
        if current_sum == k:
            return 1

        return 0

    index_element = sequence_array[index]

    current_sum += index_element
    first_recursion_count = get_subsequence_count(index+1, sequence_array, array_size, current_sum, k)

    current_sum -= index_element
    second_recursion_count = get_subsequence_count(index+1, sequence_array, array_size, current_sum, k)

    return first_recursion_count + second_recursion_count


if __name__ == '__main__':
    k = 2
    sequence = [1, 3, 1, -1]
    subsequence_count = get_subsequence_count(0, sequence, len(sequence), 0, k)
    print("subsequence found:", subsequence_count)
