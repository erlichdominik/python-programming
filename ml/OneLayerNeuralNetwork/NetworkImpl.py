# custom implemenation of 1NN
from typing import List, Dict

from Network import Network
from Utils import _transform_str_to_vector_with_da, _transform_txt_to_vector_without_da
import glob
import os

DATA_FOLDER_NAME = './data'


def load_languages_names() -> Dict[str, List]:
    # collect every folder name inside data folder
    list_of_languages = os.listdir(DATA_FOLDER_NAME)
    # create dict to store every name of
    # [name of language, list of .txt files from this language]
    lng_files_dict = {}
    # for each language inside list_of_languages append list of .txt from this file
    for lng in list_of_languages:
        lng_files_dict[lng] = os.listdir(DATA_FOLDER_NAME + "/" + lng)

    return lng_files_dict


def load_data() -> List:
    languages_names = load_languages_names()
    vectors = []
    for lng in languages_names.keys():
        for i in range(len(languages_names[lng])):
            with open(DATA_FOLDER_NAME + '/' + lng + '/' + languages_names[lng][i], 'r', encoding='UTF8') as f:
                txt = f.read()
            vectors.append(_transform_str_to_vector_with_da(txt, lng))
    return vectors


if __name__ == '__main__':
    input_vectors = load_data()
    network = Network(input_vectors)
    network.train(100)

    with open('./test/test.txt', 'r', encoding='UTF8') as f:
        test_file = f.read()

    test_file = _transform_txt_to_vector_without_da(test_file)
    network.predict(test_file)



