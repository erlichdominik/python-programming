def _init_weight_list(length):
    """return list of zero's for len"""
    return [0 for _ in range(length)]


def _get_len_of_weights(vectors):
    """from vector output correct len of weights
    vector example: [[5.7, 2.5, 5.0, 2.0, "Iris-virginica"], [5.6, 3.0, 4.1, 1.3, "Iris-versicolor"]]
    """
    return len(vectors[0][:-1])


def _get_decision_attribute(vector):
    """return desired output of single vector"""
    return vector[-1]


def _get_matrix(vector):
    """return matrix of values from a single vector"""
    return vector[:-1]

