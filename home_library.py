import os
lib = 'D:/libray'
file = open('Список книг бібліотеки.txt', 'w')
for d, subDirs, files in os.walk(lib):
    currentDir = d.replace('D:/libray', '') + ": \n"
    if currentDir == ": \n": 
        continue
    file.write(currentDir)
    i = 0
    for f in files:
        currentFile = "\t" + str(i) + ') ' + f + "\n"
        file.write(currentFile)
        i += 1
        f = open('Список книг бібліотеки.txt', 'r')
file.close()