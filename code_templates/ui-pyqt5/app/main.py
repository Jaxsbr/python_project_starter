from PyQt5.QtWidgets import QApplication

from main_window import MainWindow

def main():
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()

if __name__ == "__main__":
    main()
