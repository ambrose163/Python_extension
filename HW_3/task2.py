'''
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
'''

my_list = [1, 1, 2, 3, 3, 3, 4]

dupl_elem = set()
for el in range(len(my_list)):
    if my_list.count(my_list[el]) > 1:
        dupl_elem.add(my_list[el])
print(f"С применением множеств: {list(dupl_elem)}")

dupl_elem = []
for el in range(len(my_list)):
    if my_list.count(my_list[el]) > 1 and dupl_elem.count(my_list[el]) < 1:
        dupl_elem.append(my_list[el])
print(f"Без применения множеств: {dupl_elem}")