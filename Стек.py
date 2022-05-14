stack = []
for i in range(5):
    print('Какую футболку вы кладёте сверху стопки?')
    stack.append(input())
print(stack)
while stack:
    print('Сегодня вы надеваете футболку',stack.pop())