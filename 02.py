'''
Реализовать крестики-нолики
Название
TikTacToe
функции
place_crosses
place_noughts
get_winner
'''


class TikTacToe:
    field = [['', '', ''], ['', '', ''], ['', '', '']]
    winner = 0
    def __init__(self, field):
        self.field = field

    def place_crosses(self, x, y):
        """
        Должен вернуть 1, если всё ок. Или 0, если нельзя осуществить операцию
        """
        if self.field[x-1][y-1] == '':
            self.field[x-1][y-1] = 'X'
            return 1
        else:
            return 0

    def place_noughts(self, x, y):
        """
        Должен вернуть 1, если всё ок. Или 0, если нельзя осуществить операцию
        """
        if self.field[x-1][y-1] == ' ':
            self.field[x-1][y-1] = '0'
            return 1
        else:
            return 0

    def get_winner(self):
        """
        Вернуть
        0 нет победителя
        1 победили crosses
        0 победили noughts
        """
        # по 1й строчке победа
        if self.field[0][0] == self.field[0][1] == self.field[0][2]:
            winner = self.field[0][0]
        # по 2й строчке победа
        elif self.field[1][0] == self.field[1][1] == self.field[1][2]:
            winner = self.field[1][0]
        # по 3й строчке победа
        elif self.field[2][0] == self.field[2][1] == self.field[2][2]:
            winner = self.field[2][0]
        # по 1ому столбцу победа
        elif self.field[0][0] == self.field[1][0] == self.field[2][0]:
            winner = self.field[0][0]
        # по 2ому столбцу победа
        elif self.field[0][1] == self.field[1][1] == self.field[2][1]:
            winner = self.field[0][1]
        # по 3ему столбцу победа
        elif self.field[0][2] == self.field[1][2] == self.field[2][2]:
            winner = self.field[0][2]
        # диагональ от [0][0] до [2][2]
        elif self.field[0][0] == self.field[1][1] == self.field[2][2]:
            winner = self.field[0][0]
        # диагональ от [0][2] до [2][0]
        elif self.field[0][2] == self.field[1][1] == self.field[2][0]:
            winner = self.field[0][2]
        if winner == 'X':
            return 1
        else:
            return 0





def test_1():
    game = TikTacToe()
    assert game.place_crosses(1, 3) == 1
    assert game.place_crosses(1, 3) == 0