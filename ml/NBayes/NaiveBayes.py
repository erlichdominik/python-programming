from typing import List, Callable, final, Final, Dict
import itertools
from collections import defaultdict
from Utils import _populate_main_dict, _populate_main_dict_for_each_attribute

DATA_PATH_TEST: Final[str] = './data/test'
DATA_PATH_TRAIN: Final[str] = './data/train'
DATA_PATH_LIST: Final[List[str]] = [DATA_PATH_TRAIN, DATA_PATH_TEST]


def get_num_of_rows(data_list: List) -> int:
    ctr = 0
    for data in data_list:
        ctr += 1
    return ctr


def get_decision_attribute(row: List) -> str:
    return str(*row[-1:])


def get_all_decision_attributes(data_list: List) -> List:
    all_decision_arguments = set()
    for single_row in data_list:
        all_decision_arguments.add(get_decision_attribute(single_row))
    return list(all_decision_arguments)


def get_freq_of_all_decision_attribute(data_list: List, decision_attributes_list: List[str]) -> \
        Dict[str, int]:
    prob_dict = {}
    for da in decision_attributes_list:
        nr_of_app = 0
        for row in data_list:
            if get_decision_attribute(row) == da:
                nr_of_app += 1
        prob_dict[da] = nr_of_app
    return prob_dict


def get_data(data_path: str) -> List:
    output_list = []
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


def get_amount_of_attributes(data_list: List) -> int:
    return len(data_list[0][:-1])


def get_list_of_all_attributes(data_list: List) -> List:
    """

    :param data_list: data
    :return: list of attributes -> [0] first column
    """
    nr_of_attributes = get_amount_of_attributes(data_list)
    final_list = []
    # omitting last element which is decision argument
    for attribute_nr in range(nr_of_attributes):
        data = set()
        for row in data_list:
            data.add(row[attribute_nr])
        final_list.append(list(data))
    return final_list


def get_cartesian_product_of_all_attributes(list_of_all_attributes: List) -> List:
    _list = []
    for element in itertools.product(*list_of_all_attributes):
        _list.append(list(element))
    return _list


def get_num_of_app_for_dec_atr_and_arg(data_list: List, dec_atr: str, atr: str) -> int:
    _ctr = 0
    for row in data_list:
        if row[0] == atr and get_decision_attribute(row) == dec_atr:
            _ctr += 1
    return _ctr


def populate_prob_for_attr(data_list: List, col_nr: int, curr_dict: Dict):
    decision_attributes = get_all_decision_attributes(data_list)
    freq = get_freq_of_all_decision_attribute(data_list, decision_attributes)
    list_of_values_for_attr = curr_dict.keys()
    # iterate over data
    for row in data_list:
        value = row[col_nr]
        da = get_decision_attribute(row)
        curr_dict[value][da][0] += 1
    # calculate probability
    for row in data_list:
        value = row[col_nr]
        da = get_decision_attribute(row)
        accur = curr_dict[value][da][0]
        curr_dict[value][da][1] = accur / freq[da]

    return curr_dict


def get_attribute_table(data_list: List, all_attributes: List[List], decision_attributes: List) -> Dict[str, List]:
    main_dictionary = defaultdict(defaultdict)
    main_dictionary = _populate_main_dict(all_attributes)

    # populate with values of each attribute for each attribute
    for attribute_number in range(len(main_dictionary)):
        main_dictionary[
            'attribute{}'.format(attribute_number + 1)
        ] = {attr: {da: [0, 0] for da in decision_attributes} for attr in all_attributes[attribute_number]}

    # for every decision attribute in attributes value add number of appereancies
    for attribute_number in range(len(main_dictionary)):
        curr_dict_attr = main_dictionary['attribute{}'.format(attribute_number + 1)]
        # print('curr dict attr', curr_dict_attr)
        main_dictionary['attribute{}'.format(attribute_number + 1)] = populate_prob_for_attr(
            data_list,
            attribute_number,
            curr_dict_attr,
        )

    return dict(main_dictionary)


def get_prob_of_arg_val(attr_table: Dict, attr_name: str, att_value: str, ) -> float:
    _num = 0.0
    for data in attr_table[attr_name][att_value]:
        _num += attr_table[attr_name][att_value][data][1]
    return _num


def get_results_for_test_data(test_data: List, list_off_all_attr: List,  attr_table: Dict) -> None:
    probability = 0.0

    amount_of_attributes = len(list_off_all_attr)
    for row in test_data:
        row_without_da = row[0:amount_of_attributes]
        decision_attribute = get_decision_attribute(row)
        print('decision_attribute', decision_attribute)
        for attribute_number in range(len(row_without_da)):
            current_attr_num = attribute_number + 1
            current_attr = row[attribute_number]
            # print('attr num', current_attr_num)
            current_attr_table = attr_table['attribute{}'.format(current_attr_num)]
            prob_for_current_attr = current_attr_table[row[attribute_number]]
            # print('prob_for_current_attr', prob_for_current_attr)
            prob_for_current_attr_for_da = prob_for_current_attr[decision_attribute]
            print('prob_for_current_attr_for_da', prob_for_current_attr_for_da[1])


if __name__ == '__main__':
    # using train data to classify all the cases
    train_data = get_data(DATA_PATH_TRAIN)
    nr_of_rows = get_num_of_rows(train_data)
    decision_attributes = get_all_decision_attributes(train_data)
    list_of_all_attributes = get_list_of_all_attributes(train_data)
    prob = get_freq_of_all_decision_attribute(train_data, decision_attributes)
    attribute_table = get_attribute_table(
        train_data,
        list_of_all_attributes,
        decision_attributes
    )

    print(attribute_table)

    # importing test data
    test_data = get_data(DATA_PATH_TEST)
    test_nr_of_rows = get_num_of_rows(test_data)
    test_decision_attributes = get_all_decision_attributes(test_data)
    test_list_of_all_attributes = get_list_of_all_attributes(test_data)
    print(test_list_of_all_attributes)
    print('len', len(test_list_of_all_attributes))
    # TODO:
    #   for each row check all possible 1650
    #   for each row we need to check every column
    #   extract probability of each value  and use formula for each dec attr

    get_results_for_test_data(test_data, list_of_all_attributes, attribute_table)