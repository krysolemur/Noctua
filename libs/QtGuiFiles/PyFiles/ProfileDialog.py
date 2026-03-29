# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProfileDialog.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ProfileDialog(object):
    def setupUi(self, ProfileDialog):
        if not ProfileDialog.objectName():
            ProfileDialog.setObjectName(u"ProfileDialog")
        ProfileDialog.resize(400, 300)
        self.mainLayout = QVBoxLayout(ProfileDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.profileNameLayout = QVBoxLayout()
        self.profileNameLayout.setObjectName(u"profileNameLayout")
        self.nameLayout = QHBoxLayout()
        self.nameLayout.setObjectName(u"nameLayout")
        self.profileNameLabel = QLabel(ProfileDialog)
        self.profileNameLabel.setObjectName(u"profileNameLabel")

        self.nameLayout.addWidget(self.profileNameLabel)

        self.profileNameLineEdit = QLineEdit(ProfileDialog)
        self.profileNameLineEdit.setObjectName(u"profileNameLineEdit")

        self.nameLayout.addWidget(self.profileNameLineEdit)


        self.profileNameLayout.addLayout(self.nameLayout)

        self.statusLabel = QLabel(ProfileDialog)
        self.statusLabel.setObjectName(u"statusLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusLabel.sizePolicy().hasHeightForWidth())
        self.statusLabel.setSizePolicy(sizePolicy)
        self.statusLabel.setAlignment(Qt.AlignCenter)
        self.statusLabel.setIndent(0)

        self.profileNameLayout.addWidget(self.statusLabel)


        self.mainLayout.addLayout(self.profileNameLayout)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.cancelButton = QPushButton(ProfileDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.buttonsLayout.addWidget(self.cancelButton)

        self.createButton = QPushButton(ProfileDialog)
        self.createButton.setObjectName(u"createButton")

        self.buttonsLayout.addWidget(self.createButton)


        self.mainLayout.addLayout(self.buttonsLayout)


        self.retranslateUi(ProfileDialog)

        QMetaObject.connectSlotsByName(ProfileDialog)
    # setupUi

    def retranslateUi(self, ProfileDialog):
        ProfileDialog.setWindowTitle(QCoreApplication.translate("ProfileDialog", u"Dialog", None))
        self.profileNameLabel.setText(QCoreApplication.translate("ProfileDialog", u"Profile name: ", None))
        self.statusLabel.setText("")
        self.cancelButton.setText(QCoreApplication.translate("ProfileDialog", u"Cancel", None))
        self.createButton.setText(QCoreApplication.translate("ProfileDialog", u"Create", None))
    # retranslateUi

