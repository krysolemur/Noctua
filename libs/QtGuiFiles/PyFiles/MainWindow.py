# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(798, 600)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionRestart = QAction(MainWindow)
        self.actionRestart.setObjectName(u"actionRestart")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.actionSetTarget = QAction(MainWindow)
        self.actionSetTarget.setObjectName(u"actionSetTarget")
        self.actionDownloadSourceCode = QAction(MainWindow)
        self.actionDownloadSourceCode.setObjectName(u"actionDownloadSourceCode")
        self.actionXSS = QAction(MainWindow)
        self.actionXSS.setObjectName(u"actionXSS")
        self.actionSQLInjection2 = QAction(MainWindow)
        self.actionSQLInjection2.setObjectName(u"actionSQLInjection2")
        self.actionPlugins = QAction(MainWindow)
        self.actionPlugins.setObjectName(u"actionPlugins")
        self.actionAdd_2 = QAction(MainWindow)
        self.actionAdd_2.setObjectName(u"actionAdd_2")
        self.actionInstall = QAction(MainWindow)
        self.actionInstall.setObjectName(u"actionInstall")
        self.actionReportBug = QAction(MainWindow)
        self.actionReportBug.setObjectName(u"actionReportBug")
        self.actionIdeas = QAction(MainWindow)
        self.actionIdeas.setObjectName(u"actionIdeas")
        self.actionManageUsers = QAction(MainWindow)
        self.actionManageUsers.setObjectName(u"actionManageUsers")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 801, 581))
        self.toolsLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.toolsLayout.setObjectName(u"toolsLayout")
        self.toolsLayout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 798, 21))
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuTarget = QMenu(self.menubar)
        self.menuTarget.setObjectName(u"menuTarget")
        self.menuAttack = QMenu(self.menubar)
        self.menuAttack.setObjectName(u"menuAttack")
        self.menuInjections = QMenu(self.menuAttack)
        self.menuInjections.setObjectName(u"menuInjections")
        self.menuPlugins = QMenu(self.menubar)
        self.menuPlugins.setObjectName(u"menuPlugins")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuTarget.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuAttack.menuAction())
        self.menubar.addAction(self.menuPlugins.menuAction())
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionSettings)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionAbout)
        self.menuWindow.addAction(self.actionDocumentation)
        self.menuWindow.addAction(self.actionHelp)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionReportBug)
        self.menuWindow.addAction(self.actionIdeas)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionRestart)
        self.menuWindow.addAction(self.actionQuit)
        self.menuTarget.addAction(self.actionSetTarget)
        self.menuTarget.addAction(self.actionDownloadSourceCode)
        self.menuAttack.addAction(self.menuInjections.menuAction())
        self.menuAttack.addAction(self.actionXSS)
        self.menuInjections.addAction(self.actionSQLInjection2)
        self.menuPlugins.addAction(self.actionAdd_2)
        self.menuPlugins.addAction(self.actionInstall)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionRestart.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionSetTarget.setText(QCoreApplication.translate("MainWindow", u"Set target", None))
        self.actionDownloadSourceCode.setText(QCoreApplication.translate("MainWindow", u"Download source code", None))
        self.actionXSS.setText(QCoreApplication.translate("MainWindow", u"XSS", None))
        self.actionSQLInjection2.setText(QCoreApplication.translate("MainWindow", u"SQL Injection", None))
        self.actionPlugins.setText(QCoreApplication.translate("MainWindow", u"Plugins", None))
        self.actionAdd_2.setText(QCoreApplication.translate("MainWindow", u"Manage", None))
        self.actionInstall.setText(QCoreApplication.translate("MainWindow", u"Install", None))
        self.actionReportBug.setText(QCoreApplication.translate("MainWindow", u"Report bug", None))
        self.actionIdeas.setText(QCoreApplication.translate("MainWindow", u"Ideas", None))
        self.actionManageUsers.setText(QCoreApplication.translate("MainWindow", u"Manage users", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuTarget.setTitle(QCoreApplication.translate("MainWindow", u"Target", None))
        self.menuAttack.setTitle(QCoreApplication.translate("MainWindow", u"Attack", None))
        self.menuInjections.setTitle(QCoreApplication.translate("MainWindow", u"Injections", None))
        self.menuPlugins.setTitle(QCoreApplication.translate("MainWindow", u"Plugins", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

