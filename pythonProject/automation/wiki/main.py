import sys
import wikipedia
import os

if __name__ == '__main__':
    args = [arg for arg in sys.argv[1:]]
    languages = []
    nr_of_titles = []
    languages_titles_dict = {}
    titles = []
    path = os.path.abspath(args[0])
    for i in range(2, len(args), 2):
        languages.append(args[i-1])
        titles.append(args[i].split(','))
    for i in range(0, len(languages)):
        languages_titles_dict[languages[i]] = titles[i]
    print(path)

    for lang in languages_titles_dict:
        wikipedia.set_lang(lang)
        for title in languages_titles_dict[lang]:
            file_path = path + "/" + title + '.txt'
            with open(file_path, 'w+', encoding='utf-8') as f:
                page = wikipedia.page(title)
                print(page.title)
                f.write(page.content)



