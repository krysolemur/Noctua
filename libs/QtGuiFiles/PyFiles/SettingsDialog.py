# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDialog.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDialog,
    QFontComboBox, QFrame, QHBoxLayout, QLabel,
    QLayout, QListWidget, QListWidgetItem, QPushButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(632, 560)
        SettingsDialog.setContextMenuPolicy(Qt.NoContextMenu)
        self.mainLayout = QVBoxLayout(SettingsDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.settingsLayout = QHBoxLayout()
        self.settingsLayout.setSpacing(0)
        self.settingsLayout.setObjectName(u"settingsLayout")
        self.settingsLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.settingsView = QListWidget(SettingsDialog)
        QListWidgetItem(self.settingsView)
        self.settingsView.setObjectName(u"settingsView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsView.sizePolicy().hasHeightForWidth())
        self.settingsView.setSizePolicy(sizePolicy)

        self.settingsLayout.addWidget(self.settingsView)

        self.settingsWidget = QStackedWidget(SettingsDialog)
        self.settingsWidget.setObjectName(u"settingsWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.settingsWidget.sizePolicy().hasHeightForWidth())
        self.settingsWidget.setSizePolicy(sizePolicy1)
        self.generalPage = QWidget()
        self.generalPage.setObjectName(u"generalPage")
        sizePolicy1.setHeightForWidth(self.generalPage.sizePolicy().hasHeightForWidth())
        self.generalPage.setSizePolicy(sizePolicy1)
        self.generalScrollArea = QScrollArea(self.generalPage)
        self.generalScrollArea.setObjectName(u"generalScrollArea")
        self.generalScrollArea.setGeometry(QRect(-1, -1, 371, 481))
        self.generalScrollArea.setFrameShape(QFrame.NoFrame)
        self.generalScrollArea.setFrameShadow(QFrame.Plain)
        self.generalScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.generalScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.generalScrollArea.setWidgetResizable(True)
        self.generalScrollAreaContents = QWidget()
        self.generalScrollAreaContents.setObjectName(u"generalScrollAreaContents")
        self.generalScrollAreaContents.setGeometry(QRect(0, 0, 371, 481))
        sizePolicy1.setHeightForWidth(self.generalScrollAreaContents.sizePolicy().hasHeightForWidth())
        self.generalScrollAreaContents.setSizePolicy(sizePolicy1)
        self.verticalLayoutWidget = QWidget(self.generalScrollAreaContents)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 392, 481))
        self.generalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.generalLayout.setObjectName(u"generalLayout")
        self.generalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.generalLayout.setContentsMargins(6, 6, 6, 0)
        self.askOnCloseLayout = QHBoxLayout()
        self.askOnCloseLayout.setObjectName(u"askOnCloseLayout")
        self.askOnCloseLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.askOnCloseLayout.setContentsMargins(6, 6, 6, 6)
        self.askOnCloseLabel = QLabel(self.verticalLayoutWidget)
        self.askOnCloseLabel.setObjectName(u"askOnCloseLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.askOnCloseLabel.sizePolicy().hasHeightForWidth())
        self.askOnCloseLabel.setSizePolicy(sizePolicy2)

        self.askOnCloseLayout.addWidget(self.askOnCloseLabel)

        self.askOnCloseComboBox = QComboBox(self.verticalLayoutWidget)
        self.askOnCloseComboBox.addItem("")
        self.askOnCloseComboBox.addItem("")
        self.askOnCloseComboBox.setObjectName(u"askOnCloseComboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.askOnCloseComboBox.sizePolicy().hasHeightForWidth())
        self.askOnCloseComboBox.setSizePolicy(sizePolicy3)

        self.askOnCloseLayout.addWidget(self.askOnCloseComboBox)

        self.askOnCloseLayout.setStretch(1, 1)

        self.generalLayout.addLayout(self.askOnCloseLayout)

        self.themeLayout = QHBoxLayout()
        self.themeLayout.setObjectName(u"themeLayout")
        self.themeLayout.setContentsMargins(6, 6, 6, 6)
        self.themeLabel = QLabel(self.verticalLayoutWidget)
        self.themeLabel.setObjectName(u"themeLabel")

        self.themeLayout.addWidget(self.themeLabel)

        self.themeComboBox = QComboBox(self.verticalLayoutWidget)
        self.themeComboBox.setObjectName(u"themeComboBox")
        sizePolicy3.setHeightForWidth(self.themeComboBox.sizePolicy().hasHeightForWidth())
        self.themeComboBox.setSizePolicy(sizePolicy3)

        self.themeLayout.addWidget(self.themeComboBox)

        self.themeAddButton = QPushButton(self.verticalLayoutWidget)
        self.themeAddButton.setObjectName(u"themeAddButton")

        self.themeLayout.addWidget(self.themeAddButton)

        self.themeLayout.setStretch(1, 1)

        self.generalLayout.addLayout(self.themeLayout)

        self.fontLayout = QHBoxLayout()
        self.fontLayout.setObjectName(u"fontLayout")
        self.fontLayout.setContentsMargins(6, 6, 6, 6)
        self.fontLabel = QLabel(self.verticalLayoutWidget)
        self.fontLabel.setObjectName(u"fontLabel")

        self.fontLayout.addWidget(self.fontLabel)

        self.fontComboBox = QFontComboBox(self.verticalLayoutWidget)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.fontLayout.addWidget(self.fontComboBox)

        self.fontAddButton = QPushButton(self.verticalLayoutWidget)
        self.fontAddButton.setObjectName(u"fontAddButton")

        self.fontLayout.addWidget(self.fontAddButton)


        self.generalLayout.addLayout(self.fontLayout)

        self.fontSizeLayout = QHBoxLayout()
        self.fontSizeLayout.setObjectName(u"fontSizeLayout")
        self.fontSizeLayout.setContentsMargins(6, 6, 6, 6)
        self.fontSizeLabel = QLabel(self.verticalLayoutWidget)
        self.fontSizeLabel.setObjectName(u"fontSizeLabel")

        self.fontSizeLayout.addWidget(self.fontSizeLabel)

        self.fontSizeSlider = QSlider(self.verticalLayoutWidget)
        self.fontSizeSlider.setObjectName(u"fontSizeSlider")
        self.fontSizeSlider.setOrientation(Qt.Horizontal)

        self.fontSizeLayout.addWidget(self.fontSizeSlider)

        self.fontSizeLayout.setStretch(1, 1)

        self.generalLayout.addLayout(self.fontSizeLayout)

        self.layoutSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.generalLayout.addItem(self.layoutSpacer)

        self.generalScrollArea.setWidget(self.generalScrollAreaContents)
        self.horizontalLayoutWidget = QWidget(self.generalPage)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 480, 371, 39))
        self.profileButtonsLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.profileButtonsLayout.setObjectName(u"profileButtonsLayout")
        self.profileButtonsLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.profileButtonsLayout.setContentsMargins(6, 0, 6, 0)
        self.removeProfileButton = QPushButton(self.horizontalLayoutWidget)
        self.removeProfileButton.setObjectName(u"removeProfileButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.removeProfileButton.sizePolicy().hasHeightForWidth())
        self.removeProfileButton.setSizePolicy(sizePolicy4)

        self.profileButtonsLayout.addWidget(self.removeProfileButton)

        self.addProfileButton = QPushButton(self.horizontalLayoutWidget)
        self.addProfileButton.setObjectName(u"addProfileButton")
        sizePolicy4.setHeightForWidth(self.addProfileButton.sizePolicy().hasHeightForWidth())
        self.addProfileButton.setSizePolicy(sizePolicy4)

        self.profileButtonsLayout.addWidget(self.addProfileButton)

        self.profileButtonsLayout.setStretch(0, 1)
        self.profileButtonsLayout.setStretch(1, 1)
        self.settingsWidget.addWidget(self.generalPage)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.settingsWidget.addWidget(self.page_2)

        self.settingsLayout.addWidget(self.settingsWidget)

        self.settingsLayout.setStretch(1, 1)

        self.mainLayout.addLayout(self.settingsLayout)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.buttonsLayout.setContentsMargins(6, 0, 6, 3)
        self.cancelButton = QPushButton(SettingsDialog)
        self.cancelButton.setObjectName(u"cancelButton")
        sizePolicy3.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy3)

        self.buttonsLayout.addWidget(self.cancelButton)

        self.resetButton = QPushButton(SettingsDialog)
        self.resetButton.setObjectName(u"resetButton")
        sizePolicy3.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy3)

        self.buttonsLayout.addWidget(self.resetButton)

        self.applyButton = QPushButton(SettingsDialog)
        self.applyButton.setObjectName(u"applyButton")
        sizePolicy3.setHeightForWidth(self.applyButton.sizePolicy().hasHeightForWidth())
        self.applyButton.setSizePolicy(sizePolicy3)

        self.buttonsLayout.addWidget(self.applyButton)

        self.profilesComboBox = QComboBox(SettingsDialog)
        self.profilesComboBox.setObjectName(u"profilesComboBox")
        sizePolicy3.setHeightForWidth(self.profilesComboBox.sizePolicy().hasHeightForWidth())
        self.profilesComboBox.setSizePolicy(sizePolicy3)

        self.buttonsLayout.addWidget(self.profilesComboBox)


        self.mainLayout.addLayout(self.buttonsLayout)

        self.mainLayout.setStretch(0, 1)

        self.retranslateUi(SettingsDialog)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Dialog", None))

        __sortingEnabled = self.settingsView.isSortingEnabled()
        self.settingsView.setSortingEnabled(False)
        ___qlistwidgetitem = self.settingsView.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("SettingsDialog", u"General", None));
        self.settingsView.setSortingEnabled(__sortingEnabled)

        self.askOnCloseLabel.setText(QCoreApplication.translate("SettingsDialog", u"Ask on close: ", None))
        self.askOnCloseComboBox.setItemText(0, QCoreApplication.translate("SettingsDialog", u"Yes", None))
        self.askOnCloseComboBox.setItemText(1, QCoreApplication.translate("SettingsDialog", u"No", None))

        self.themeLabel.setText(QCoreApplication.translate("SettingsDialog", u"Theme: ", None))
        self.themeAddButton.setText(QCoreApplication.translate("SettingsDialog", u"Add Theme", None))
        self.fontLabel.setText(QCoreApplication.translate("SettingsDialog", u"Font: ", None))
        self.fontAddButton.setText(QCoreApplication.translate("SettingsDialog", u"Add font", None))
        self.fontSizeLabel.setText(QCoreApplication.translate("SettingsDialog", u"Font size: ", None))
        self.removeProfileButton.setText(QCoreApplication.translate("SettingsDialog", u"Remove", None))
        self.addProfileButton.setText(QCoreApplication.translate("SettingsDialog", u"Add", None))
        self.cancelButton.setText(QCoreApplication.translate("SettingsDialog", u"Cancel", None))
        self.resetButton.setText(QCoreApplication.translate("SettingsDialog", u"Reset", None))
        self.applyButton.setText(QCoreApplication.translate("SettingsDialog", u"Apply", None))
    # retranslateUi

