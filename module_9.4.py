first = 'Мама мыла раму'
second = 'Рамена мало было'
new_list = (list(map(lambda x, y: f"'{x}' и '{y}' совпадают: {x == y}",first, second)))
for i in new_list:
    print(i,end='\n')
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a',encoding='utf-8') as file:
            for i in range(len(data_set)):
                file.write(str(data_set[i]) + "\n")
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

with open('example.txt', 'r',encoding='utf-8') as file:
    print(file.read())

import random
class MysticBall:
    def __init__(self,word):
        self.word = word

    def __call__(self):
        return random.choice(self.word)

ball = MysticBall(["Да", "Нет", "Возможно", "Не знаю"])
print(ball())
print(ball())
print(ball())
print(ball())