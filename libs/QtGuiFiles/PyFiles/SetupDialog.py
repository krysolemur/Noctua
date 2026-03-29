# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SetupDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_setupDialog(object):
    def setupUi(self, setupDialog):
        if not setupDialog.objectName():
            setupDialog.setObjectName(u"setupDialog")
        setupDialog.resize(400, 300)
        self.mainLayout = QVBoxLayout(setupDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.loadingBar = QProgressBar(setupDialog)
        self.loadingBar.setObjectName(u"loadingBar")
        self.loadingBar.setValue(0)

        self.mainLayout.addWidget(self.loadingBar)

        self.setupLayout = QHBoxLayout()
        self.setupLayout.setObjectName(u"setupLayout")
        self.loadingLabel = QLabel(setupDialog)
        self.loadingLabel.setObjectName(u"loadingLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadingLabel.sizePolicy().hasHeightForWidth())
        self.loadingLabel.setSizePolicy(sizePolicy)

        self.setupLayout.addWidget(self.loadingLabel)

        self.statusLabel = QLabel(setupDialog)
        self.statusLabel.setObjectName(u"statusLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.statusLabel.sizePolicy().hasHeightForWidth())
        self.statusLabel.setSizePolicy(sizePolicy1)

        self.setupLayout.addWidget(self.statusLabel)


        self.mainLayout.addLayout(self.setupLayout)

        self.loginLayout = QVBoxLayout()
        self.loginLayout.setObjectName(u"loginLayout")

        self.mainLayout.addLayout(self.loginLayout)


        self.retranslateUi(setupDialog)

        QMetaObject.connectSlotsByName(setupDialog)
    # setupUi

    def retranslateUi(self, setupDialog):
        setupDialog.setWindowTitle(QCoreApplication.translate("setupDialog", u"Dialog", None))
        self.loadingLabel.setText("")
        self.statusLabel.setText("")
    # retranslateUi

