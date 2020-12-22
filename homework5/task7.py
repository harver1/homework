# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

j_list = []
my_dict = {}

with open(file='task7.txt', mode='rt', encoding='UTF-8') as file:
    temp = [line.split() for line in file]
    average = []

    for i in temp:
        i.pop(1)
# считаем прибыль компании
    for lst in temp:
        name, profit, costs = lst
        average.append([name, (int(profit)-int(costs))])
# считаем среднюю прибыль, без учета убыточных компаний
    medium_profit = sum([i[1] for i in average if i[1] > 0]) / len([i[1] for i in average if i[1] > 0])
# формируем словарь где ключ название компании, а прибыль или убыток - значение
    for i, k in average:
        my_dict[i] = k
# добавляем словарь в список
j_list.append(my_dict)
j_list.append(dict(average_profit=medium_profit))  # добавляем в список словарь со средней выручкой компаний

# Записываем данные в json
with open(file='task7.json', mode='wt', encoding='utf-8') as file_json:
    json.dump(j_list, file_json, ensure_ascii=False, indent=2)  # без ensure_ascii=False экранирует ключт первого
    # словаря почему так не разобрался.

with open(file='task7_1.json', mode='wt', encoding='utf-8') as file_json:
    json.dump(j_list, file_json, indent=2)  # экранировались ключи первого словаря \uXXXX
