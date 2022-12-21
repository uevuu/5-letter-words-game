from PyQt6.QtWidgets import QApplication
from window import start_window

if __name__ == "__main__":
    app = QApplication([])
    window = start_window.StartWindow()
    window.show()
    app.exec()
