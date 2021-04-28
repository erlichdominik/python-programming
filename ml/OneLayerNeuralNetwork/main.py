import unicodedata
import string
import collections

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

txt = 'text HisTogramu'.lower()

c = collections.Counter(txt)

freq_list = []

for letter in string.ascii_lowercase:
    print('{}: {}'.format(letter, c[letter]))
    freq_list.append(c[letter])

print(freq_list)

# lol = Network()


# Network (ammount of perceptrons, [[input vector, decision argument], [..], [.]...])
# Network.train(number of epochs)
# Network.SetPredict()
# Network.SinglePredict()
# xd = Network()
