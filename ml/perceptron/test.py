from Perceptron import Perceptron


def format_data(data_set):
    _result = []
    for data in data_set:
        matrix = data.split(',')[:-1]
        for i in range(len(matrix)):
            matrix[i] = float(matrix[i])
        decision_attribute = data.split(',')[-1:]
        _result.append([*matrix, *decision_attribute])
    return _result

def read_file(file_path):
    with open(file_path, 'r') as f:
        file = f.read().splitlines()
    return file

iris_training_data = read_file('./data/iris_training.txt')
iris_training_data = format_data(iris_training_data)

iris_test_data = read_file('./data/iris_test.txt')
iris_test_data = format_data(iris_test_data)

perceptron = Perceptron(iris_training_data)
perceptron.set_output_names(name_for_zero='Iris-versicolor', name_for_one='Iris-virginica')
perceptron.set_threshold(0.3)
perceptron.set_learning_rate(0.5)
perceptron.train(1000)
perceptron.set_predict(iris_test_data)

# perceptron.set_predict(iris_test_data) or perceptron.single_predict([1,2,3,4])