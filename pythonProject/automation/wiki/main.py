import sys
import wikipedia

if __name__ == '__main__':
    args = [arg for arg in sys.argv[1:]]
    # input: [nr_of_languages], [language], [nr_of_titles], [titles] x times
    # 3 pl 2 ada,piernik eng 3 test,angielski,nice
    num_of_languages = int(args[0]) + 1
    languages = []
    nr_of_titles = []
    languages_titles_dict = {}
    titles = []
    for i in range(1, len(args), 2):
        languages.append(args[i])
    for i in range(2, len(args), 2):
        titles.append(args[i].split(','))
    for i in range(0, len(languages)):
        languages_titles_dict[languages[i]] = titles[i]
    print(languages_titles_dict)


