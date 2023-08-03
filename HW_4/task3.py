'''
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
'''

import operator

with open("task3_text.txt") as file:
    text = file.read().lower().replace(",", "").replace(".", "").split()

TOP_WORDS = 10
count_words = 0
dct = {}

for el in range(len(text)):
    dct.update([(text[el], text.count(text[el]))])
sorted_dct = dict(sorted(dct.items(), key=operator.itemgetter(1)))

for key, value in reversed(sorted_dct.items()):
    count_words += 1
    print(f'#{count_words} {key} {value}')
    if count_words == TOP_WORDS:
        break