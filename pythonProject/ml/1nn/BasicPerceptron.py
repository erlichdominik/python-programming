class BasicPerceptron:
    def __init__(self, threshold, learning_rate, language):
        self.weights = [0 for i in range(26)]
        self.language = language
        self.threshold = threshold
        self.learning_rate = learning_rate

    def predict(self, input_vector):
        output = 0.0
        print('wages', self.weights)
        print('input vector', input_vector)
        print('input vector len', len(input_vector))
        for i in range(len(input_vector)):
            output += input_vector[i] * self.weights[i]
        output -= self.threshold
        return 1.0 if output >= 0.0 else 0.0

    def train_weights(self, desired_language, input_vector):
        desired_output = 1.0 if self.language == desired_language else 0.0
        prediction = self.predict(input_vector)
        for i in range(len(self.weights)):
            self.weights[i] = (desired_output - prediction) \
                              * self.weights[i] + self.learning_rate * input_vector[i]
        self.calculate_threshold(desired_output, prediction)

    def calculate_threshold(self, desired_output, prediction):
        self.threshold = self.threshold + (desired_output - prediction) * self.learning_rate * (-1)

