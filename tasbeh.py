import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QBoxLayout



class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Tasbeh')
        self.setFixedSize(200,150)
        self.v_box = QVBoxLayout()
        

        self.setStyleSheet("background-color: #FFBBFF")

        self.count = 0
        self.z_c = 0
        self.zikrlar = ('Subhanalloh', 'Alhamdulillah', 'Laa ilaha illalloh', 'Allohu Akbar')
        
        self.zikr_label = QLabel(self.zikrlar[self.z_c])

        self.count_btn = QPushButton(str(self.count))
        self.count_btn.clicked.connect(self.changeCount)
        self.count_btn.setStyleSheet("background-color: #FF69B4")

        self.v_box.addWidget(self.zikr_label)
        self.v_box.addWidget(self.count_btn)

        self.setLayout(self.v_box)

        self.show()

    def changeCount(self):
        if self.count == 33:
            self.z_c += 1
            self.zikr_label.setText(self.zikrlar[self.z_c % len(self.zikrlar)])
            self.count = -1                         
        self.count += 1
        self.count_btn.setText(str(self.count))



app = QApplication([])
win = Window()
sys.exit(app.exec_())