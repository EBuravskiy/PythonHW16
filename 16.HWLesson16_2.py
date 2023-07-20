from random import randint


class Turtle(object):
    x_position = 0
    y_position = 0
    s_values = 1

    def go_up(self):
        self.y_position += self.s_values

    def go_down(self):
        self.y_position -= self.s_values

    def go_left(self):
        self.x_position -= self.s_values

    def go_right(self):
        self.x_position += self.s_values

    def evolve(self):
        self.s_values += 1

    def degrade(self):
        if self.s_values - 1 <= 0:
            print("Ошибка. Скорость не может быть нулевой или отрицательной")
            return
        self.s_values -= 1

    def count_moves(self, x2, y2):
        count = 0
        x_moves = 0
        y_moves = 0
        if self.x_position < x2:
            if self.x_position >= 0 and x2 >= 0:
                x_moves = x2 - self.x_position
            elif self.x_position < 0 and x2 >= 0:
                x_moves = x2 + (self.x_position * -1)
            elif self.x_position < 0 and x2 < 0:
                x_moves = (self.x_position - x2) * -1
        elif self.x_position > x2:
            if self.x_position >= 0 and x2 >= 0:
                x_moves = self.x_position - x2
            elif self.x_position >= 0 and x2 < 0:
                x_moves = (x2 * -1) + self.x_position
            elif self.x_position < 0 and x2 < 0:
                x_moves = (x2 - self.x_position) * -1

        if self.y_position < y2:
            if self.y_position >= 0 and y2 >= 0:
                y_moves = y2 - self.y_position
            elif self.y_position < 0 and y2 >= 0:
                y_moves = y2 + (self.y_position * -1)
            elif self.y_position < 0 and y2 < 0:
                y_moves = (self.y_position - y2) * -1
        elif self.y_position > y2:
            if self.y_position >= 0 and y2 >= 0:
                y_moves = self.y_position - y2
            elif self.y_position >= 0 and y2 < 0:
                y_moves = (y2 * -1) + self.y_position
            elif self.y_position < 0 and y2 < 0:
                y_moves = (y2 - self.y_position) * -1

        if x_moves % self.s_values == 0 and y_moves % self.s_values == 0:
            count = int((x_moves / self.s_values) + (y_moves / self.s_values))
            return (count)
        else:
            count = 0
            return (count)


def commands():
    print("Выберите и введите одну из нижеследующих команд")
    print('"увеличить скорость" - увеличивает скорость перемещения черепахи на 1 клетку')
    print('"уменьшить скорость" - уменьшает скорость перемещения черепахи на 1 клетку')
    print('"вверх" - перемещает черепаху вверх с заданной скоростью')
    print('"вниз" - перемещает черепаху вниз с заданной скоростью')
    print('"влево" - перемещает черепаху влево с заданной скоростью')
    print('"вправо" - перемещает черепаху вправо с заданной скоростью')
    print('"количество шагов" - сообщает о минимальном количестве перемещений до цели')
    print('"инфо" - для получения сведений о текущем положении черепахи и ее скорости')
    print('"цель" - для получения сведений о координатах финиша')


print("ЧЕРЕПАШЬИ БЕГА")
x_target = 0
y_target = 0
command = ''
print('Для игры с самостоятельно заданными координатами финиша введите: "самостоятельно:"')
print('Для игры с рандомными координатами финиша введите: "рандом"')
command = input()
if command == "самостоятельно":
    print("Введите координаты точки финиша")
    x_target = int(input("Введите координату финиша по оси X: "))
    y_target = int(input("Введите координату финиша по оси Y: "))
elif command == "рандом":
    x_target = randint(-10, 10)
    y_target = randint(-10, 10)
else:
    print("Ошибка.Неверно введенная команда! Попробуйте еще раз")
    quit()
ninja = Turtle()
while command != "stop":
    print("Введите команду. Список команд доступен по команде: список")
    command = input()
    if command == "список":
        commands()
    elif command == "увеличить скорость":
        ninja.evolve()
    elif command == "уменьшить скорость":
        ninja.degrade()
    elif command == "вверх":
        ninja.go_up()
    elif command == "вниз":
        ninja.go_down()
    elif command == "влево":
        ninja.go_left()
    elif command == "вправо":
        ninja.go_right()
    elif command == "количество шагов":
        count = ninja.count_moves(x_target, y_target)
        if count > 0:
            print("")
            print(f"Минимальное количество перемещений: {count}")
            print("")
        else:
            print("\nC текущей скоростью Вы не сможете добраться до точки финиша.\nВам необходимо изменить скорость черепахи")
            print("")
    elif command == "stop":
        print("Черепаха не дошла до финиша")
        count = ninja.count_moves(x_target, y_target)
        if count > 0:
            print(
                f"Оставшееся минимальное количество перемещений составляет {ninja.count_moves(x_target, y_target)}")
            print("")
            quit()
        else:
            print("С выбранной скоростью черепаха не могла попасть в точку финиша\n")
    elif command == "инфо":
        print(
            f"Черепаха находится по следующим координатам: x = {ninja.x_position}, y = {ninja.y_position}, скорость черепахи: {ninja.s_values}")
    elif command == "цель":
        print(
            f"Точка находится по следующим координатам x = {x_target}, y = {y_target}")
    else:
        print("-----------------------------------")
        print("Ошибка. Введена неизвестная команда")
        print("-----------------------------------")
    if (ninja.x_position == x_target) and (ninja.y_position == y_target):
        print("\nПОЗДРАВЛЯЕМ! ЧЕРЕПАХА ДОБРАЛАСЬ ДО ЦЕЛИ\n")
        command = "stop"
