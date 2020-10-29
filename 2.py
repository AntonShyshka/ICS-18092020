fn = "text.txt"
lines = 0
words = 0
letters = 0
words_dict = 0
for line in open(fn):
    lines += 1
    letters += len(line)
 
    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
import os
 
 
def get_words(fn):
 
    with open(fn, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words
 
 
def get_words_dict(words):
    words_dict = dict()
 
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict
 
 
def main():
    fn = input("Введите путь к файлу: ")
    if not os.path.exists(fn):
        print("Указанный файл не существует")
    else:
        words = get_words(fn)
        words_dict = get_words_dict(words)
        print("Кількість слів: %d" % len(words))
        print("Кількість унікальних слів: %d" % len(words_dict))
        print("Всі використані слова:")
        for word in words_dict:
             print(word.ljust(20), words_dict[word])
 
 
if __name__ == "__main__":
    main()
