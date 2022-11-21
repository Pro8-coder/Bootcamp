file = open(r'Programming\Task24\file.txt', 'r', encoding='utf-8')

list_1 = list()
resultData = list()
for line in file.readlines():
    resultData.append(tuple(line.split('\n')[0].split(';')))

file.close()

print(resultData)
'''
a - режим добавление
w - режим на запись(очищает файл)
r - режим считывания
'''