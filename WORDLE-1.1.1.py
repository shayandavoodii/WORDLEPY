# -*- coding: utf-8 -*-



# ┌────────────────────────┐
# │************************│
# │                        │
# │     Version 1.1.2      │
# │                        │
# │                        │
# │************************│
# └────────────────────────┘

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import sys
import numpy as np
import random
import pandas as pd
import emoji
import datetime
import re

class Ui_WORDLE(object):
    def setupUi(self, WORDLE):
        WORDLE.setObjectName("WORDLE")
        WORDLE.resize(863, 641)

        font = QtGui.QFont()
        font.setPointSize(12)

        font1 = QtGui.QFont()
        font1.setPointSize(14)
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(WORDLE)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 9, 861, 511))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        
        
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.adjustSize()
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)        
        self.horizontalLayout.addWidget(self.label)
        
        self.label2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label2.adjustSize()
        self.label2.setFont(font)
        self.label2.setText("")
        self.label2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label2.setObjectName("label2")
        self.horizontalLayout.addWidget(self.label2)
        
        
        
        self.label_word = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_word.adjustSize()
        self.label_word.setFont(font1)
        self.label_word.setText("")
        self.label_word.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_word.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_word.setObjectName("label_word")
        self.horizontalLayout.addWidget(self.label_word)
        
        
        self.label3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label3.adjustSize()
        self.label3.setText("")
        self.label3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label3.setObjectName("label3")
        self.horizontalLayout.addWidget(self.label3)
        
        
        
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(WORDLE)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(230, 540, 391, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        
        
# ====================================== Stats Button ======================================
        
        self.Stats_Button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.Stats_Button.setObjectName("Stats_Button")
        self.Stats_Button.clicked.connect(self.stats)
        self.verticalLayout_2.addWidget(self.Stats_Button)
        
# ====================================== History Button ======================================

        self.History_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.History_button.setObjectName("History_button")
        self.History_button.clicked.connect(self.history)
        self.verticalLayout_2.addWidget(self.History_button)
        
        
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
# ====================================== Input Feild ======================================

        self.input_text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.input_text.setObjectName("input_text")
        self.input_text.setPlaceholderText("Enter The Word")
        self.verticalLayout_3.addWidget(self.input_text)
        
        self.placeHolder_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.placeHolder_label.setFont(font)
        self.placeHolder_label.setText("")
        self.placeHolder_label.setAlignment(QtCore.Qt.AlignCenter)
        self.placeHolder_label.setObjectName("placeHolder_label")
        self.verticalLayout_3.addWidget(self.placeHolder_label)
        
        
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

# ====================================== Enter Button ======================================
        
        self.button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button.setObjectName("button")
        self.button.clicked.connect(self.clicked)
        self.verticalLayout.addWidget(self.button)
        
# ====================================== Start Button ======================================
        
        self.button2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.button2.setObjectName("button2")
        self.button2.clicked.connect(self.reset_clicked)
        self.verticalLayout.addWidget(self.button2)
        
        self.horizontalLayout_2.addLayout(self.verticalLayout)


# ====================================== Made By Shayan Hyper Link ======================================

        self.MadeByShayan = QtWidgets.QLabel(WORDLE)
        self.MadeByShayan.setGeometry(QtCore.QRect(70, 570, 101, 16))
        self.MadeByShayan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MadeByShayan.setOpenExternalLinks(True)
        self.MadeByShayan.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.MadeByShayan.setObjectName("MadeByShayan")

# ====================================== LOGO ======================================
        self.logo_label = QtWidgets.QLabel(WORDLE)
        self.logo_label.setGeometry(QtCore.QRect(47, 569, 20, 20))
        self.logo_label.setMinimumSize(QtCore.QSize(20, 20))
        self.logo_label.setMaximumSize(QtCore.QSize(55, 16777215))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("C:\\Users\\Shayan\\Documents\\Python Scripts\\WORDLE\\2048px-Octicons-mark-github.svg.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        # self.logo_label.setOpenExternalLinks(True)


        self.retranslateUi(WORDLE)
        QtCore.QMetaObject.connectSlotsByName(WORDLE)

        self.need_restart = True

    def retranslateUi(self, WORDLE):
        _translate = QtCore.QCoreApplication.translate
        WORDLE.setWindowTitle(_translate("WORDLE", "WORDLE"))
        self.Stats_Button.setText(_translate("WORDLE", "Stats"))
        self.Stats_Button.setShortcut(_translate("WORDLE", "Ctrl+S"))
        self.History_button.setText(_translate("WORDLE", "History"))
        self.History_button.setShortcut(_translate("WORDLE", "Ctrl+H"))
        self.button.setText(_translate("WORDLE", "Enter"))
        self.button.setShortcut(_translate("WORDLE", "Ctrl+Return"))
        self.button2.setText(_translate("WORDLE", "Start"))
        self.button2.setShortcut(_translate("WORDLE", "Ctrl+E"))
        self.MadeByShayan.setText(_translate("WORDLE", "Made By <a href='https://github.com/shayandavoodii/WORDLEPY'>Shayan</a>"))

    def reset_clicked(self):
        self.need_restart = False
        self._submit_counter = 0
        # self.words = pd.read_csv("C:\\Users\\Shayan\\Documents\\Python Scripts\\WORDLE\\frequent_5_char_words.csv").iloc[: , 1].to_list()
        self.words = pd.read_csv("frequent_5_char_words.csv").iloc[: , 1].to_list()
        self.chosen_word = random.choice(self.words).lower()
        self.chosen_word_frequency = {char:self.chosen_word.count(char) for char in list(self.chosen_word)}
        self.letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        # self.show = np.zeros((6,1) , dtype=[('x', '<U6')])
        self.show = []
        self.tries = []
        self.potential_letters = []
        self.place_holder = ["_" for l in range(5)]
        self.place_holder_helper = [False for l in range(5)]
        self.label3.setText(emoji.emojize("Start!:tada:" , use_aliases=True))
        self.label.setText("")
        self.label2.setText("")
        self.label_word.setText("")
        self.placeHolder_label.setText("")
        self.input_text.setReadOnly(False)
        self.input_text.setStyleSheet("color : black")


    def clicked(self):
        if not self.input_text.text():
            pass

        elif self.need_restart:
            self.label.setText("Click on Start to play")

        elif self._submit_counter<6:

            # if QLineEdit contains a word
            if self.input_text.text():
                
                a = self.input_text.text()

                # a condition for accepting input. I mean input should satisfy this condition
                if a =="?" and self._submit_counter>4:
                    self.label3.setText("!!Never Give Up!!it was '{}'".format(self.chosen_word))
                    # self._submit_counter = 0
                    self.need_restart = True
                    # with open("C:\\Users\\Shayan\\Documents\\Python Scripts\\WORDLE\\My WORDLE Log.txt" , 'a+') as txt_file:
                    with open("My WORDLE Log.txt" , 'a+') as txt_file:
                        txt_file.write("{} {} {}\n".format(str(datetime.date.today()) , "None" , self.chosen_word))
                        txt_file.close()
                        
                
                elif len(a) ==5:
                    if a.lower() in self.words:
                        if a.lower() in self.tries:
                            pass
                        
                        else:
                            a = a.lower()
                            self.tries.append(a)



                            if a == self.chosen_word:
                                # self.show[self._submit_counter , :] = emoji.emojize(":green_square::green_square::green_square::green_square::green_square:")
                                self.show.append(emoji.emojize(":green_square::green_square::green_square::green_square::green_square:"))
                                
                                self.label.setText(emoji.emojize("{}/6<br>Congrats!:tada: its true : {}<br>Click on Start to play again".format(self._submit_counter+1 , self.chosen_word) , use_aliases=True))
                                # print()
                                
                                # for row in range(self._submit_counter+1):
                                # self.label2.setText(f"{self.show}")
                                self.label2.setText("<br>".join(self.show))
                                self.label_word.setText("<br>".join(self.tries))
                                    # print(self.show[row][0][0] , self.tries[row])

                                # df = pd.read_csv("C:\\Users\\Shayan\\Documents\\Python Scripts\\WORDLE\\My WORDLE Log.txt" , sep=" " , header=None)
                                df = pd.read_csv("My WORDLE Log.txt" , sep=" " , header=None)
                                

                                if df.iloc[-1 , 1] == "None":
                                    max_streak = np.diff(np.where(df.iloc[: , 1] == "None")).max()-1

                                else:
                                    max_streak = max(len(df) - np.where(df.iloc[: , 1] == "None")[0].max() , np.diff(np.where(df.iloc[: , 1] == "None")).max()-1)

                                self.label3.setText("Max Streak = {} , Current Streak = {}".format(max_streak , len(df) - np.where(df.iloc[: , 1] == "None")[0].max()))    
                                
                                # with open("C:\\Users\\Shayan\\Documents\\Python Scripts\\WORDLE\\My WORDLE Log.txt" , 'a+') as txt_file:
                                with open("My WORDLE Log.txt" , 'a+') as txt_file:
                                    txt_file.write("{} {} {}\n".format(str(datetime.date.today()) , self._submit_counter+1 , self.chosen_word))
                                    txt_file.close()

                                self.need_restart = True
                                self.input_text.setReadOnly(True)
                                self.input_text.setStyleSheet("background-color: green; color : white")
                            else:
                                
                                counts = {item:a.count(item) for item in set(a)}
                                info = {item:0 for item in set(a)}
                                res = ""
                                for i in range(len(list(a))):
                                    if a[i] in self.chosen_word:
                                        if a[i] == self.chosen_word[i]:
                                            res += emoji.emojize(':green_square:')
                                            if self.place_holder_helper[i] == False:
                                                self.place_holder[i] = a[i]
                                                self.place_holder_helper[i] = True
                                            info[a[i]] = True

                                            if a[i] not in self.potential_letters:
                                                self.potential_letters.append(a[i])
                        # ======================================== yellow area ========================================
                                        else:
                                            if counts[a[i]]>1 and self.chosen_word_frequency[a[i]]==1 and info[a[i]] ==True:
                                                res += emoji.emojize(':red_square:')
                                                if a[i] in self.letters:
                                                    self.letters.remove(a[i])

                                            elif counts[a[i]]>1 and self.chosen_word_frequency[a[i]]==1 and info[a[i]] ==False:
                                                if self.chosen_word.index(a[i]) in [i.start() for i in re.finditer(a[i], a)]:
                                                    res += emoji.emojize(':red_square:')
                                                    
                                                else:
                                                    res += emoji.emojize(':yellow_square:')
                                                    if a[i] not in self.potential_letters:
                                                        self.potential_letters.append(a[i])

                                            elif counts[a[i]]>1 and self.chosen_word_frequency[a[i]]>1 and info[a[i]] ==True:
                                                res += emoji.emojize(':yellow_square:')
                                                if a[i] not in self.potential_letters:
                                                    self.potential_letters.append(a[i])

                                            else: 
                                                res += emoji.emojize(':yellow_square:')
                                                if a[i] not in self.potential_letters:
                                                    self.potential_letters.append(a[i])

                        # ======================================== yellow area ========================================
                                    
                                    else:
                                        res += emoji.emojize(':red_square:')
                                        if a[i] in self.letters:
                                            self.letters.remove(a[i])

                                

                                # self.show[self._submit_counter , :] = res
                                self.show.append(res)

                                self.label.setText("{}/6".format(self._submit_counter+1))
                                self.label2.setText("<br>".join(self.show))
                                self.placeHolder_label.setText("{}<br>{}".format(','.join(self.place_holder) , self.potential_letters))
                                self.label_word.setText("<br>".join(self.tries))
                                self.label3.setText(f"{self.letters}")

                                if self._submit_counter == 5:
                                    self.input_text.setReadOnly(True)
                                    self.input_text.setStyleSheet("background-color: red; color : white")
                                    self.label.setText("{}/6<br>!!FAILED!!<br>it was '{}'.<br>Click on Start to play".format(self._submit_counter+1 , self.chosen_word))
                                    self.need_restart = True
                                    # with open("C:\\Users\\Shayan\\Documents\\Python Scripts\\WORDLE\\My WORDLE Log.txt" , 'a+') as txt_file:
                                    with open("My WORDLE Log.txt" , 'a+') as txt_file:
                                        txt_file.write("{} {} {}\n".format(str(datetime.date.today()) , "None" , self.chosen_word))
                                        txt_file.close()
                            
                            self._submit_counter += 1


                else: pass

        # else:
        #     self.label.setText("!!FAILED!!")
        #     self.label2.setText("it was '{}'.".format(self.chosen_word))
        #     self.need_restart = True
        #     # with open("C:\\Users\\Shayan\\Documents\\Python Scripts\\WORDLE\\My WORDLE Log.txt" , 'a+') as txt_file:
        #     with open("My WORDLE Log.txt" , 'a+') as txt_file:
        #         txt_file.write("{} {} {}\n".format(str(datetime.date.today()) , "None" , self.chosen_word))
        #         txt_file.close()



    def stats(self):
        """statistical analysis of historical results."""
        # df = pd.read_csv("C:\\Users\\Shayan\\Documents\\Python Scripts\\WORDLE\\My WORDLE Log.txt" , sep=" " , header=None)
        df = pd.read_csv("My WORDLE Log.txt" , sep=" " , header=None)
        pairs = sorted(df[df.iloc[:,1]!='None'][1].value_counts().to_dict().items())
        _, ax = plt.subplots()
        fig1 = ax.bar([value[0] for value in pairs], height= [value[1] for value in pairs])

        if df.iloc[-1 , 1] == "None":
            max_streak = np.diff(np.where(df.iloc[: , 1] == "None")).max()-1

        else:
            max_streak = max(len(df) - np.where(df.iloc[: , 1] == "None")[0].max() , np.diff(np.where(df.iloc[: , 1] == "None")).max()-1)
        
        plt.title("Success rate = {}, Played = {}, Max Streak = {} , Current Streak = {}".format(round(len(df[df.iloc[:,1]!='None'][1])/len(df) , 2) , len(df) , max_streak , len(df) - np.where(df.iloc[: , 1] == "None")[0].max() - 1) , color = 'g')
        
        plt.xlabel("i'th guess" , size = 12)
        plt.ylabel("ّFrequency" , size = 12)
        plt.suptitle("stats of success" , size = 20)
        ax.bar_label(fig1, label_type='edge')
        plt.show()

    def history(self):
        """
        Historical plot of gaming.
        """
        # df = pd.read_csv("C:\\Users\\Shayan\\Documents\\Python Scripts\\WORDLE\\My WORDLE Log.txt" , sep=" " , header=None)
        df = pd.read_csv("My WORDLE Log.txt" , sep=" " , header=None)
        _, ax = plt.subplots()
        sorted_dates = sorted(df.iloc[:,0].value_counts().to_dict().keys())
        fig1 = ax.bar(sorted_dates , [df.iloc[:,0].value_counts().to_dict()[value] for value in sorted_dates])
        plt.title("Gaming History" , size = 20)
        plt.xlabel("Dates" , size = 13)
        plt.ylabel("Frequency" , size = 13)
        plt.xticks(rotation=30 , size = 8)
        ax.bar_label(fig1, label_type='edge')
        plt.show();


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WORDLE = QtWidgets.QWidget()
    ui = Ui_WORDLE()
    ui.setupUi(WORDLE)
    WORDLE.show()
    sys.exit(app.exec_())
