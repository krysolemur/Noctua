# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SourcePage.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QButtonGroup, QComboBox,
    QHBoxLayout, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_sourcePage(object):
    def setupUi(self, sourcePage):
        if not sourcePage.objectName():
            sourcePage.setObjectName(u"sourcePage")
        sourcePage.resize(978, 793)
        self.mainLayout = QVBoxLayout(sourcePage)
        self.mainLayout.setSpacing(3)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(3, 3, 3, 3)
        self.sourceCodeScrollArea = QScrollArea(sourcePage)
        self.sourceCodeScrollArea.setObjectName(u"sourceCodeScrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceCodeScrollArea.sizePolicy().hasHeightForWidth())
        self.sourceCodeScrollArea.setSizePolicy(sizePolicy)
        self.sourceCodeScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sourceCodeScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.sourceCodeScrollArea.setWidgetResizable(True)
        self.sourceCodeScrollArea.setAlignment(Qt.AlignCenter)
        self.sourceCodeScrollContent = QWidget()
        self.sourceCodeScrollContent.setObjectName(u"sourceCodeScrollContent")
        self.sourceCodeScrollContent.setGeometry(QRect(0, 0, 970, 785))
        self.sourceCodeScrollLayout = QVBoxLayout(self.sourceCodeScrollContent)
        self.sourceCodeScrollLayout.setObjectName(u"sourceCodeScrollLayout")
        self.sourceCodeScrollLayout.setContentsMargins(0, 0, 0, 0)
        self.exampleTextLayout = QVBoxLayout()
        self.exampleTextLayout.setObjectName(u"exampleTextLayout")
        self.exampleTextLayout.setContentsMargins(-1, 0, -1, 6)
        self.exampleTextEdit = QTextEdit(self.sourceCodeScrollContent)
        self.exampleTextEdit.setObjectName(u"exampleTextEdit")
        self.exampleTextEdit.setReadOnly(True)

        self.exampleTextLayout.addWidget(self.exampleTextEdit)

        self.markingLayout = QHBoxLayout()
        self.markingLayout.setObjectName(u"markingLayout")
        self.elementsButton = QPushButton(self.sourceCodeScrollContent)
        self.stylingButtonGroup = QButtonGroup(sourcePage)
        self.stylingButtonGroup.setObjectName(u"stylingButtonGroup")
        self.stylingButtonGroup.addButton(self.elementsButton)
        self.elementsButton.setObjectName(u"elementsButton")
        self.elementsButton.setCheckable(True)
        self.elementsButton.setChecked(True)
        self.elementsButton.setAutoDefault(False)

        self.markingLayout.addWidget(self.elementsButton)

        self.atributsButton = QPushButton(self.sourceCodeScrollContent)
        self.stylingButtonGroup.addButton(self.atributsButton)
        self.atributsButton.setObjectName(u"atributsButton")
        self.atributsButton.setCheckable(True)

        self.markingLayout.addWidget(self.atributsButton)

        self.stringButton = QPushButton(self.sourceCodeScrollContent)
        self.stylingButtonGroup.addButton(self.stringButton)
        self.stringButton.setObjectName(u"stringButton")
        self.stringButton.setCheckable(True)

        self.markingLayout.addWidget(self.stringButton)

        self.attrValuesButton = QPushButton(self.sourceCodeScrollContent)
        self.stylingButtonGroup.addButton(self.attrValuesButton)
        self.attrValuesButton.setObjectName(u"attrValuesButton")
        self.attrValuesButton.setCheckable(True)

        self.markingLayout.addWidget(self.attrValuesButton)

        self.commentsButton = QPushButton(self.sourceCodeScrollContent)
        self.stylingButtonGroup.addButton(self.commentsButton)
        self.commentsButton.setObjectName(u"commentsButton")
        self.commentsButton.setCheckable(True)

        self.markingLayout.addWidget(self.commentsButton)


        self.exampleTextLayout.addLayout(self.markingLayout)

        self.stylingLayout = QHBoxLayout()
        self.stylingLayout.setObjectName(u"stylingLayout")
        self.foregroundStyle = QPushButton(self.sourceCodeScrollContent)
        self.foregroundStyle.setObjectName(u"foregroundStyle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.foregroundStyle.sizePolicy().hasHeightForWidth())
        self.foregroundStyle.setSizePolicy(sizePolicy1)

        self.stylingLayout.addWidget(self.foregroundStyle)

        self.backgroundStyle = QPushButton(self.sourceCodeScrollContent)
        self.backgroundStyle.setObjectName(u"backgroundStyle")
        sizePolicy1.setHeightForWidth(self.backgroundStyle.sizePolicy().hasHeightForWidth())
        self.backgroundStyle.setSizePolicy(sizePolicy1)

        self.stylingLayout.addWidget(self.backgroundStyle)

        self.boldStyle = QPushButton(self.sourceCodeScrollContent)
        self.boldStyle.setObjectName(u"boldStyle")
        sizePolicy1.setHeightForWidth(self.boldStyle.sizePolicy().hasHeightForWidth())
        self.boldStyle.setSizePolicy(sizePolicy1)
        self.boldStyle.setCheckable(True)

        self.stylingLayout.addWidget(self.boldStyle)

        self.italicStyle = QPushButton(self.sourceCodeScrollContent)
        self.italicStyle.setObjectName(u"italicStyle")
        sizePolicy1.setHeightForWidth(self.italicStyle.sizePolicy().hasHeightForWidth())
        self.italicStyle.setSizePolicy(sizePolicy1)
        self.italicStyle.setCheckable(True)

        self.stylingLayout.addWidget(self.italicStyle)

        self.underlineStyle = QPushButton(self.sourceCodeScrollContent)
        self.underlineStyle.setObjectName(u"underlineStyle")
        sizePolicy1.setHeightForWidth(self.underlineStyle.sizePolicy().hasHeightForWidth())
        self.underlineStyle.setSizePolicy(sizePolicy1)
        self.underlineStyle.setCheckable(True)

        self.stylingLayout.addWidget(self.underlineStyle)

        self.transformStyle = QComboBox(self.sourceCodeScrollContent)
        self.transformStyle.addItem("")
        self.transformStyle.addItem("")
        self.transformStyle.setObjectName(u"transformStyle")
        sizePolicy1.setHeightForWidth(self.transformStyle.sizePolicy().hasHeightForWidth())
        self.transformStyle.setSizePolicy(sizePolicy1)

        self.stylingLayout.addWidget(self.transformStyle)

        self.resetButton = QPushButton(self.sourceCodeScrollContent)
        self.resetButton.setObjectName(u"resetButton")
        sizePolicy1.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy1)

        self.stylingLayout.addWidget(self.resetButton)


        self.exampleTextLayout.addLayout(self.stylingLayout)


        self.sourceCodeScrollLayout.addLayout(self.exampleTextLayout)

        self.sourceCodeLayoutSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sourceCodeScrollLayout.addItem(self.sourceCodeLayoutSpacer)

        self.sourceCodeScrollArea.setWidget(self.sourceCodeScrollContent)

        self.mainLayout.addWidget(self.sourceCodeScrollArea)


        self.retranslateUi(sourcePage)

        QMetaObject.connectSlotsByName(sourcePage)
    # setupUi

    def retranslateUi(self, sourcePage):
        sourcePage.setWindowTitle(QCoreApplication.translate("sourcePage", u"Form", None))
        self.exampleTextEdit.setDocumentTitle(QCoreApplication.translate("sourcePage", u"Preview", None))
        self.exampleTextEdit.setHtml(QCoreApplication.translate("sourcePage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><title>Preview</title><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;html&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  &lt;body style=&quot;font-family: 'Arial', sans-serif; font-size: 10pt; color: #222;&quot;&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;h2 styl"
                        "e=&quot;color: #004a99;&quot;&gt;System Manifest&lt;/h2&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;blockquote style=&quot;background: #f4f4f4; border-left: 4px solid #004a99; padding: 8px;&quot;&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      &quot;Core modules initialized. All systems nominal.&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;/blockquote&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;p&gt;Network Status: &lt;span style=&quot;color: #28a745; font-weight: bold;&quot;&gt;CONNECTED&lt;/span&gt;&lt;/p&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px"
                        ";\">    &lt;hr /&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;p&gt;Configuration Script:&lt;/p&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;pre style=&quot;background: #1e1e1e; color: #d4d4d4; padding: 12px; border-radius: 4px;&quot;&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">def sync_data():</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    # Syncing local database with remote</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    target = &quot;https://api.internal/v1&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\">    return True</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;/pre&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;table border=&quot;1&quot; width=&quot;100%&quot; cellpadding=&quot;6&quot; style=&quot;border-collapse: collapse; border: 1px solid #ddd;&quot;&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      &lt;tr bgcolor=&quot;#f2f2f2&quot;&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &lt;th&gt;Component&lt;/th&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &lt;th&gt;ID&lt;/th&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bot"
                        "tom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &lt;th&gt;Health&lt;/th&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      &lt;/tr&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      &lt;tr&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &lt;td&gt;&lt;b&gt;CPU Cluster&lt;/b&gt;&lt;/td&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &lt;td&gt;&lt;code&gt;NODE_01&lt;/code&gt;&lt;/td&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &lt;td&gt;&lt;i style=&quot;color: green;&quot;&gt;98%&lt;/i&gt;&lt;/td&gt;</p>\n"
"<p style=\" "
                        "margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      &lt;/tr&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      &lt;tr&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &lt;td colspan=&quot;2&quot;&gt;Backup Power Supply&lt;/td&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">        &lt;td align=&quot;right&quot;&gt;Standby&lt;/td&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      &lt;/tr&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;/table&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:"
                        "0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;p&gt;User Actions:&lt;/p&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;ul&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      &lt;li&gt;&lt;a href=&quot;cmd://reboot&quot; style=&quot;color: #d9534f; font-weight: bold;&quot;&gt;System Reboot&lt;/a&gt;&lt;/li&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      &lt;li&gt;&lt;a href=&quot;https://wiki.local&quot; style=&quot;color: #0275d8;&quot;&gt;Access Manual&lt;/a&gt;&lt;/li&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;/ul&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent"
                        ":0; text-indent:0px;\">    &lt;div style=&quot;background: #fff3cd; padding: 10px; border: 1px solid #ffeeba;&quot;&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      &lt;strong&gt;Debug Info (Non-functional in Qt):&lt;/strong&gt;&lt;br&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      &lt;code&gt;&amp;lt;script&amp;gt;alert('No JS support');&amp;lt;/script&amp;gt;&lt;/code&gt;&lt;br&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">      &lt;code&gt;&amp;lt;input type=&quot;text&quot; placeholder=&quot;No inputs&quot;&amp;gt;&lt;/code&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;/div&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; m"
                        "argin-right:0px; -qt-block-indent:0; text-indent:0px;\">  &lt;/body&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;/html&gt;</p></body></html>", None))
        self.exampleTextEdit.setPlaceholderText("")
        self.elementsButton.setText(QCoreApplication.translate("sourcePage", u"Elements", None))
        self.atributsButton.setText(QCoreApplication.translate("sourcePage", u"Atributs", None))
        self.stringButton.setText(QCoreApplication.translate("sourcePage", u"Strings", None))
        self.attrValuesButton.setText(QCoreApplication.translate("sourcePage", u"Atribut values", None))
        self.commentsButton.setText(QCoreApplication.translate("sourcePage", u"Comments", None))
        self.foregroundStyle.setText(QCoreApplication.translate("sourcePage", u"Foreground", None))
        self.backgroundStyle.setText(QCoreApplication.translate("sourcePage", u"Background", None))
        self.boldStyle.setText(QCoreApplication.translate("sourcePage", u"B", None))
        self.italicStyle.setText(QCoreApplication.translate("sourcePage", u"I", None))
        self.underlineStyle.setText(QCoreApplication.translate("sourcePage", u"U", None))
        self.transformStyle.setItemText(0, QCoreApplication.translate("sourcePage", u"Lowercase", None))
        self.transformStyle.setItemText(1, QCoreApplication.translate("sourcePage", u"Uppercase", None))

        self.resetButton.setText(QCoreApplication.translate("sourcePage", u"Reset", None))
    # retranslateUi

