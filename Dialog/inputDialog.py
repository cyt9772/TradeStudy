import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800,200,300,300)
        self.setWindowTitle("PyStoick v0.1")

        self.pushButton=QPushButton("Input Number")
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label=QLabel()

        layout=QVBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)

        self.setLayout(layout)


    def pushButtonClicked(self):
        # text,ok=QInputDialog.getInt(self, '매수수량','매수 수량을 입력하세요')
        # if ok:
        #     self.label.setText(str(text))
        items=("KOSPI","KOSDAQ","KONEX")
        item,ok=QInputDialog.getItem(self, "시장선택","시장을 선택하세요",items, 0, False)
        if ok and item:
            self.label.setText(item)


if __name__=="__main__":
    app = QApplication(sys.argv)
    window=MyWindow()
    window.show()
    app.exec_()


