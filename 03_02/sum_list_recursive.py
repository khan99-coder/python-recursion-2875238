"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


def list_sum(a_list):
    # iterative solution
    result = 0
    for item in a_list:
        result += item
    return result


def list_sum_recursive(a_list):
    # base case
    if len(a_list) == 0:
        return 0
    # recursive case
    else:
        return a_list[0] + list_sum_recursive(a_list[1:])


assert list_sum([2, 3, 5, 7]) == 17
assert list_sum([-4, -3, -2, -1, 10]) == 0

assert list_sum_recursive([2, 3, 5, 7]) == 17
assert list_sum_recursive([-4, -3, -2, -1, 10]) == 0
assert list_sum_recursive([]) == 0
assert list_sum_recursive([3]) == 3
assert list_sum_recursive([-5, -3]) == -8
