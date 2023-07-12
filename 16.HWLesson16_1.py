class Kassa(object):
    money = 0

    def top_up(self, x):
        self.money += x
        print(f"Касса пополнена на {x} рублей, общее количество денег в кассе {self.money} рублей")
    
    def take_away(self, x):
        if self.money < x:
            print(f"Недостаточно денег в кассе. В кассе осталось {self.money} рублей")
            return
        self.money -= x
        print(f"Выданы из кассы {x} рублей. Остаток в кассе {self.money} рублей")

    def count_1000(self):
        count = int(self.money // 1000)
        string = "тысяч"
        if (count == 1):
            string = "тысяча"
        elif (count > 20) and (count % 10) == 1:
            string = "тысяча"
        elif (count > 0) and (count < 5):
            string = "тысячи"
        elif (count > 20) and ((count % 10) > 0) and ((count % 10) < 5):
            string = "тысячи"
        else:
            string = "тысяч"
        print(f"В кассе осталось {count} {string} рублей")

pyaterochka = Kassa()
up_money = float(input("Введите сумму денег вносимую в кассу: "))
pyaterochka.top_up(up_money)
take_money = float(input("Введите сумму сдачи: "))
pyaterochka.take_away(take_money)
pyaterochka.count_1000()
