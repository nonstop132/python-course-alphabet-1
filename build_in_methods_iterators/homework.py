from typing import List, Dict, Union, Generator
import random
import string

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter
    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """

    for dt in data:
        if dt.get('name'):
            dt['name'] = dt['name'].title()
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value
    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """

    return [{k: v for k, v in d.items() if k not in redundant_keys} for d in data]


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """

    return [dt for dt in data if value in dt.values()]


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """

    return min(data) if data else None


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the longest string
    """

    return str(min(data, key=lambda item: len(str(item)))) if data else None


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:
    """

    return min((item for item in data if key in item), key=lambda x: x[key])


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """

    return max(max(data))


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """

    return sum(data)


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text
    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532
    """

    return sum(map(lambda item: ord(item), text))


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """

    def check_simple_number(number):
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    def generator_simple_number():
        number = 2
        while number <= 200:
            if check_simple_number(number):
                yield number
            number += 1

    return generator_simple_number()


def task_11_create_list_of_random_characters() -> List[str]:
    """
    Create list of 20 elements where each element is random letter from latin alphabet
    """

    return [random.choice(string.ascii_lowercase) for i in range(20)]
