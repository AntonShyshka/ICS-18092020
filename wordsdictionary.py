from words import words

def eng():
    eng_words=dict([[v, k] for k,v in words.items()])
    find_word=input('Enter word ' '')
    print(eng_words.get(find_word) or print('No such key'))

def rus():
    key=input('Введите слово ' '')
    print (words.get(key) or 'Искомое слово не найдено')

if __name__ == '__main__':
    x=input('Найти перевод английского слова? ' '')
    if x == 'y':
        rus()
    elif x == 'n':
        eng()
    else:
        print('Увидимся позже')