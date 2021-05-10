from typing import Final, List, Dict, Iterable, Sized
from math import sqrt, exp, pi

DATA_PATH_TEST: Final[str] = './data/test'
DATA_PATH_TRAIN: Final[str] = './data/train'
DATA_PATH_LIST: Final[List[str]] = [DATA_PATH_TRAIN, DATA_PATH_TEST]


# IMPORT DATA

def get_data(data_path: str) -> List:
    output_list: List = []
    if data_path == DATA_PATH_TRAIN:
        with open(DATA_PATH_TRAIN, "r") as f:
            lines = f.read().splitlines()
        for line in lines:
            output_list.append(line.split(','))
    elif data_path == DATA_PATH_TEST:
        with open(DATA_PATH_TEST, "r") as f:
            lines = f.read().splitlines()
        for line in lines:
            output_list.append(line.split(','))
    return output_list


# SEPARATE BY CLASS

def separate_by_class(data_set: List) -> Dict:
    separated_dict: Dict = dict()
    for i in range(len(data_set)):
        vector = data_set[i]
        class_value = vector[-1]
        if class_value not in separated_dict:
            separated_dict[class_value] = list()
        separated_dict[class_value].append(vector)
    return separated_dict


# SUMMARIZE DATA FOR OUR MODEL

def get_rows_number(data_set):
    return len(data_set)


def get_len_of_attr(data_set):
    return len(data_set[0][:-1])


def get_all_attributes_for_index(data_set, index):
    attributes = set()
    for row in data_set:
        attributes.add(row[0])
    return list(attributes)


def get_num_app_for_y(data_set, label):
    separated = separate_by_class(data_set)
    return len(separated[label])


def calculate_prob_of_class_value(data_set, data_label):
    count: int = 0
    num_of_rows = get_rows_number(data_set)
    separated = separate_by_class(data_set)
    for row in separated[data_label]:
        count += 1
    return count / num_of_rows


def calculate_prob_of_x_and_y(data_set, index, value_of_x, label):
    count: int = 0
    num_of_y = get_num_app_for_y(data_set, label)
    separated = separate_by_class(data_set)
    for row in separated[label]:
        if row[index] == value_of_x:
            count += 1
    # applying smoothing
    if count == 0:
        count = count + 1
        num_of_y = num_of_y + len(get_all_attributes_for_index(data_set, index))
    return count / num_of_y


def calculate_conditional_prob(prob_of_x, prob_of_y):
    return prob_of_x


def classify(data_set: List, vector: List):
    best_output: Dict = {}
    separated = separate_by_class(data_set)
    for label in separated:
        best_prob: float = -1.
        best_lab = label
        prob_of_y = calculate_prob_of_class_value(data_set, label)
        # print('label', label)
        probability_for_label: float = 1.
        for index in range(get_len_of_attr(data_set)):
            value_of_x = vector[index]
            # print('val of x', value_of_x)
            prob_of_x = calculate_prob_of_x_and_y(data_set, index, value_of_x, label)
            # print('prob of x', prob_of_x)
            probability_for_label *= prob_of_x
        best_output[label] = probability_for_label
    return best_output


# PREDICTION

def predict(classified_data: Dict) -> str:
    max: float = -1.
    output: str = ''
    for data in classified_data:
        if classified_data[data] > max:
            max = classified_data[data]
            output = data
    return output


def classify_test_file():
    train_data_set: List = get_data(DATA_PATH_TRAIN)
    separated_by_class_train_data_set = separate_by_class(train_data_set)

    test_data_set: List = get_data(DATA_PATH_TEST)
    acc: float = 0.

    for row in test_data_set:
        classified_row = classify(train_data_set, row[:-1])
        predicted_value = predict(classified_row)
        print('for row', row, 'predicted output is', predict(classified_row))
        if predicted_value == row[-1]:
            acc += 1

    print('acc', acc / len(test_data_set))


def classify_custom_data():
    train_data_set: List = get_data(DATA_PATH_TRAIN)
    separated_by_class_train_data_set = separate_by_class(train_data_set)

    input_vector = input('provide custom observation: [a, b, c, d] ')
    input_vector = input_vector.split(',')

    classify_data = classify(train_data_set, input_vector)
    print('prediction is: ', predict(classify_data))



def ui():
    op = input('1. classify test file'
               '2. classify custom data')
    op = int(op)
    if op == 1:
        classify_test_file()
    elif op == 2:
        classify_custom_data()


if __name__ == '__main__':
    ui()
