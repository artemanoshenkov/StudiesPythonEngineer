import re

message = input("Введите строку: ")

pattern = r'[\W]'
worlds_list = re.split(pattern, message)

list_count_alpha_worlds = []
count_worlds = 0

for world in worlds_list:
    if world.isalpha():
        count_worlds += 1
        list_count_alpha_worlds.append(len(world))

print("Количество слов: {}".format(count_worlds))
print("Средняя длина слова: {:.2f}".format(sum(list_count_alpha_worlds) / count_worlds))
