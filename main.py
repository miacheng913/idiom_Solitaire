from PyQt5 import QtWidgets

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton)
from PyQt5.QtGui import QFont

import START ,DECIDE,PLAY,NUMBER

import pandas as pd
import numpy as np
df = pd.read_csv("pic/test.csv",encoding="utf-8")

t = df.pinyin.str.split()
df["shoupin"] = t.str[0]
df["weipin"] = t.str[-1]
df = df.set_index("chengyu")[["shoupin", "weipin"]]

word = "一毛不拔"
words = df.index[df.shoupin == df.loc[word, "weipin"]]

state = ''
weipin = ''

n = 0

count = 0

class PLAY_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = PLAY.Ui_Form()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('遊戲中')
        self.ui.label.setFont(QFont("微軟正黑體",12))
        self.enter = self.ui.enter
        self.enter.clicked.connect(self.enterClick)
        self.ui.restart.clicked.connect(self.restart)
        self.ui.return_2.clicked.connect(self.return_click)
        self.enter.setEnabled(True)
        
        global weipin

        if state == '後':
            word2 = np.random.choice(df.index)
            text = "電腦 : " + word2
            print(text)
            self.ui.label.setText(text)
            weipin = df.loc[word2, "weipin"]
        else:
            weipin = ''
        
        global n,count
        count = n
        print(count)

    def enterClick(self):
        
        msg = self.ui.lineEdit.text()
        text = self.ui.label.text()
        print(msg)
        global n,count
        count,text = self.play(text,msg,count)
        self.ui.label.setText(text)
        if count == -1 :
            self.enter.setEnabled(False)
        else :
            self.enter.setEnabled(True)
        #self.ui.label.setText(msg)
        self.ui.lineEdit.setText("")

    def restart(self):
        global n,count
        global weipin,df
        if state == '後':
            word2 = np.random.choice(df.index)
            text = self.ui.label.text()
            text = " 電腦 : " + word2
            print(text)
            self.ui.label.setText(text)
            weipin = df.loc[word2, "weipin"]
        else:
            weipin = ''

        
        global n,count
        count = n

        self.enter.setEnabled(True)

    def return_click(self):
        global window
        window = decide_controller()
        window.show()
    


    def play(self,text,msg,count):
        global weipin
        word = msg
        
        if word not in df.index:
            text = text + "\n你輸入的不是一個成語,請重新輸入!"
            print(text)
            return count,text

        if weipin and df.loc[word, 'shoupin'] != weipin:
            text = text + "\n你輸入的成語並不能與機器人出的成語接上來，你輸了，遊戲結束！！！"
            print(text)
            return -1,text

        words = df.index[df.shoupin == df.loc[word, "weipin"]]
        if words.size == 0 :
            text = text + "\n恭喜你贏了！成語機器人已經被你打敗！！！"
            print(text)
            return -1,text

        
        count = count-1
        if count == 0 :
            text = text + "\n恭喜你贏了！成語機器人已經被你打敗！！！"
            return -1,text

        text = text + "\n 你 : " + word

        word2 = np.random.choice(words)
        text = text + "\n電腦 : " + word2

        weipin = df.loc[word2, "weipin"]

        return count,text

class NUMBER_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = NUMBER.Ui_Form()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('遊戲中')

        self.enter = self.ui.enter
        self.enter.clicked.connect(self.enterClick)

    def enterClick(self):
        global n,window
        n = int(self.ui.lineEdit.text())
        print(n)
        window = PLAY_controller()
        window.show()
        

class decide_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = DECIDE.Ui_Form()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('my window')

        self.first = self.ui.first
        self.second = self.ui.second
        self.first.clicked.connect(self.firstClick)
        self.second.clicked.connect(self.secondClick)
        self.ui.pushButton.clicked.connect(self.return_click)

    def firstClick(self):
        global state
        state = '先'
        global window
        window = NUMBER_controller()
        window.show()

    def secondClick(self):
        global state
        state = '後'
        global window
        window = NUMBER_controller()
        window.show()

    def return_click(self):
        global window
        window = MainWindow_controller()
        window.show()


class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = START.Ui_start()
        self.ui.setupUi(self)
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle('my window')

        self.startButton = self.ui.startButton
        self.startButton.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        global window
        window = decide_controller()
        window.show()



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow_controller()
    window.show()
    sys.exit(app.exec_())