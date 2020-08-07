from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    result = [[]]
    length = len(input_set)
    for i in range(1, 2**length):
        j = 0
        sub_set = []
        while j < length:
            if (i >> j) & 1:
                sub_set.append(input_set[j])
            j += 1
        result.append(sub_set)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
