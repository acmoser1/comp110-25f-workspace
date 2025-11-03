"""practice with sort algorithms"""


def selection_sort(items: list[int]) -> list[int]:
    """repeatedly pull out the minimum"""
    # outer loop keeps track of how far we've sorted
    outer_index: int = 0
    while outer_index < len(items):
        # inner loop repeatedly finding the minimum
        inner_index: int = outer_index
        min: int = items[outer_index]
        min_index: int = outer_index
        while inner_index < len(items):
            if items[inner_index] < min:
                min = items[inner_index]
                min_index = inner_index
            inner_index += 1
        # by the time i've exited the inner loop, min should be my smallest element
        # put the smallest element in back of sorted part
        # SWAP
        items[min_index] = items[outer_index]  # put front elem in minimum's part
        items[outer_index] = min  # put the min in the front
        outer_index += 1
    return items


nums: list[int] = [10, 9, 7, 8]  # worst case input: most amount of swaps
print(selection_sort(nums))


def insert(item: int, new_item_idx: int, item_list: list[int]) -> list[int]:
    """input item and index in item_list"""
    new_list: list[int] = []
    index: int = 0
    while index < len(item_list):
        if index == new_item_idx:
            new_list.append(item)
        new_list.append(item_list[index])
        index += 1
    return new_list


def insertion_sort(items: list[int]) -> list[int]:
    """repeatedly move element to correct sorted spot"""
    outer_index: int = 0
    while outer_index < len(items):
        # inner loop moves backwards to put current element in the right spot
        current_element: int = items[outer_index]
        # loop backwards to put element in the right spot
        inner_index: int = outer_index
        inserted: bool = False  # track whether of not i've inserted current element
        while (inner_index >= 0) and not inserted:
            if current_element > items[inner_index]:
                items = insert(current_element, inner_index, items)
                inserted = True
            inner_index -= 1
        if (
            not inserted
        ):  # this basically means my element is smaller and needs to go in the front
            items = insert(current_element, 0, items)
        outer_index += 1
    return items


nums: list[int] = [1, 1, 1]
print(insert(2, 2, nums))
