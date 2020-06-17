# Задание 9
# Простой класс для карточный игры "Игра в дурака".
# Реализованы следующие методы: инициализация игры (раздача карт себе и компьютеру), ходит компютер, я отбиваюсь.
import random
cards = [6, 7, 8, 9, 10, "V", "D", "K", "A"]
lears = ["♥", "♦", "♠", "♣"]

'''
     V - Валет
     D - Дама
     K - Король
     A - Туз
     '''

class Game:
    def __init__(self, x, y):
        self.player = x
        self.computer = y

    def logic(self):
        h_hand = self.player
        c_hand = self.computer
        c_card = random.choice(c_hand)
        print("Ход компьютера: {}".format(c_card))
        n = int(input("Выберите номер карты: "))
        h_card = h_hand[n]
        print("Ваша карта: {}".format(h_card))

        # Выражение карт (валет, дама, король, туз) численными значениями
        if c_card[0] == "A":
            c_card = c_card.replace("A", "14")
        elif c_card[0] == "K":
            c_card = c_card.replace("K", "13")
        elif c_card[0] == "D":
            c_card = c_card.replace("D", "12")
        elif c_card[0] == "V":
            c_card = c_card.replace("V", "11")

        if h_card[0] == "A":
            h_card = h_card.replace("A", "14")
        elif h_card[0] == "K":
            h_card = h_card.replace("K", "13")
        elif h_card[0] == "D":
            h_card = h_card.replace("D", "12")
        elif h_card[0] == "V":
            h_card = h_card.replace("V", "11")

        if c_card[-1] == h_card[-1]:
            if int(h_card[:-1]) > int(c_card[:-1]):
                result = "Бито!"
        else:
            result = 'Эта карта не бьет!'
        print(result)
        return result

# Формирование колоды
def gen_deck():
    deck = []
    for i in range(9):
        for j in range(4):
            _card = str(cards[i]) + lears[j]
            deck.append(_card)
    return deck


class Hands:
    def __init__(self, gen_dec):
        self.gen = gen_dec

    def gen_h_hand(self):

        # Карты игрока
        gen_dec = self.gen
        player_hand = {}
        for i in range(6):
            player_hand[i] = random.choice(gen_dec)
            gen_dec.remove(player_hand[i])
        print("Карты игрока: {}".format(player_hand))
        return player_hand

    def gen_c_hand(self):

        # Карты Компьютера
        gen_dec = self.gen
        computer_hand = {}
        for i in range(6):
            computer_hand[i] = random.choice(gen_dec)
            gen_dec.remove(computer_hand[i])
        print("Карты компьютера: {}".format(computer_hand))
        return computer_hand


gen = Hands(gen_deck())
game = Game(gen.gen_h_hand(), gen.gen_c_hand())
if __name__ == "__main__":
    game.logic()