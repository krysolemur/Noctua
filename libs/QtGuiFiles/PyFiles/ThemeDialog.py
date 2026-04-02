# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ThemeDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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

class Ui_ThemeDialog(object):
    def setupUi(self, ThemeDialog):
        if not ThemeDialog.objectName():
            ThemeDialog.setObjectName(u"ThemeDialog")
        ThemeDialog.resize(400, 300)
        self.mainLayout = QVBoxLayout(ThemeDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(3, 3, 3, 3)
        self.statusLabel = QLabel(ThemeDialog)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setAlignment(Qt.AlignCenter)

        self.mainLayout.addWidget(self.statusLabel)

        self.addLayout = QHBoxLayout()
        self.addLayout.setObjectName(u"addLayout")
        self.addLayout.setContentsMargins(3, 3, 3, 3)
        self.addLabel = QLabel(ThemeDialog)
        self.addLabel.setObjectName(u"addLabel")

        self.addLayout.addWidget(self.addLabel)

        self.addLineEdit = QLineEdit(ThemeDialog)
        self.addLineEdit.setObjectName(u"addLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addLineEdit.sizePolicy().hasHeightForWidth())
        self.addLineEdit.setSizePolicy(sizePolicy)

        self.addLayout.addWidget(self.addLineEdit)

        self.browseButton = QPushButton(ThemeDialog)
        self.browseButton.setObjectName(u"browseButton")
        sizePolicy.setHeightForWidth(self.browseButton.sizePolicy().hasHeightForWidth())
        self.browseButton.setSizePolicy(sizePolicy)

        self.addLayout.addWidget(self.browseButton)

        self.addButton = QPushButton(ThemeDialog)
        self.addButton.setObjectName(u"addButton")

        self.addLayout.addWidget(self.addButton)

        self.addLayout.setStretch(1, 1)

        self.mainLayout.addLayout(self.addLayout)


        self.retranslateUi(ThemeDialog)

        QMetaObject.connectSlotsByName(ThemeDialog)
    # setupUi

    def retranslateUi(self, ThemeDialog):
        ThemeDialog.setWindowTitle(QCoreApplication.translate("ThemeDialog", u"Dialog", None))
        self.statusLabel.setText("")
        self.addLabel.setText(QCoreApplication.translate("ThemeDialog", u"Path:", None))
        self.addLineEdit.setPlaceholderText(QCoreApplication.translate("ThemeDialog", u"path/to/your/stylesheet/file", None))
        self.browseButton.setText(QCoreApplication.translate("ThemeDialog", u"Browse", None))
        self.addButton.setText(QCoreApplication.translate("ThemeDialog", u"Add", None))
    # retranslateUi

