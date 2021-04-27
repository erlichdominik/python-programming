from typing import Set, List, Any


def _get_number_of_perceptrons(list_of_input_vectors: List) -> int:
    """passing arr_of_input_vectors [[1,2,3,4,decision_att],[]] in correct format
    and returning number of perceptrons to be passed to network constructor
    """
    return list_of_input_vectors[0][:-1]


def _extract_decision_attributes(input_vectors: List) -> Set:
    """passing input_vectors [[1,2,3,4,decision_att],[...],...]
    and returning set of decision_attributs
    """
    output = set()
    for i in range(len(input_vectors)):
        output.add(*input_vectors[i][-1:])
    return output


def __get_att_from_input_vector(input_vec: List) -> Any:
    return input_vec[:-1]


test = [[1, 2, 3, 4, 'xd'], [13, 321, 321, 321, 'lol'], [123, 321, 32112, 213, 'xd'], [1123, 321, 321, 321, 'wtf']]

print(_extract_decision_attributes(test))

# print(*test[0][-1:])
