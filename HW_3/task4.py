'''
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
'''

travel_items = {'Палатка': 5, 'Спальник': 1, 'Гиря': 16, 'Котелок': 1, 'Вода': 2, 'Еда': 3}
backpack_capacity = 7
res_dict = {}
weight = 0

for key, value in travel_items.items():
    if weight + value > backpack_capacity:
        continue
    if weight <= backpack_capacity:
        res_dict.update(dict([(key, value)]))
        weight += value
print(*res_dict, sep=", ")