from typing import List

from Utils import _get_number_of_perceptrons, _extract_decision_attributes
from perceptron.Perceptron import Perceptron


class Network:
    def __init__(self, list_of_input_vectors):
        # input vector: [[1,2,3,4, dec_att], [5,6,7,8, dec_att2],...]
        self.input_vectors: List = list_of_input_vectors
        # list of perceptrons used to predict output
        self.perceptrons: List = self.__init_perceptrons()
        # list of all decision attributes from input vector
        self.decision_attributes: List = list(_extract_decision_attributes(self.input_vectors))
        self.num_of_perceptrons: int = _get_number_of_perceptrons(self.decision_attributes)

    def train(self, num_of_epochs=1) -> None:
        """
        Trains each Perceptron\n
        :param num_of_epochs: Number of epochs for training Neural Network
        :return: None
        """
        for j in range(self.num_of_perceptrons):
            self.perceptrons[j].train(num_of_epochs)

    def __init_perceptrons(self) -> List[Perceptron]:
        """
        Creates list of Perceptrons with input vectors for Neural Network\n
        :return: list of Perceptrons
        """
        perceptrons = []
        for i in range(self.num_of_perceptrons):
            perceptrons.append(Perceptron(self.input_vectors))

        for i in range(len(self.decision_attributes)):
            perceptrons[i].set_output_names(
                name_for_zero="Other",
                name_for_one=self.decision_attributes[i]
            )

        return perceptrons

# TODO: Predict for one text that'll be passed to fun
    def predict(self, test_set: List) -> None:
        """
        :param test_set: test set
        :return: None
        """
