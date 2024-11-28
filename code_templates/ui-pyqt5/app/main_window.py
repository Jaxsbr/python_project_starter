from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout, QHBoxLayout, QSplitter, QTextEdit, QListWidget, QPushButton, QInputDialog

save_path = "sentiments.json"

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Sentiment Analyzer")
        self._init_widgets()


    def _init_widgets(self) -> None:
        top_frame = self._create_frame("background-color: lightblue;")

        self._list_widget = QListWidget()
        self._list_widget.addItem("item 1")
        self._list_widget.addItem("item 2")
        self._list_widget.addItem("item 3")
        self._list_widget.itemClicked.connect(self._list_widget_item_clicked)

        add_button = QPushButton("Click Me")
        add_button.clicked.connect(self._button_clicked)

        top_layout = QVBoxLayout()
        top_layout.addWidget(add_button)
        top_layout.addWidget(self._list_widget)
        top_frame.setLayout(top_layout)

        self._text_edit = QTextEdit()
        self._text_edit.setStyleSheet("background-color: lightyellow; color: black")
        self._text_edit.setDisabled(False)

        horizontal_splitter = QSplitter(Qt.Orientation.Horizontal)
        horizontal_splitter.addWidget(top_frame)
        horizontal_splitter.addWidget(self._text_edit)
        horizontal_splitter.setSizes([150, 400])

        layout = QHBoxLayout(self)
        layout.addWidget(horizontal_splitter)
        self.setLayout(layout)
        self.setFixedSize(QSize(800, 480))


    def _create_frame(self, style: str) -> QFrame:
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet(style)
        return frame


    def _list_widget_item_clicked(self, item) -> None:
        self._text_edit.setText(item.text())


    def _button_clicked(self) -> None:
        text, ok = QInputDialog.getText(self, "INPUT DIALOG", "Enter text:")
        if ok and text:
            self._list_widget.addItem(text)
            self._text_edit.setText(text)
            last_row_index = self._list_widget.count() - 1
            self._list_widget.setCurrentRow(last_row_index)
