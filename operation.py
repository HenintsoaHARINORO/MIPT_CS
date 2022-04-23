my_set = {'a', 'b', 'c', 1, 2, 3}
n = len(my_set)
print(n)

computer = {'Системный блок', 'Монитор',
'Клавиатура', 'Мышь'}
for element in computer:
    print(element, end = ', ')

print('Мышь' in computer)
print('Блок' in computer)