"""Напишите программу на Python, которая на вход получает список списков:\
[
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]
и возвращает список кортежей. Каждый кортеж состоит из номера заказа и произведения
цены на товары и количества. Стоимость заказа должна быть увеличена на $10, если она
меньше $100. Программа должна использовать lambda, map, однострочный if, round и list.
Решение задачи должно быть выполнено в ОДНУ СТРОКУ!"""

accounting_book = [[34587, 'Learning Python, Mark Lutz', 4, 40.95],
           [98762, 'Programming Python, Mark Lutz', 5, 56.80],
           [77226, 'Head First Python, Paul Barry', 3, 32.95],
           [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]]

print(list(map(lambda x: (x[0], round(x[2]*x[3], 2) if x[2]*x[3] >= 100 else round(x[2]*x[3], 2)+10), accounting_book)))