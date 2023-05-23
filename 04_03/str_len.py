"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


def iterative_str_len(a_str):
    count = 0
    for char in a_str:
        count += 1
    return count


def recursive_str_len(a_str):
    # Base case
    if a_str == '':
        return 0
    # Recursive case
    return 1 + recursive_str_len(a_str[1:])


input_str = "I love recursion"
print(len(input_str))  # Standard Pythonic way
print(iterative_str_len(input_str))
print(recursive_str_len(input_str))
