import socket

from PyQt6.QtWidgets import QMainWindow
from pymorphy2 import MorphAnalyzer

from window import riddler, game
from view import start_window_ui

HOST = '127.0.0.1'
PORT = 5060


class StartWindow(QMainWindow, start_window_ui.Ui_MainWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.setupUi(self)

        self.player = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.player.connect((HOST, PORT))

        self.game_window = None
        self.create_word_label.setHidden(True)
        self.join_room_label.setHidden(True)
        self.create_room_btn.clicked.connect(self.create_room)
        self.join_room_btn.clicked.connect(self.join_room)

    def create_room(self):
        word = self.hidden_word_line.text().replace(' ', '')
        parse_rez = MorphAnalyzer().parse(word)[0].tag
        if parse_rez.POS == 'NOUN' and parse_rez.number == 'sing' and len(word) == 5:
            self.create_word_label.setHidden(True)
            self.player.send(f"create_{word}".encode('utf-8'))
            room_id = self.player.recv(1024).decode('utf-8')
            self.game_window = riddler.RiddlerWindow(self.player, room_id, word)
            self.game_window.show()
            self.close()
        else:
            self.create_word_label.setHidden(False)

    def join_room(self):
        room_id = self.join_room_line.text()
        if room_id.isdigit():
            self.player.send(f"join_{room_id}".encode('utf-8'))
            status, room_id, guess_word = self.player.recv(1024).decode('utf-8').split('_')
            if status == 'success':
                self.join_room_label.setHidden(True)
                self.game_window = game.Game(self.player, room_id, guess_word)
                self.game_window.show()
                self.close()
            elif status == 'error':
                self.join_room_label.setHidden(False)
        else:
            self.join_room_label.setHidden(False)


