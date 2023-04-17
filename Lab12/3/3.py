stop_word = 'stop'

text = open('Lab12/3/text.txt', 'r')
text_data = text.read()

new_text_data = text_data.replace(stop_word, '')

text = open('Lab12/3/text.txt', 'w')
text.write(new_text_data)
words_list = list(new_text_data.split(' '))
words_dict = dict()
for i in words_list:
    if i in words_dict:
        words_dict[i.capitalize()] += 1
    else:
        words_dict.setdefault(i.capitalize(), 1)

print(f'Частота встречи слова: {words_dict}')
unique_word = set(words_dict)
print(f'\nКоличество уникальных слов: {len(unique_word)}')

text.close()
