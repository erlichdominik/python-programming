from typing import Set, List, Any, Sized
import unicodedata
import collections
import string

def _get_number_of_perceptrons(decision_attributes: Sized) -> int:
    """
    :param decision_attributes: List of input vectors with decision attributes as last element
    :return: len of decision attributes
    """
    return len(decision_attributes)


def _extract_decision_attributes(input_vectors: List) -> Set:
    """
    :param input_vectors: List of input vectors with decision attributes as last element
    :return: Set of decision attributes
    """
    output = set()
    for i in range(len(input_vectors)):
        output.add(*input_vectors[i][-1:])
    return output


def __get_att_from_input_vector(input_vec: List) -> Any:
    return input_vec[:-1]


# TODO: create functions to transform string into input vector without decision argument

def _transform_str_to_vector_with_da(text: str, name_of_file: str) -> List:
    text = _strip_accents(text).lower()
    freq_list = []
    c = collections.Counter(text)
    for letter in string.ascii_lowercase:
        freq_list.append(c[letter])
    freq_list.append(name_of_file)
    return freq_list




# TODO: create function to transform text into input vector with decision argument

def _transform_txt_to_vector_without_da(text: str) -> List:
    pass


def _strip_accents(s: str) -> str:
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


test = [[1, 2, 3, 4, 'xd'], [13, 321, 321, 321, 'lol'], [123, 321, 32112, 213, 'xd'], [1123, 321, 321, 321, 'wtf']]

print(_extract_decision_attributes(test))

# print(*test[0][-1:])
