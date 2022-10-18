# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'no_stock.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogNoStock(object):
    def setupUi(self, DialogNoStock):
        if not DialogNoStock.objectName():
            DialogNoStock.setObjectName(u"DialogNoStock")
        DialogNoStock.resize(350, 150)
        DialogNoStock.setSizeGripEnabled(False)
        DialogNoStock.setModal(False)
        self.verticalLayout = QVBoxLayout(DialogNoStock)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DialogNoStock)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(350, 16777215))
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(DialogNoStock)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(DialogNoStock)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DialogNoStock)

        QMetaObject.connectSlotsByName(DialogNoStock)
    # setupUi

    def retranslateUi(self, DialogNoStock):
        DialogNoStock.setWindowTitle(QCoreApplication.translate("DialogNoStock", u"Stock insuficiente", None))
        self.label.setText("")
        self.pushButton.setText(QCoreApplication.translate("DialogNoStock", u"Continuar", None))
        self.pushButton_2.setText(QCoreApplication.translate("DialogNoStock", u"Cancelar", None))
    # retranslateUi

