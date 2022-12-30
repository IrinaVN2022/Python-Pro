# Дана строка (большАя строка, лучше взять на английском). Выведите слово, которое в этой строке
# встречается чаще всего.
# Если таких слов несколько, выведите последнее.
# Задачу необходимо решить с использованием словаря.

some_string = 'I like apple because apple is useful and I recommend to eat apple everyone.'
word_list = some_string.split()
word_dict = {}
for word in word_list:
    word_dict.update({word_list.count(word): word})
print(word_dict)
sorted_dict = sorted(word_dict.items())
print(f'the word {sorted_dict[-1][1]} occurs most often.')


