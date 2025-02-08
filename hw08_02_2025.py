# 1. Импортируйте `full_dict` из файла `Marvel.py`.
from marvel import full_dict
from pprint import pprint
print('----------------start---------------')
# print(full_dict)
# print('----------------2---------------')
# 2. Реализуйте ввод от пользователя, который будет принимать цифры через пробел. Разбейте введённую строку на список и примените к каждому элементу `int`, заменяя нечисловые элементы на `None` с помощью `map`.
def f2(inp):
    try:
        int(inp)
    except:
        inp = None
    return inp

num_list = map(f2, input("Введите числа через пробел: ").split())
# num_list = [1, 42, 3]
# print(num_list)

# print('----------------3---------------')
# 3. Используйте `filter`, чтобы создать словарь, содержащий исходные `id` и другие ключи, но только для тех фильмов, `id` которых присутствуют в списке, полученном на предыдущем шаге.
result_dict = dict(filter(lambda film: film[0] in num_list, full_dict.items()))
# print(result_dict)

# print('----------------4---------------')
# 4. Создайте множество с помощью `set comprehension`, собрав уникальные значения ключа `director` из словаря.
unique_values = {val['director'] for val in full_dict.values()}
# print(unique_values)

# print('----------------5---------------')
# 5. С помощью `dict comprehension` создайте копию исходного словаря `full_dict`, преобразовав каждое значение `'year'` в строку. **(Опционально)**
full_dict_copy = {id: {**data, 'year': str(data['year'])} for id, data in full_dict.items()}
# print(full_dict_copy)

# print('----------------6---------------')
# 6. Используйте `filter`, чтобы получить словарь, содержащий только те фильмы, которые начинаются на букву `Ч`.
ch_filtered = list(filter(lambda x: x[1]['title'] and x[1]['title'][0].lower() == 'ч', full_dict.items()))
# print(ch_filtered)

# print('----------------7---------------')
# 7. Отсортируйте словарь `full_dict` по одному параметру с использованием `lambda`, создавая аналогичный по структуре словарь. Обязательно укажите, по какому параметру вы производите сортировку.
year_sorted_dict = dict(sorted(full_dict.items(), key=lambda item: item[1]['year'] if isinstance (item[1]['year'], int) else 0))
# print(year_sorted_dict)

# print('----------------8---------------')
# 8. Отсортируйте словарь `full_dict` по двум параметрам с использованием `lambda`, создавая аналогичный по структуре словарь. Обязательно укажите, по каким параметрам вы производите сортировку.
year_title_sorted_dict = sorted(full_dict.items(), key=lambda item: (item[1]['year'] if isinstance (item[1]['year'], int) else 0, item[1]['title'] if isinstance (item[1]['title'], str) else ''))
# pprint(year_title_sorted_dict, sort_dicts=False, indent= 4)
