import threading

from PyQt6.QtWidgets import QMainWindow

from view import riddler_ui


class RiddlerWindow(QMainWindow, riddler_ui.Ui_MainWindow):
    def __init__(self, player, room_name, guessed_word):
        super(RiddlerWindow, self).__init__()

        self.player = player
        self.room_name = room_name
        self.guessed_word = guessed_word
        self.try_num = 0
        self.finish_game = False

        self.setupUi(self)
        self.room_name_label.setText(f"Room name: {self.room_name}")
        self.guess_word_label.setText(f"Guessed word: {self.guessed_word}")
        self.leave.setEnabled(False)
        self.leave.clicked.connect(self.leave_game)

        self.all_rez = [self.rez1_label, self.rez2_label, self.rez3_label, self.rez4_label, self.rez5_label,
                        self.rez6_label]
        self.thread = threading.Thread(target=self.receive)
        self.thread.start()

    def receive(self):
        while not self.finish_game:
            try:
                try_rez = self.player.recv(1024).decode('utf-8')
                if try_rez == "win":
                    self.all_rez[self.try_num].setText("guessed it")
                    self.status_label.setText("LOSE")
                    self.finish_game = True
                    self.leave.setEnabled(True)
                elif try_rez == "lose":
                    self.all_rez[self.try_num].setText("not guessed it")
                    self.status_label.setText("WIN")
                    self.finish_game = True
                    self.leave.setEnabled(True)
                else:
                    self.all_rez[self.try_num].setText("not guessed it")
                self.try_num += 1
            except Exception as exc:
                print(f"{self.player} leave (with Exception{exc})")
                self.close()
                break

    def leave_game(self):
        self.close()
