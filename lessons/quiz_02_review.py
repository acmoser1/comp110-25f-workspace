"""function-writing practice problems for quiz 02"""

"""lists"""


def short_words(input_list: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters"""
    return_list: list[str] = []
    for x in input_list:
        if len(x) < 5:
            return_list.append(x)
        else:
            print(f"{x} is too long!")
    return return_list


def multiples(values: list[int]) -> list[bool]:
    """returns a list[bool] that tells whether each int value
    is a multiple of the previous value"""
    multiples: list[bool] = []
    # check first value against last value
    if values[0] % values[len(values) - 1] == 0:
        multiples.append(True)
    else:
        multiples.append(False)
    index: int = 1
    while index < len(values):
        if values[index] % values[index - 1] == 0:
            multiples.append(True)
        else:
            multiples.append(False)
        index += 1
    return multiples


def reverse_multiply(vals: list[int]) -> list[int]:
    dub_reverse: list[int] = []
    index: int = len(vals) - 1
    while index >= 0:
        dub_reverse.append(vals[index] * 2)
        index -= 1
    return dub_reverse


def process_and_reverse_list(list):
    squared_list = []
    index = 0
    while index < len(list):
        squared_value = list[index] * list[index]
        squared_list.append(squared_value)
        index += 1
    summed_pairs = []
    index = 0
    while index < len(squared_list) - 1:
        pair_sum = squared_list[index] + squared_list[index + 1]
        summed_pairs.append(pair_sum)
        index += 2
    if len(squared_list) % 2 != 0:
        summed_pairs.append(squared_list[-1])
    reversed_list = []
    index = len(summed_pairs) - 1
    while index >= 0:
        reversed_list.append(summed_pairs[index])
        index -= 1
    return reversed_list


"""dictionaries"""


def value_exists(my_dict: dict[str, int], val: int) -> bool:
    for key in my_dict:
        if my_dict[key] == val:
            return True
    return False


def plus_or_minus_n(inp: dict[str, int], n: int) -> None:
    for key in inp:
        if inp[key] % 2 == 0:
            inp[key] += n
        else:
            inp[key] -= n


def free_biscuits(dict1: dict[str, list[int]]) -> dict[str, bool]:
    result: dict[str, bool] = {}
    for key in dict1:
        list_to_sum: list[int] = dict1[key]
        sum: int = 0
        for element in list_to_sum:
            sum += element
        if sum >= 100:
            result[key] = True
        else:
            result[key] = False
    return result


def max_key(my_dict: dict[str, list[int]]) -> str:
    max_key: str = ""
    max_val_sum: int = 0
    for key in my_dict:
        val_sum: int = 0
        for value in my_dict[key]:
            val_sum += value
        if val_sum > max_val_sum:
            max_val_sum = val_sum
            max_key = key
    return max_key
