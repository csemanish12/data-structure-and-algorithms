import copy


def generate_combination_sum(index, candidates, subsequence, target, result):
    if target == 0:
        result.append(copy.copy(subsequence))
        return

    candidates_length = len(candidates)
    for i in range(index, candidates_length):
        current_element = candidates[i]

        if current_element > target:
            break

        if i > index and current_element == candidates[i - 1]:
            continue

        subsequence.append(current_element)
        generate_combination_sum(i + 1, candidates, subsequence, target - current_element, result)
        subsequence.remove(current_element)


if __name__ == '__main__':
    candidates_array = [4, 1, 1, 2, 2, 1]
    candidates_array.sort()
    target = 4
    required_combinations = []
    generate_combination_sum(0, candidates_array, [], target, required_combinations)
    print(required_combinations)
