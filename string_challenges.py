# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
letters = 'аоуэиыеёюя'
sum_letters = 0
for letter in word.lower():
    if letter in letters:
        sum_letters += 1
print(f'Количество гласных букв в слове {word}: {sum_letters}')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sentence_list = sentence.split()
for word in sentence_list:
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sentence_len = len(sentence.split())
sentence_sum = len(sentence.replace(' ', ''))
print(sentence_sum / sentence_len)
