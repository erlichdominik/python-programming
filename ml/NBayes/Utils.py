from collections import defaultdict
from typing import List


def __get_len_of_all_attr_without_decision_attr(all_attributes: List) -> int:
    return len(all_attributes)


def _populate_main_dict(all_attributes: List) -> defaultdict:
    dictionary = defaultdict(defaultdict)
    len_of_all_attributes = __get_len_of_all_attr_without_decision_attr(all_attributes)

    # can be push to another function
    for attribute_number in range(len_of_all_attributes):
        dictionary['attribute{}'.format(attribute_number + 1)] = (defaultdict(defaultdict))

    return dictionary

def _populate_main_dict_for_each_attribute(attr_num: int):
    pass
