# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CrossedSwords/gamewindow.ui'
#
# Created: Tue Aug 07 20:13:19 2012
#      by: pyside-uic 0.2.14 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GameWindow(object):
    def setupUi(self, GameWindow):
        GameWindow.setObjectName("GameWindow")
        GameWindow.resize(524, 353)
        self.centralwidget = QtGui.QWidget(GameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.vLayTarget = QtGui.QVBoxLayout()
        self.vLayTarget.setObjectName("vLayTarget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblName = QtGui.QLabel(self.centralwidget)
        self.lblName.setObjectName("lblName")
        self.horizontalLayout_3.addWidget(self.lblName)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lblHeart = QtGui.QLabel(self.centralwidget)
        self.lblHeart.setText("")
        self.lblHeart.setPixmap(QtGui.QPixmap("images/Heart.png"))
        self.lblHeart.setObjectName("lblHeart")
        self.horizontalLayout_3.addWidget(self.lblHeart)
        self.lblHP = QtGui.QLabel(self.centralwidget)
        self.lblHP.setObjectName("lblHP")
        self.horizontalLayout_3.addWidget(self.lblHP)
        self.lblSword = QtGui.QLabel(self.centralwidget)
        self.lblSword.setText("")
        self.lblSword.setPixmap(QtGui.QPixmap("images/Swords.png"))
        self.lblSword.setObjectName("lblSword")
        self.horizontalLayout_3.addWidget(self.lblSword)
        self.lblVP = QtGui.QLabel(self.centralwidget)
        self.lblVP.setObjectName("lblVP")
        self.horizontalLayout_3.addWidget(self.lblVP)
        self.vLayTarget.addLayout(self.horizontalLayout_3)
        self.listPlayer = QtGui.QTableWidget(self.centralwidget)
        self.listPlayer.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listPlayer.setAlternatingRowColors(True)
        self.listPlayer.setObjectName("listPlayer")
        self.listPlayer.setColumnCount(3)
        self.listPlayer.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.listPlayer.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.listPlayer.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.listPlayer.setHorizontalHeaderItem(2, item)
        self.vLayTarget.addWidget(self.listPlayer)
        self.verticalLayout.addLayout(self.vLayTarget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.vLayActions = QtGui.QVBoxLayout()
        self.vLayActions.setObjectName("vLayActions")
        self.vLayAtk = QtGui.QVBoxLayout()
        self.vLayAtk.setObjectName("vLayAtk")
        self.btnStrike = QtGui.QPushButton(self.centralwidget)
        self.btnStrike.setStyleSheet("QPushButton \n"
"{\n"
"    color: black;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fbb, stop: 1 #daa);\n"
"    border-width: 1px;\n"
"    border-color: #333;\n"
"    border-style: solid;\n"
"    border-radius: 10px;\n"
"    padding: 3px;\n"
"    font-size: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 10px;\n"
"    min-height: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #daa, stop: 1 #fbb);\n"
"    border-style: inset;\n"
"    border-color: #633;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b88, stop: 1 #d99);\n"
"    border-style: inset;\n"
" }")
        self.btnStrike.setCheckable(False)
        self.btnStrike.setObjectName("btnStrike")
        self.btnGroupActions = QtGui.QButtonGroup(GameWindow)
        self.btnGroupActions.setObjectName("btnGroupActions")
        self.btnGroupActions.addButton(self.btnStrike)
        self.vLayAtk.addWidget(self.btnStrike)
        self.btnLunge = QtGui.QPushButton(self.centralwidget)
        self.btnLunge.setStyleSheet("QPushButton \n"
"{\n"
"    color: black;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fbb, stop: 1 #daa);\n"
"    border-width: 1px;\n"
"    border-color: #333;\n"
"    border-style: solid;\n"
"    border-radius: 10px;\n"
"    padding: 3px;\n"
"    font-size: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 10px;\n"
"    min-height: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #daa, stop: 1 #fbb);\n"
"    border-style: inset;\n"
"    border-color: #633;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b88, stop: 1 #d99);\n"
"    border-style: inset;\n"
" }")
        self.btnLunge.setCheckable(False)
        self.btnLunge.setObjectName("btnLunge")
        self.btnGroupActions.addButton(self.btnLunge)
        self.vLayAtk.addWidget(self.btnLunge)
        self.btnAssail = QtGui.QPushButton(self.centralwidget)
        self.btnAssail.setStyleSheet("QPushButton \n"
"{\n"
"    color: black;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fbb, stop: 1 #daa);\n"
"    border-width: 1px;\n"
"    border-color: #333;\n"
"    border-style: solid;\n"
"    border-radius: 10px;\n"
"    padding: 3px;\n"
"    font-size: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 10px;\n"
"    min-height: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #daa, stop: 1 #fbb);\n"
"    border-style: inset;\n"
"    border-color: #633;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #b88, stop: 1 #d99);\n"
"    border-style: inset;\n"
" }")
        self.btnAssail.setCheckable(False)
        self.btnAssail.setObjectName("btnAssail")
        self.btnGroupActions.addButton(self.btnAssail)
        self.vLayAtk.addWidget(self.btnAssail)
        self.vLayActions.addLayout(self.vLayAtk)
        self.vLayDef = QtGui.QVBoxLayout()
        self.vLayDef.setObjectName("vLayDef")
        self.btnDodge = QtGui.QPushButton(self.centralwidget)
        self.btnDodge.setStyleSheet("QPushButton \n"
"{\n"
"    color: black;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #bfb, stop: 1 #ada);\n"
"    border-width: 1px;\n"
"    border-color: #333;\n"
"    border-style: solid;\n"
"    border-radius: 10px;\n"
"    padding: 3px;\n"
"    font-size: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 10px;\n"
"    min-height: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ada, stop: 1 #bfb);\n"
"    border-style: inset;\n"
"    border-color: #363;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #8b8, stop: 1 #9d9);\n"
"    border-style: inset;\n"
" }")
        self.btnDodge.setCheckable(False)
        self.btnDodge.setObjectName("btnDodge")
        self.btnGroupActions.addButton(self.btnDodge)
        self.vLayDef.addWidget(self.btnDodge)
        self.btnBlock = QtGui.QPushButton(self.centralwidget)
        self.btnBlock.setStyleSheet("QPushButton \n"
"{\n"
"    color: black;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #bfb, stop: 1 #ada);\n"
"    border-width: 1px;\n"
"    border-color: #333;\n"
"    border-style: solid;\n"
"    border-radius: 10px;\n"
"    padding: 3px;\n"
"    font-size: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 10px;\n"
"    min-height: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ada, stop: 1 #bfb);\n"
"    border-style: inset;\n"
"    border-color: #363;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #8b8, stop: 1 #9d9);\n"
"    border-style: inset;\n"
" }")
        self.btnBlock.setCheckable(False)
        self.btnBlock.setObjectName("btnBlock")
        self.btnGroupActions.addButton(self.btnBlock)
        self.vLayDef.addWidget(self.btnBlock)
        self.btnRiposte = QtGui.QPushButton(self.centralwidget)
        self.btnRiposte.setStyleSheet("QPushButton \n"
"{\n"
"    color: black;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #bfb, stop: 1 #ada);\n"
"    border-width: 1px;\n"
"    border-color: #333;\n"
"    border-style: solid;\n"
"    border-radius: 10px;\n"
"    padding: 3px;\n"
"    font-size: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 10px;\n"
"    min-height: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ada, stop: 1 #bfb);\n"
"    border-style: inset;\n"
"    border-color: #363;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #8b8, stop: 1 #9d9);\n"
"    border-style: inset;\n"
" }")
        self.btnRiposte.setCheckable(False)
        self.btnRiposte.setObjectName("btnRiposte")
        self.btnGroupActions.addButton(self.btnRiposte)
        self.vLayDef.addWidget(self.btnRiposte)
        self.vLayActions.addLayout(self.vLayDef)
        self.vLayAct = QtGui.QVBoxLayout()
        self.vLayAct.setObjectName("vLayAct")
        self.btnTaunt = QtGui.QPushButton(self.centralwidget)
        self.btnTaunt.setStyleSheet("QPushButton \n"
"{\n"
"    color: black;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #bbf, stop: 1 #aad);\n"
"    border-width: 1px;\n"
"    border-color: #333;\n"
"    border-style: solid;\n"
"    border-radius: 10px;\n"
"    padding: 3px;\n"
"    font-size: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 10px;\n"
"    min-height: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #aad, stop: 1 #bbf);\n"
"    border-style: inset;\n"
"    border-color: #336;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88b, stop: 1 #99d);\n"
"    border-style: inset;\n"
" }")
        self.btnTaunt.setCheckable(False)
        self.btnTaunt.setObjectName("btnTaunt")
        self.btnGroupActions.addButton(self.btnTaunt)
        self.vLayAct.addWidget(self.btnTaunt)
        self.btnFocus = QtGui.QPushButton(self.centralwidget)
        self.btnFocus.setStyleSheet("QPushButton \n"
"{\n"
"    color: black;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #bbf, stop: 1 #aad);\n"
"    border-width: 1px;\n"
"    border-color: #333;\n"
"    border-style: solid;\n"
"    border-radius: 10px;\n"
"    padding: 3px;\n"
"    font-size: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 10px;\n"
"    min-height: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #aad, stop: 1 #bbf);\n"
"    border-style: inset;\n"
"    border-color: #336;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88b, stop: 1 #99d);\n"
"    border-style: inset;\n"
" }")
        self.btnFocus.setCheckable(False)
        self.btnFocus.setObjectName("btnFocus")
        self.btnGroupActions.addButton(self.btnFocus)
        self.vLayAct.addWidget(self.btnFocus)
        self.btnMend = QtGui.QPushButton(self.centralwidget)
        self.btnMend.setStyleSheet("QPushButton \n"
"{\n"
"    color: black;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #bbf, stop: 1 #aad);\n"
"    border-width: 1px;\n"
"    border-color: #333;\n"
"    border-style: solid;\n"
"    border-radius: 10px;\n"
"    padding: 3px;\n"
"    font-size: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 10px;\n"
"    min-height: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #aad, stop: 1 #bbf);\n"
"    border-style: inset;\n"
"    border-color: #336;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88b, stop: 1 #99d);\n"
"    border-style: inset;\n"
" }")
        self.btnMend.setCheckable(False)
        self.btnMend.setObjectName("btnMend")
        self.btnGroupActions.addButton(self.btnMend)
        self.vLayAct.addWidget(self.btnMend)
        self.btnHalt = QtGui.QPushButton(self.centralwidget)
        self.btnHalt.setStyleSheet("QPushButton \n"
"{\n"
"    color: black;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #bbf, stop: 1 #aad);\n"
"    border-width: 1px;\n"
"    border-color: #333;\n"
"    border-style: solid;\n"
"    border-radius: 10px;\n"
"    padding: 3px;\n"
"    font-size: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 60px;\n"
"    min-height: 10px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #aad, stop: 1 #bbf);\n"
"    border-style: inset;\n"
"    border-color: #336;\n"
"}\n"
"\n"
"QPushButton:pressed \n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #88b, stop: 1 #99d);\n"
"    border-style: inset;\n"
" }")
        self.btnHalt.setCheckable(False)
        self.btnHalt.setObjectName("btnHalt")
        self.btnGroupActions.addButton(self.btnHalt)
        self.vLayAct.addWidget(self.btnHalt)
        self.vLayActions.addLayout(self.vLayAct)
        self.horizontalLayout_2.addLayout(self.vLayActions)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        GameWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GameWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        GameWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GameWindow)
        self.statusbar.setObjectName("statusbar")
        GameWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(GameWindow)
        QtCore.QMetaObject.connectSlotsByName(GameWindow)

    def retranslateUi(self, GameWindow):
        GameWindow.setWindowTitle(QtGui.QApplication.translate("GameWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.lblName.setText(QtGui.QApplication.translate("GameWindow", "Player", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHP.setText(QtGui.QApplication.translate("GameWindow", "HP", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVP.setText(QtGui.QApplication.translate("GameWindow", "VP", None, QtGui.QApplication.UnicodeUTF8))
        self.listPlayer.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("GameWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.listPlayer.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("GameWindow", "HP", None, QtGui.QApplication.UnicodeUTF8))
        self.listPlayer.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("GameWindow", "VP", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStrike.setText(QtGui.QApplication.translate("GameWindow", "Strike", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLunge.setText(QtGui.QApplication.translate("GameWindow", "Lunge", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAssail.setText(QtGui.QApplication.translate("GameWindow", "Assail", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDodge.setText(QtGui.QApplication.translate("GameWindow", "Dodge", None, QtGui.QApplication.UnicodeUTF8))
        self.btnBlock.setText(QtGui.QApplication.translate("GameWindow", "Block", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRiposte.setText(QtGui.QApplication.translate("GameWindow", "Riposte", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTaunt.setText(QtGui.QApplication.translate("GameWindow", "Taunt", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFocus.setText(QtGui.QApplication.translate("GameWindow", "Focus", None, QtGui.QApplication.UnicodeUTF8))
        self.btnMend.setText(QtGui.QApplication.translate("GameWindow", "Mend", None, QtGui.QApplication.UnicodeUTF8))
        self.btnHalt.setText(QtGui.QApplication.translate("GameWindow", "Halt", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("GameWindow", "File", None, QtGui.QApplication.UnicodeUTF8))

