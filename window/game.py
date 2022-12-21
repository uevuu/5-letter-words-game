from PyQt6.QtWidgets import QMainWindow
from pymorphy2 import MorphAnalyzer

from view import game_ui


class Game(QMainWindow, game_ui.Ui_MainWindow):
    def __init__(self, player, room_name, guessed_word):
        super(Game, self).__init__()

        self.player = player
        self.room_name = room_name
        self.guessed_word = guessed_word
        self.try_num = 0

        self.setupUi(self)
        self.room_name_label.setText(f"Room name: {self.room_name}")
        self.guess.clicked.connect(self.guess_word)
        self.leave.setEnabled(False)
        self.leave.clicked.connect(self.leave_game)

        self.row_1 = [self.word_1_1, self.word_1_2, self.word_1_3, self.word_1_4, self.word_1_5]
        self.row_2 = [self.word_2_1, self.word_2_2, self.word_2_3, self.word_2_4, self.word_2_5]
        self.row_3 = [self.word_3_1, self.word_3_2, self.word_3_3, self.word_3_4, self.word_3_5]
        self.row_4 = [self.word_4_1, self.word_4_2, self.word_4_3, self.word_4_4, self.word_4_5]
        self.row_5 = [self.word_5_1, self.word_5_2, self.word_5_3, self.word_5_4, self.word_5_5]
        self.row_6 = [self.word_6_1, self.word_6_2, self.word_6_3, self.word_6_4, self.word_6_5]
        self.all_row = [self.row_1, self.row_2, self.row_3, self.row_4, self.row_5, self.row_6]

    def guess_word(self):
        curr_row = self.all_row[self.try_num]
        rez_word = ''.join([i.text().replace(' ', '') for i in curr_row]).lower()
        parse_rez = MorphAnalyzer().parse(rez_word)[0].tag
        if parse_rez.POS == 'NOUN' and parse_rez.number == 'sing' and len(rez_word) == 5:
            if rez_word == self.guessed_word:
                for word in curr_row:
                    word.setStyleSheet("QLineEdit {background: rgb(250, 225, 97); color: rgb(0, 0, 0)}")
                    self.guess.setEnabled(False)
                    self.leave.setEnabled(True)
                    word.setEnabled(False)
                    self.player.send('win'.encode('utf-8'))
                    self.status_label.setText("WIN")
            else:
                for index in range(len(curr_row)):
                    if curr_row[index].text() == self.guessed_word[index]:
                        curr_row[index].setStyleSheet("QLineEdit {background: rgb(250, 225, 97); color: rgb(0, 0, 0)}")
                    elif curr_row[index].text() in self.guessed_word:
                        curr_row[index].setStyleSheet("QLineEdit {background: rgb(255, 255, 255); color: rgb(0, 0, 0)}")
                    else:
                        curr_row[index].setStyleSheet(
                            "QLineEdit {background: rgb(174, 174, 174); color: rgb(255, 255, 255)}")
                    curr_row[index].setEnabled(False)
                if self.try_num == 5:
                    self.guess.setEnabled(False)
                    self.leave.setEnabled(True)
                    self.player.send('lose'.encode('utf-8'))
                    self.status_label.setText("LOSE")
                else:
                    self.player.send('none'.encode('utf-8'))
                    self.try_num += 1
                    for word in self.all_row[self.try_num]:
                        word.setEnabled(True)
        else:
            print('incorrect word')

    def leave_game(self):
        self.close()
        self.player.send('leave'.encode('utf-8'))


