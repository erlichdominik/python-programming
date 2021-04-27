from Utils import _get_number_of_perceptrons
from perceptron.Perceptron import Perceptron

class Network:
    def __init__(self, list_of_input_vectors):
        # input vector: [[1,2,3,4, dec_att], [5,6,7,8, dec_att2],...]
        self.input_vectors = list_of_input_vectors
        # list of perceptrons used to predcit output
        self.perceptrons = self.__create_perceptrons()
        self.num_of_perceptrons = _get_number_of_perceptrons(self.input_vectors)

    def train(self, num_of_epochs=1):
        for j in range(self.num_of_perceptrons):
            self.perceptrons[j].train(num_of_epochs)

    def __create_perceptrons(self):
        perceptrons = []
        for i in range(self.num_of_perceptrons):
            perceptrons.append(Perceptron(self.input_vectors))
        return perceptrons

