# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CrossedSwords/mainwindow.ui'
#
# Created: Tue Aug 07 20:17:30 2012
#      by: pyside-uic 0.2.14 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 524)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.splashimage = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splashimage.sizePolicy().hasHeightForWidth())
        self.splashimage.setSizePolicy(sizePolicy)
        self.splashimage.setText("")
        self.splashimage.setObjectName("splashimage")
        self.horizontalLayout_4.addWidget(self.splashimage)
        self.textEdit = QtGui.QTextEdit(self.centralWidget)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_4.addWidget(self.textEdit)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnAddHuman = QtGui.QPushButton(self.centralWidget)
        self.btnAddHuman.setObjectName("btnAddHuman")
        self.horizontalLayout_3.addWidget(self.btnAddHuman)
        self.btnAddAI = QtGui.QPushButton(self.centralWidget)
        self.btnAddAI.setObjectName("btnAddAI")
        self.horizontalLayout_3.addWidget(self.btnAddAI)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblName = QtGui.QLabel(self.centralWidget)
        self.lblName.setObjectName("lblName")
        self.horizontalLayout.addWidget(self.lblName)
        self.leName = QtGui.QLineEdit(self.centralWidget)
        self.leName.setObjectName("leName")
        self.horizontalLayout.addWidget(self.leName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listPlayer = QtGui.QListView(self.centralWidget)
        self.listPlayer.setObjectName("listPlayer")
        self.verticalLayout_2.addWidget(self.listPlayer)
        self.btnStart = QtGui.QPushButton(self.centralWidget)
        self.btnStart.setObjectName("btnStart")
        self.verticalLayout_2.addWidget(self.btnStart)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.btnQuit = QtGui.QPushButton(self.centralWidget)
        self.btnQuit.setObjectName("btnQuit")
        self.gridLayout.addWidget(self.btnQuit, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 783, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The rules are simple.  Every player has 10 moves to choose from, and starts with 20 HP and 0 VP.  Every turn, each player chooses a move, and which player he will target with it, and he PMs the move to the host.  Once all of the players have selected the host receives all of the player\'s moves and targets, he reveals all of the moves and targets to everyone, and all calculations of damage are made.  For every point of damage dealt to a player, one of their HPs is moved to the VP pool of the player that dealt the damage.  When only one player is left, that player moves all of his life counters over to his VP pool.  All players then count up their VP, and the player with the most VP wins. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Strike: (Attack) - Deal 3 damage to target player.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Lunge: (Attack) - Deal 5 damage to target player.  If that player damages you this turn, he deals 3 additional damage to you -- plus 6 MORE damage if you were Focused on him.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Assail: (Attack) - Deal 1 damage to every player.  Target player\'s Defense moves cannot reduce this damage. You cannot gain more than 8 VP from this move on any one turn. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Dodge: (Defense) - Target player\'s (Attack) moves deal no damage to you this turn, and 3 less damage to you next turn.  All other (Attack) moves deal 3 less damage to you this turn.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Block: (Defense) - All (Attack) moves deal 2 less damage to you this turn.  If target player targets you with an (Attack) move this turn, deal 2 damage to him.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Riposte: (Defense) - If target player targets you with an (Attack) move this turn, it\'s damage is reduced to zero, and you deal 3 damage to him.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Taunt: (Action) - Steal 3 counters from target player\'s Victory Pool.  All other player\'s (Attack) moves deal 1 extra damage to you this turn. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Focus: (Action) - If you use an (Attack) move on target player next turn, you deal twice your normal damage, plus one.  (Damage-reducing effects apply after Focus is applied.)   </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Mend: (Action) - Add 3 counters to target player\'s Life Pool -- or 7 counters if you Focused last turn (regardless of the target of your Focus).  Gain 1 Victory Point.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Halt: (Action) - If target player plays an (Action) move, you deal 3 damage to him or her and negate the effect of the (Action) he played.  If two or more players Halt each other in a loop at the same time, nothing happens.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddHuman.setText(QtGui.QApplication.translate("MainWindow", "Add Hotseat Player", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddAI.setText(QtGui.QApplication.translate("MainWindow", "Add AI Player", None, QtGui.QApplication.UnicodeUTF8))
        self.lblName.setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStart.setText(QtGui.QApplication.translate("MainWindow", "Start Game", None, QtGui.QApplication.UnicodeUTF8))
        self.btnQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

