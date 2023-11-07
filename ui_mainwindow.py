# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLCDNumber,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(725, 552)

        # I tweaked the colors behind the click count LCDs to look better in dark mode
        # on MacOS Monterey. If you're not using dark mode, change darkMode to False and
        # it will probably look better on your machine.
        darkMode = True
        if darkMode:
            MainWindow.setStyleSheet(u"QLCDNumber#totalClicksLcd,\n"
                "QLCDNumber#majDeductTotalLcd {\n"
                "	background-color: rgb(65	, 65, 65)\n"
                "}\n"
                "\n"
                "QLCDNumber#plusClicksLcd {\n"
                "	background-color: rgb(65, 80, 65)\n"
                "}\n"
                "\n"
                "QLCDNumber#minusClicksLcd {\n"
                "	background-color: rgb(85, 65, 65)\n"
                "}\n"
                "\n"
                "QLCDNumber#majDeductLv1Lcd {\n"
                "	background-color: rgb(85, 65, 65)\n"
                "}\n"
                "\n"
                "QLCDNumber#majDeductLv2Lcd {\n"
                "	background-color: rgb(85, 60, 60)\n"
                "}\n"
                "\n"
                "QLCDNumber#majDeductLv3Lcd {\n"
                "	background-color: rgb(87, 58, 58)\n"
                "}\n"
                "\n"
                "QLabel#totalClicksLabel,\n"
                "QLabel#majDeductTotalLabel {\n"
                "	font-weight: bold\n"
                "}")
        else:
            MainWindow.setStyleSheet(u"QLCDNumber#totalClicksLcd,\n"
                "QLCDNumber#majDeductTotalLcd {\n"
                "	background-color: rgb(240	, 240, 240)\n"
                "}\n"
                "\n"
                "QLCDNumber#plusClicksLcd {\n"
                "	background-color: rgb(210, 230, 210)\n"
                "}\n"
                "\n"
                "QLCDNumber#minusClicksLcd {\n"
                "	background-color: rgb(230, 210, 210)\n"
                "}\n"
                "\n"
                "QLCDNumber#majDeductLv1Lcd {\n"
                "	background-color: rgb(230, 205, 205)\n"
                "}\n"
                "\n"
                "QLCDNumber#majDeductLv2Lcd {\n"
                "	background-color: rgb(220, 190, 190)\n"
                "}\n"
                "\n"
                "QLCDNumber#majDeductLv3Lcd {\n"
                "	background-color: rgb(205, 175, 175)\n"
                "}\n"
                "\n"
                "QLabel#totalClicksLabel,\n"
                "QLabel#majDeductTotalLabel {\n"
                "	font-weight: bold\n"
                "}")

        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionUndoReset = QAction(MainWindow)
        self.actionUndoReset.setObjectName(u"actionUndoReset")
        self.actionUndoReset.setEnabled(False)
        self.actionPrefs = QAction(MainWindow)
        self.actionPrefs.setObjectName(u"actionPrefs")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.timerLayout = QHBoxLayout()
        self.timerLayout.setObjectName(u"timerLayout")
        self.timeElapsedLayout = QVBoxLayout()
        self.timeElapsedLayout.setObjectName(u"timeElapsedLayout")
        self.timeElapsedLabel = QLabel(self.centralwidget)
        self.timeElapsedLabel.setObjectName(u"timeElapsedLabel")
        self.timeElapsedLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.timeElapsedLayout.addWidget(self.timeElapsedLabel)

        self.timeElapsedLcd = QLCDNumber(self.centralwidget)
        self.timeElapsedLcd.setObjectName(u"timeElapsedLcd")
        self.timeElapsedLcd.setMinimumSize(QSize(0, 80))
        self.timeElapsedLcd.setDigitCount(8)

        self.timeElapsedLayout.addWidget(self.timeElapsedLcd)


        self.timerLayout.addLayout(self.timeElapsedLayout)

        self.timeRemainingLayout = QVBoxLayout()
        self.timeRemainingLayout.setObjectName(u"timeRemainingLayout")
        self.timeRemainingLabel = QLabel(self.centralwidget)
        self.timeRemainingLabel.setObjectName(u"timeRemainingLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeRemainingLabel.sizePolicy().hasHeightForWidth())
        self.timeRemainingLabel.setSizePolicy(sizePolicy)
        self.timeRemainingLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.timeRemainingLayout.addWidget(self.timeRemainingLabel)

        self.timeRemainingLcd = QLCDNumber(self.centralwidget)
        self.timeRemainingLcd.setObjectName(u"timeRemainingLcd")
        self.timeRemainingLcd.setMinimumSize(QSize(0, 80))
        self.timeRemainingLcd.setDigitCount(8)

        self.timeRemainingLayout.addWidget(self.timeRemainingLcd)


        self.timerLayout.addLayout(self.timeRemainingLayout)


        self.verticalLayout.addLayout(self.timerLayout)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_13 = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_13)

        self.timerDivider = QFrame(self.centralwidget)
        self.timerDivider.setObjectName(u"timerDivider")
        self.timerDivider.setFrameShadow(QFrame.Raised)
        self.timerDivider.setLineWidth(3)
        self.timerDivider.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.timerDivider)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.minusClicksVLayout = QVBoxLayout()
        self.minusClicksVLayout.setObjectName(u"minusClicksVLayout")
        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.minusClicksVLayout.addItem(self.verticalSpacer)

        self.minusClicksLabel = QLabel(self.centralwidget)
        self.minusClicksLabel.setObjectName(u"minusClicksLabel")
        self.minusClicksLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.minusClicksVLayout.addWidget(self.minusClicksLabel)

        self.minusClicksInstructionLabel = QLabel(self.centralwidget)
        self.minusClicksInstructionLabel.setObjectName(u"minusClicksInstructionLabel")
        self.minusClicksInstructionLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.minusClicksVLayout.addWidget(self.minusClicksInstructionLabel)

        self.minusClicksLcd = QLCDNumber(self.centralwidget)
        self.minusClicksLcd.setObjectName(u"minusClicksLcd")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.minusClicksLcd.sizePolicy().hasHeightForWidth())
        self.minusClicksLcd.setSizePolicy(sizePolicy1)
        self.minusClicksLcd.setMinimumSize(QSize(0, 120))
        self.minusClicksLcd.setDigitCount(4)

        self.minusClicksVLayout.addWidget(self.minusClicksLcd)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.minusClicksVLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.minusClicksVLayout)

        self.plusClicksVLayout = QVBoxLayout()
        self.plusClicksVLayout.setObjectName(u"plusClicksVLayout")
        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.plusClicksVLayout.addItem(self.verticalSpacer_5)

        self.plusClicksLabel = QLabel(self.centralwidget)
        self.plusClicksLabel.setObjectName(u"plusClicksLabel")
        self.plusClicksLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.plusClicksVLayout.addWidget(self.plusClicksLabel)

        self.plusClicksInstructionLabel = QLabel(self.centralwidget)
        self.plusClicksInstructionLabel.setObjectName(u"plusClicksInstructionLabel")
        self.plusClicksInstructionLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.plusClicksVLayout.addWidget(self.plusClicksInstructionLabel)

        self.plusClicksLcd = QLCDNumber(self.centralwidget)
        self.plusClicksLcd.setObjectName(u"plusClicksLcd")
        sizePolicy1.setHeightForWidth(self.plusClicksLcd.sizePolicy().hasHeightForWidth())
        self.plusClicksLcd.setSizePolicy(sizePolicy1)
        self.plusClicksLcd.setMinimumSize(QSize(0, 120))
        self.plusClicksLcd.setDigitCount(4)

        self.plusClicksVLayout.addWidget(self.plusClicksLcd)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.plusClicksVLayout.addItem(self.verticalSpacer_6)


        self.horizontalLayout.addLayout(self.plusClicksVLayout)

        self.totalClicksVLayout = QVBoxLayout()
        self.totalClicksVLayout.setObjectName(u"totalClicksVLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.totalClicksVLayout.addItem(self.verticalSpacer_3)

        self.totalClicksLabel = QLabel(self.centralwidget)
        self.totalClicksLabel.setObjectName(u"totalClicksLabel")
        self.totalClicksLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.totalClicksVLayout.addWidget(self.totalClicksLabel)

        self.totalClicksInstructionLabel = QLabel(self.centralwidget)
        self.totalClicksInstructionLabel.setObjectName(u"totalClicksInstructionLabel")
        self.totalClicksInstructionLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.totalClicksVLayout.addWidget(self.totalClicksInstructionLabel)

        self.totalClicksLcd = QLCDNumber(self.centralwidget)
        self.totalClicksLcd.setObjectName(u"totalClicksLcd")
        sizePolicy1.setHeightForWidth(self.totalClicksLcd.sizePolicy().hasHeightForWidth())
        self.totalClicksLcd.setSizePolicy(sizePolicy1)
        self.totalClicksLcd.setMinimumSize(QSize(0, 120))
        self.totalClicksLcd.setFrameShape(QFrame.Panel)
        self.totalClicksLcd.setFrameShadow(QFrame.Raised)
        self.totalClicksLcd.setLineWidth(3)
        self.totalClicksLcd.setDigitCount(4)

        self.totalClicksVLayout.addWidget(self.totalClicksLcd)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.totalClicksVLayout.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addLayout(self.totalClicksVLayout)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.majDeductLv1Layout = QVBoxLayout()
        self.majDeductLv1Layout.setObjectName(u"majDeductLv1Layout")
        self.majDeductLv1Label = QLabel(self.centralwidget)
        self.majDeductLv1Label.setObjectName(u"majDeductLv1Label")
        self.majDeductLv1Label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.majDeductLv1Layout.addWidget(self.majDeductLv1Label)

        self.majDeductLv1Lcd = QLCDNumber(self.centralwidget)
        self.majDeductLv1Lcd.setObjectName(u"majDeductLv1Lcd")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.majDeductLv1Lcd.sizePolicy().hasHeightForWidth())
        self.majDeductLv1Lcd.setSizePolicy(sizePolicy2)
        self.majDeductLv1Lcd.setMinimumSize(QSize(0, 100))
        self.majDeductLv1Lcd.setDigitCount(2)

        self.majDeductLv1Layout.addWidget(self.majDeductLv1Lcd)


        self.horizontalLayout_3.addLayout(self.majDeductLv1Layout)

        self.majDeductLv2Layout = QVBoxLayout()
        self.majDeductLv2Layout.setObjectName(u"majDeductLv2Layout")
        self.majDeductLv2Label = QLabel(self.centralwidget)
        self.majDeductLv2Label.setObjectName(u"majDeductLv2Label")
        self.majDeductLv2Label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.majDeductLv2Layout.addWidget(self.majDeductLv2Label)

        self.majDeductLv2Lcd = QLCDNumber(self.centralwidget)
        self.majDeductLv2Lcd.setObjectName(u"majDeductLv2Lcd")
        sizePolicy2.setHeightForWidth(self.majDeductLv2Lcd.sizePolicy().hasHeightForWidth())
        self.majDeductLv2Lcd.setSizePolicy(sizePolicy2)
        self.majDeductLv2Lcd.setMinimumSize(QSize(0, 100))
        self.majDeductLv2Lcd.setDigitCount(2)

        self.majDeductLv2Layout.addWidget(self.majDeductLv2Lcd)


        self.horizontalLayout_3.addLayout(self.majDeductLv2Layout)

        self.majDeductLv3Layout = QVBoxLayout()
        self.majDeductLv3Layout.setObjectName(u"majDeductLv3Layout")
        self.majDeductLv3Label = QLabel(self.centralwidget)
        self.majDeductLv3Label.setObjectName(u"majDeductLv3Label")
        self.majDeductLv3Label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.majDeductLv3Layout.addWidget(self.majDeductLv3Label)

        self.majDeductLv3Lcd = QLCDNumber(self.centralwidget)
        self.majDeductLv3Lcd.setObjectName(u"majDeductLv3Lcd")
        sizePolicy2.setHeightForWidth(self.majDeductLv3Lcd.sizePolicy().hasHeightForWidth())
        self.majDeductLv3Lcd.setSizePolicy(sizePolicy2)
        self.majDeductLv3Lcd.setMinimumSize(QSize(0, 100))
        self.majDeductLv3Lcd.setDigitCount(2)

        self.majDeductLv3Layout.addWidget(self.majDeductLv3Lcd)


        self.horizontalLayout_3.addLayout(self.majDeductLv3Layout)

        self.majDeductTotalLayout = QVBoxLayout()
        self.majDeductTotalLayout.setObjectName(u"majDeductTotalLayout")
        self.majDeductTotalLabel = QLabel(self.centralwidget)
        self.majDeductTotalLabel.setObjectName(u"majDeductTotalLabel")
        self.majDeductTotalLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.majDeductTotalLayout.addWidget(self.majDeductTotalLabel)

        self.majDeductTotalLcd = QLCDNumber(self.centralwidget)
        self.majDeductTotalLcd.setObjectName(u"majDeductTotalLcd")
        sizePolicy2.setHeightForWidth(self.majDeductTotalLcd.sizePolicy().hasHeightForWidth())
        self.majDeductTotalLcd.setSizePolicy(sizePolicy2)
        self.majDeductTotalLcd.setMinimumSize(QSize(0, 100))
        self.majDeductTotalLcd.setFrameShape(QFrame.Panel)
        self.majDeductTotalLcd.setLineWidth(3)
        self.majDeductTotalLcd.setDigitCount(2)

        self.majDeductTotalLayout.addWidget(self.majDeductTotalLcd)


        self.horizontalLayout_3.addLayout(self.majDeductTotalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 725, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionPrefs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionUndoReset)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionUndoReset.setText(QCoreApplication.translate("MainWindow", u"&Undo reset", None))
#if QT_CONFIG(shortcut)
        self.actionUndoReset.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+U", None))
#endif // QT_CONFIG(shortcut)
        self.actionPrefs.setText(QCoreApplication.translate("MainWindow", u"&Preferences...", None))
        self.timeElapsedLabel.setText(QCoreApplication.translate("MainWindow", u"Time elapsed", None))
        self.timeRemainingLabel.setText(QCoreApplication.translate("MainWindow", u"Time remaining", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Timer: [Q] Start/Pause, [W] Reset", None))
        self.minusClicksLabel.setText(QCoreApplication.translate("MainWindow", u"Negative click score", None))
        self.minusClicksInstructionLabel.setText(QCoreApplication.translate("MainWindow", u"[Z] -1, [X] -3", None))
        self.plusClicksLabel.setText(QCoreApplication.translate("MainWindow", u"Positive click score", None))
        self.plusClicksInstructionLabel.setText(QCoreApplication.translate("MainWindow", u"[/] +1, [.] +3", None))
        self.totalClicksLabel.setText(QCoreApplication.translate("MainWindow", u"Total click score", None))
        self.totalClicksInstructionLabel.setText(QCoreApplication.translate("MainWindow", u"[R] Reset all clicks", None))
        self.majDeductLv1Label.setText(QCoreApplication.translate("MainWindow", u"[A] Restart", None))
        self.majDeductLv2Label.setText(QCoreApplication.translate("MainWindow", u"[S] Switch", None))
        self.majDeductLv3Label.setText(QCoreApplication.translate("MainWindow", u"[D] Detach", None))
        self.majDeductTotalLabel.setText(QCoreApplication.translate("MainWindow", u"Total major deducts", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"&Edit", None))
    # retranslateUi

