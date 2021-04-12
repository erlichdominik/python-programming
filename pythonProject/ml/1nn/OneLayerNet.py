from BasicPerceptron import BasicPerceptron


class OneLayerNet:
    def __init__(self, languages, threshold, learning_rate):
        self.num_of_languages = len(languages)
        self.languages = languages
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.layer = self.hidden_layer_init()

    def hidden_layer_init(self):
        layer = []
        for language in self.languages:
            layer.append(BasicPerceptron(self.threshold, self.learning_rate, language))
        return layer

    def train_weights(self, desired_language, input_vector):
        for perceptron in self.layer:
            perceptron.train_weights(desired_language, input_vector)

    def predict(self, input_vector):
        predictions = []
        for i in range(len(self.layer)):
            predictions.append(self.layer[i].predict(input_vector))
            if self.layer[i].predict(input_vector) == 1.0:
                return self.layer[i].language


