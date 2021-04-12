from OneLayerNet import OneLayerNet


def letter_dict(alphabet):
    letter_dict = {}
    for letter in alphabet:
        letter_dict[letter] = 0
    return letter_dict


def input_layer(text):
    #text = remove_accents(text)
    letter_dictionary = letter_dict('abcdefghijklmnopqrstuvwxyz')
    all_letters_num = 0
    input_vector = []
    for word in text.split():
        word.lower()
        for char in word:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                all_letters_num += 1
                letter_dictionary[char] += 1
    for letter in letter_dictionary.keys():
        input_vector.append(letter_dictionary[letter] / all_letters_num)
    return input_vector


def read_trainset(folder):
    pass


def main():
    """from trainset we get a dict where languages are the keys and the values are texts in key language"""
    trainset_dict = {'pl': ['mowie po polsku, bo jestem Polakiem', 'papiez byl wielkim czlowiekiem']}
    list_of_languages = trainset_dict.keys()
    epochs = 1
    threshold = 0.5
    learning_rate = 0.1
    our_network = OneLayerNet(list_of_languages, threshold, learning_rate)
    for i in range(epochs):
        for language in list_of_languages:
            for text in trainset_dict[language]:
                input_vector = input_layer(text)
                #print(input_vector)
                our_network.train_weights(language, input_vector)

    testset = []
    for text in testset:
        print(our_network.predict(input_layer(text)))


main()
