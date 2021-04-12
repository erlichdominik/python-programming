def format_data(data_set):
    result = []
    for data in data_set:
        matrix = data.split(',')[:-1]
        for i in range(len(matrix)):
            matrix[i] = float(matrix[i])
        decision_attribute = data.split(',')[-1:]
        result.append([matrix, *decision_attribute])
    return result


def calculate_threshold(d, y, alpha):
    pass


def predict(x, w, threshold):
    """x = [1,2,3,4,5]"""
    output = 0.0
    for i in range(len(x)):
        output += x[i] * w[i]
    return 1.0 if output >= threshold else 0.0


def train_weights(training_set, learning_rate, num_of_epochs, threshold):
    weights = [0.0 for i in range(len(training_set[0][0]))]
    # print(weights)
    for epoch in range(num_of_epochs):
        for row in training_set:
            # print(row[0])
            prediction = predict(row[0], weights, threshold)
            desired_output = 1 if row[1] == 'Iris-virginica' else 0
            if prediction != desired_output:
                for i in range(len(row[0])):
                    weights[i] = weights[i] + (desired_output - prediction) * learning_rate * row[0][i]
    return weights


def train_weights_example(training_set, learning_rate, num_of_epochs, threshold):
    weights = [0.0 for i in range(len(training_set[0][0]))]
    # print(weights)
    for epoch in range(num_of_epochs):
        for row in training_set:
            # print(row[0])
            prediction = predict(row[0], weights, threshold)
            desired_output = 1 if row[1] == '1' else 0
            if prediction != desired_output:
                for i in range(len(row[0])):
                    weights[i] = weights[i] + (desired_output - prediction) * learning_rate * row[0][i]
    return weights


def iris_single(learning_rate, threshold):
    with open('./iris_training.txt') as f:
        iris_training_data = f.read().splitlines()

    iris_training_data = format_data(iris_training_data)
    trained_weights = train_weights(iris_training_data, learning_rate, 1000, threshold)

    input_vector = input("input vector: 1,2,3,4")
    input_vector_list = input_vector.split(sep=",")

    for number in range(len(input_vector_list)):
        input_vector_list[number] = float(input_vector_list[number])

    prediction = predict(input_vector_list, trained_weights, threshold)
    prediction_output = 'Iris-virginica' if prediction == 1 else 'Iris-versicolor'
    print("for input ", input_vector_list, " prediction is: ", prediction_output)


def iris(learning_rate, threshold):
    with open('./iris_training.txt') as f:
        iris_training_data = f.read().splitlines()

    iris_training_data = format_data(iris_training_data)

    trained_weights = train_weights(iris_training_data, learning_rate, 1000, threshold)

    with open('./iris_test.txt') as f:
        iris_test_data = f.read().splitlines()

    iris_test_data = format_data(iris_test_data)
    errors = 0
    for row in iris_test_data:
        prediction = predict(row[0], trained_weights, threshold)
        desired_output = 1 if row[1] == 'Iris-virginica' else 0
        prediction_output = 'Iris-virginica' if prediction == 1 else 'Iris-versicolor'
        print("for input ", row[0], " prediction is: ", prediction_output, " true output: ", row[1])
        if prediction != desired_output:
            errors += 1
    print("accuracy: ", 1 - errors / len(iris_test_data))


def example_single(learning_rate, threshold):
    with open('./example2_train.txt') as f:
        example_training_data = f.read().splitlines()

    example_training_data = format_data(example_training_data)
    trained_weights = train_weights_example(example_training_data, learning_rate, 1, threshold)
    input_vector = input("input vector: 1,2")

    input_vector_list = input_vector.split(sep=",")

    for number in range(len(input_vector_list)):
        input_vector_list[number] = float(input_vector_list[number])

    prediction = predict(input_vector_list, trained_weights, threshold)
    prediction_output = '1' if prediction == 1 else '0'
    print("for input ", input_vector_list, " prediction is: ", prediction_output)


def example(learning_rate, threshold):
    with open('./example2_train.txt') as f:
        example_training_data = f.read().splitlines()

    example_training_data = format_data(example_training_data)

    trained_weights = train_weights_example(example_training_data, learning_rate, 1, threshold)

    with open('./example1_test.txt') as f:
        example_test_data = f.read().splitlines()

    example_test_data = format_data(example_test_data)
    errors = 0
    for row in example_test_data:
        prediction = predict(row[0], trained_weights, threshold)
        desired_output = 1 if row[1] == '1' else 0
        prediction_output = '1' if prediction == 1 else '0'
        print("for input ", row[0], " prediction is: ", prediction_output, " true output: ", row[1])
        if prediction != desired_output:
            errors += 1
    print("accuracy: ", 1 - errors / len(example_test_data))


def ui():
    learning_rate = float(input('input learning rate'))
    data_type = input('input on which data you want to operate [iris, example]')
    threshold = 0.5
    flag = int(input('1.test data, 2.our vector'))
    if data_type == 'iris' and flag == 1:
        iris(learning_rate, threshold)
    elif data_type == 'iris' and flag == 2:
        iris_single(learning_rate, threshold)
    elif data_type == 'example' and flag == 1:
        example(learning_rate, threshold)
    elif data_type == 'example' and flag == 2:
        example_single(learning_rate, threshold)


ui()
