from typing import List

from .utils import _get_matrix, _init_weight_list, _get_len_of_weights, _get_decision_attribute


class Perceptron:
    """simple Perceptron class"""

    def __init__(self, input_vector, *, learning_rate=0.5):
        """
        input_vector takes array of arrays of inputs and correct output at last index
        example: [[5.7,2.5,5.0,2.0,Iris-virginica], [5.6,3.0,4.1,1.3,Iris-versicolor]]
        """
        self._input_vec: List = input_vector
        self._weights: List = _init_weight_list(
            _get_len_of_weights(input_vector))
        self._threshold: float = 0.0
        self._learning_rate: float = learning_rate
        self.output_name_for_one: str = ""
        self._output_name_for_zero: str = ""

    def set_threshold(self, threshold) -> None:
        self._threshold = threshold

    def set_learning_rate(self, learning_rate) -> None:
        self._learning_rate = learning_rate

    def set_output_names(self, *, name_for_zero, name_for_one) -> None:
        self._output_name_for_zero = name_for_zero
        self.output_name_for_one = name_for_one

    def set_output_name_for_zero(self, name) -> None:
        self._output_name_for_zero = name

    def set_output_name_for_one(self, name) -> None:
        self.output_name_for_one = name

    def _predict_output_for_one_row(self, vec) -> float:
        """predict output for single vector
        example: [1,2,3,4]
        """
        __output = 0.0
        for i in range(len(vec)):
            __output += vec[i] + self._weights[i]
        return 1.0 if __output - self._threshold > 0 else 0.0
    '''
    def predict_output(self):
        """returns 1.0 if perceptron is activated, 0.0 otherwise"""
        __output = 0.0
        for i in range(len(self._input_vec)):
            __output += self._input_vec[i] + self._weights[i]
        return 1.0 if __output - self._threshold > 0 else 0.0
    '''
    def __train_weights(self, input_vector, desired_output, prediction) -> List:
        __weights = _init_weight_list(
            _get_len_of_weights(self._input_vec)
        )
        for i in range(len(input_vector)):
            __weights[i] = __weights[i] + (desired_output - prediction) * self._learning_rate * input_vector[i]
        return __weights

    def __train_threshold(self, desired_output, prediction) -> float:
        return self._threshold + (desired_output - prediction) * self._learning_rate * (-1)

    def train(self, num_of_epochs=1) -> None:
        for epoch in range(num_of_epochs):
            self.__delta_rule()

    def set_predict(self, input_set) -> None:
        errors = 0
        for row in input_set:
            prediction = self._predict_output_for_one_row(_get_matrix(row))
            desired_output = 1 if _get_decision_attribute(row) == self.output_name_for_one else 0
            prediction_output = self.output_name_for_one if prediction == 1 else self._output_name_for_zero
            print('for: ' + str(_get_matrix(row)) + ' prediction is: ' +
                  prediction_output, ' true output ' +
                  _get_decision_attribute(row))
            if prediction != desired_output:
                errors += 1
        print('accuracy: ', 1 - errors / len(input_set))

    def single_predict(self, input_vector) -> None:
        """input vector should be the same as in training set without decision argument"""
        for i in range(len(input_vector)):
            input_vector[i] = float(input_vector[i])
        prediction = self._predict_output_for_one_row(input_vector)
        prediction_output = self.output_name_for_one if prediction == 1 else self._output_name_for_zero
        print('for input:' + str(input_vector) + ' prediction is: ' + prediction_output)

    def __delta_rule(self) -> None:
        __new_weights = _init_weight_list(
            _get_len_of_weights(self._input_vec)
        )
        __new_threshold = 0.0
        for row in self._input_vec:
            # for every input vector calculate prediction and desired output
            prediction = self._predict_output_for_one_row(_get_matrix(row))
            desired_output = 1.0 if _get_decision_attribute(row) == self.output_name_for_one else 0.0
            if prediction != desired_output:
                # calculate new weights and threshold
                __new_weights = self.__train_weights(_get_matrix(row), desired_output, prediction)
                __new_threshold = self.__train_threshold(desired_output, prediction)
        self.set_threshold(__new_threshold)
        self._weights = __new_weights
