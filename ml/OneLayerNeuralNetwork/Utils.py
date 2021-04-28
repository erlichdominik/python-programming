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


def _transform_str_to_vector_with_da(text: str, decision_attribute: str) -> List:
    """

    :param text: text to transform
    :param decision_attribute: name of decision attribute
    :return: list with histogram of letters with decision attribute at the end
    """
    text = _strip_accents(text).lower()
    freq_list = []
    c = collections.Counter(text)
    for letter in string.ascii_lowercase:
        freq_list.append(c[letter])
    freq_list.append(decision_attribute)
    return freq_list


def _transform_txt_to_vector_without_da(text: str) -> List:
    """

    :param text: text to transform
    :return: list from frequency histogram of letters
    """
    text = _strip_accents(text).lower()
    freq_list = []
    c = collections.Counter(text)
    for letter in string.ascii_lowercase:
        freq_list.append(c[letter])
    return freq_list


def _strip_accents(s: str) -> str:
    """

    :param s: text to transform
    :return: text with only latins letters
    """
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')




test = [[1, 2, 3, 4, 'xd'], [13, 321, 321, 321, 'lol'], [123, 321, 32112, 213, 'xd'], [1123, 321, 321, 321, 'wtf']]

#print(_extract_decision_attributes(test))

# print(*test[0][-1:])
