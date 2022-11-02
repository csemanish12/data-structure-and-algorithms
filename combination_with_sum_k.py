import copy


def combination_sum(index, candidates, target, selected_candidates, found_candidates):
    if index == len(candidates):
        if target == 0:
            found_candidates.append(copy.copy(selected_candidates))
            return

        return

    index_element = candidates[index]

    if index_element <= target:
        selected_candidates.append(index_element)
        combination_sum(index, candidates, target-index_element, selected_candidates, found_candidates)
        selected_candidates.remove(index_element)

    combination_sum(index+1, candidates, target, selected_candidates, found_candidates)


if __name__ == '__main__':
    target_sum = 7
    found_candidates = []
    ds = []
    input_candidates = [2, 3, 6, 7]
    combination_sum(0, input_candidates, target_sum, ds, found_candidates)
    print("output:",found_candidates)