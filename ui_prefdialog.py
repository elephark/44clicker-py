# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prefdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_PrefDialog(object):
    def setupUi(self, PrefDialog):
        if not PrefDialog.objectName():
            PrefDialog.setObjectName(u"PrefDialog")
        PrefDialog.resize(557, 447)
        self.verticalLayout_2 = QVBoxLayout(PrefDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.md1Layout = QHBoxLayout()
        self.md1Layout.setObjectName(u"md1Layout")
        self.md1Label = QLabel(PrefDialog)
        self.md1Label.setObjectName(u"md1Label")

        self.md1Layout.addWidget(self.md1Label)

        self.md1SpinBox = QSpinBox(PrefDialog)
        self.md1SpinBox.setObjectName(u"md1SpinBox")

        self.md1Layout.addWidget(self.md1SpinBox)


        self.verticalLayout.addLayout(self.md1Layout)

        self.md2Layout = QHBoxLayout()
        self.md2Layout.setObjectName(u"md2Layout")
        self.md2Label = QLabel(PrefDialog)
        self.md2Label.setObjectName(u"md2Label")

        self.md2Layout.addWidget(self.md2Label)

        self.md2SpinBox = QSpinBox(PrefDialog)
        self.md2SpinBox.setObjectName(u"md2SpinBox")

        self.md2Layout.addWidget(self.md2SpinBox)


        self.verticalLayout.addLayout(self.md2Layout)

        self.md3Layout = QHBoxLayout()
        self.md3Layout.setObjectName(u"md3Layout")
        self.md3Label = QLabel(PrefDialog)
        self.md3Label.setObjectName(u"md3Label")

        self.md3Layout.addWidget(self.md3Label)

        self.md3SpinBox = QSpinBox(PrefDialog)
        self.md3SpinBox.setObjectName(u"md3SpinBox")

        self.md3Layout.addWidget(self.md3SpinBox)


        self.verticalLayout.addLayout(self.md3Layout)

        self.multiClickLayout = QHBoxLayout()
        self.multiClickLayout.setObjectName(u"multiClickLayout")
        self.multiClickLabel = QLabel(PrefDialog)
        self.multiClickLabel.setObjectName(u"multiClickLabel")

        self.multiClickLayout.addWidget(self.multiClickLabel)

        self.multiClickSpinBox = QSpinBox(PrefDialog)
        self.multiClickSpinBox.setObjectName(u"multiClickSpinBox")

        self.multiClickLayout.addWidget(self.multiClickSpinBox)


        self.verticalLayout.addLayout(self.multiClickLayout)

        self.totalTimeLayout = QHBoxLayout()
        self.totalTimeLayout.setObjectName(u"totalTimeLayout")
        self.totalTimeLabel = QLabel(PrefDialog)
        self.totalTimeLabel.setObjectName(u"totalTimeLabel")

        self.totalTimeLayout.addWidget(self.totalTimeLabel)

        self.totalTimeSpinBox = QSpinBox(PrefDialog)
        self.totalTimeSpinBox.setObjectName(u"totalTimeSpinBox")

        self.totalTimeLayout.addWidget(self.totalTimeSpinBox)


        self.verticalLayout.addLayout(self.totalTimeLayout)

        self.timerDigitsLayout = QHBoxLayout()
        self.timerDigitsLayout.setObjectName(u"timerDigitsLayout")
        self.timerDigitsLabel = QLabel(PrefDialog)
        self.timerDigitsLabel.setObjectName(u"timerDigitsLabel")

        self.timerDigitsLayout.addWidget(self.timerDigitsLabel)

        self.timerDigitsSpinBox = QSpinBox(PrefDialog)
        self.timerDigitsSpinBox.setObjectName(u"timerDigitsSpinBox")

        self.timerDigitsLayout.addWidget(self.timerDigitsSpinBox)


        self.verticalLayout.addLayout(self.timerDigitsLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(PrefDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok|QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(PrefDialog)
        self.buttonBox.accepted.connect(PrefDialog.accept)
        self.buttonBox.rejected.connect(PrefDialog.reject)

        QMetaObject.connectSlotsByName(PrefDialog)
    # setupUi

    def retranslateUi(self, PrefDialog):
        PrefDialog.setWindowTitle(QCoreApplication.translate("PrefDialog", u"Dialog", None))
        self.md1Label.setText(QCoreApplication.translate("PrefDialog", u"MajDeduct Lv1 (restart) value", None))
        self.md2Label.setText(QCoreApplication.translate("PrefDialog", u"MajDeduct Lv2 (switch) value", None))
        self.md3Label.setText(QCoreApplication.translate("PrefDialog", u"MajDeduct Lv3 (detach) value", None))
        self.multiClickLabel.setText(QCoreApplication.translate("PrefDialog", u"Multi-click value", None))
        self.totalTimeLabel.setText(QCoreApplication.translate("PrefDialog", u"Freestyle length (seconds)", None))
        self.timerDigitsLabel.setText(QCoreApplication.translate("PrefDialog", u"Timer digits for partial seconds", None))
    # retranslateUi

