# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CustomDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_customDialog(object):
    def setupUi(self, customDialog):
        if not customDialog.objectName():
            customDialog.setObjectName(u"customDialog")
        customDialog.resize(400, 300)
        self.mainLayout = QVBoxLayout(customDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.textLabel = QLabel(customDialog)
        self.textLabel.setObjectName(u"textLabel")

        self.mainLayout.addWidget(self.textLabel)

        self.showDialogCheckBox = QCheckBox(customDialog)
        self.showDialogCheckBox.setObjectName(u"showDialogCheckBox")

        self.mainLayout.addWidget(self.showDialogCheckBox)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.cancelButton = QPushButton(customDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.buttonsLayout.addWidget(self.cancelButton)

        self.sumbitButton = QPushButton(customDialog)
        self.sumbitButton.setObjectName(u"sumbitButton")

        self.buttonsLayout.addWidget(self.sumbitButton)


        self.mainLayout.addLayout(self.buttonsLayout)


        self.retranslateUi(customDialog)

        QMetaObject.connectSlotsByName(customDialog)
    # setupUi

    def retranslateUi(self, customDialog):
        customDialog.setWindowTitle(QCoreApplication.translate("customDialog", u"Dialog", None))
        self.textLabel.setText("")
        self.showDialogCheckBox.setText(QCoreApplication.translate("customDialog", u"Don't ask me again.", None))
        self.cancelButton.setText("")
        self.sumbitButton.setText("")
    # retranslateUi

