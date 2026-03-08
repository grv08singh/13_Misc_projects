# Modules
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont
from googletrans import Translator
from languages import *

# Class
class Home(QWidget):
    # Constructor
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()
        self.button_click()

    # App Object and Design
    def initUI(self):
        self.input_box = QTextEdit()
        self.output_box = QTextEdit()
        self.reverse = QPushButton("Reverse")
        self.reset = QPushButton("Reset")
        self.submit = QPushButton("Translate Now")
        self.input_option = QComboBox()
        self.output_option = QComboBox()
        self.input_option.addItems(values)
        self.output_option.addItems(values)
        self.title = QLabel("Translate")
        self.title.setFont(QFont("Helvetica", 45))

        self.master = QHBoxLayout()
        col1 = QVBoxLayout()
        col2 = QVBoxLayout()
        col1.addWidget(self.title)
        col1.addWidget(self.input_option)
        col1.addWidget(self.output_option)
        col1.addWidget(self.submit)
        col1.addWidget(self.reset)
        col2.addWidget(self.input_box)
        col2.addWidget(self.reverse)
        col2.addWidget(self.output_box)
        self.master.addLayout(col1, 20)
        self.master.addLayout(col2, 80)
        self.setLayout(self.master)

        self.setStyleSheet("""
            QWidget{
                           background-color: #333;
                           color: #fff;
                           }
            QPushButton{
                           background-color: #66a3ff;
                           color: #333;
                           border: 1px solid #fff;
                           border-radius: 5px;
                           padding: 5px 10px;
                           }
            QPushButton:hover{
                           background-color: #3399ff;
                           }
        
        """)


    # App Settings
    def settings(self):
        self.setWindowTitle("PyLate")
        self.setGeometry(250,250,600,500)

    # button events
    def button_click(self):
        self.submit.clicked.connect(self.translate_click)
        self.reverse.clicked.connect(self.reverse_click)
        self.reset.clicked.connect(self.reset_app)

    # Translate Click
    def translate_click(self):
        value_to_key1 = self.output_option.currentText()
        value_to_key2 = self.input_option.currentText()

        key_to_value1 = [k for k,v in LANGUAGES.items() if v == value_to_key1]
        key_to_value2 = [k for k,v in LANGUAGES.items() if v == value_to_key2]

        self.script = self.translate_text(self.input_box.toPlainText(), key_to_value1[0], key_to_value2[0])
        self.output_box.setText(self.script)

    # Reset App
    def reset_app(self):
        self.input_box.clear()
        self.output_box.clear()

    # Translate Text (Google)
    def translate_text(self, text, dest_lang, src_lang):
        speaker = Translator()
        translation = speaker.translate(text,dest=dest_lang, src=src_lang)
        return translation.text

    # Reverse Translation
    def reverse_click(self):
        s1, l1 = self.input_box.toPlainText(), self.input_option.currentText()
        s2, l2 = self.output_box.toPlainText(), self.output_option.currentText()

        self.input_box.setText(s2)
        self.output_box.setText(s1)

        self.input_option.setCurrentText(l2)
        self.output_option.setCurrentText(l1)



# Main Run
if __name__=="__main__":
    app = QApplication([])
    main = Home()
    main.show()
    app.exec_()