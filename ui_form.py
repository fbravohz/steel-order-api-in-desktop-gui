# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 1000)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, 30, 30, 30)
        self.tabWidget_warehouses = QTabWidget(self.centralwidget)
        self.tabWidget_warehouses.setObjectName(u"tabWidget_warehouses")
        self.tab_warehouses = QWidget()
        self.tab_warehouses.setObjectName(u"tab_warehouses")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_warehouses)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_origin = QHBoxLayout()
        self.horizontalLayout_origin.setObjectName(u"horizontalLayout_origin")
        self.label_origin = QLabel(self.tab_warehouses)
        self.label_origin.setObjectName(u"label_origin")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_origin.sizePolicy().hasHeightForWidth())
        self.label_origin.setSizePolicy(sizePolicy1)
        self.label_origin.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_origin.addWidget(self.label_origin)

        self.comboBox_origin = QComboBox(self.tab_warehouses)
        self.comboBox_origin.setObjectName(u"comboBox_origin")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_origin.sizePolicy().hasHeightForWidth())
        self.comboBox_origin.setSizePolicy(sizePolicy2)
        self.comboBox_origin.setMinimumSize(QSize(150, 0))
        self.comboBox_origin.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_origin.addWidget(self.comboBox_origin)


        self.verticalLayout_2.addLayout(self.horizontalLayout_origin)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalLayout_destiny = QHBoxLayout()
        self.horizontalLayout_destiny.setObjectName(u"horizontalLayout_destiny")
        self.horizontalLayout_destiny.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_destiny = QLabel(self.tab_warehouses)
        self.label_destiny.setObjectName(u"label_destiny")
        sizePolicy1.setHeightForWidth(self.label_destiny.sizePolicy().hasHeightForWidth())
        self.label_destiny.setSizePolicy(sizePolicy1)
        self.label_destiny.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_destiny.addWidget(self.label_destiny)

        self.comboBox_destiny = QComboBox(self.tab_warehouses)
        self.comboBox_destiny.setObjectName(u"comboBox_destiny")
        sizePolicy2.setHeightForWidth(self.comboBox_destiny.sizePolicy().hasHeightForWidth())
        self.comboBox_destiny.setSizePolicy(sizePolicy2)
        self.comboBox_destiny.setMinimumSize(QSize(150, 0))
        self.comboBox_destiny.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_destiny.addWidget(self.comboBox_destiny)


        self.verticalLayout_2.addLayout(self.horizontalLayout_destiny)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.pushButton_pull = QPushButton(self.tab_warehouses)
        self.pushButton_pull.setObjectName(u"pushButton_pull")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_pull.sizePolicy().hasHeightForWidth())
        self.pushButton_pull.setSizePolicy(sizePolicy3)
        self.pushButton_pull.setMaximumSize(QSize(200, 16777215))
        self.pushButton_pull.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.pushButton_pull)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.pushButton_clear = QPushButton(self.tab_warehouses)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        sizePolicy3.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy3)
        self.pushButton_clear.setMaximumSize(QSize(200, 16777215))
        self.pushButton_clear.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.pushButton_clear)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.pushButton_save = QPushButton(self.tab_warehouses)
        self.pushButton_save.setObjectName(u"pushButton_save")
        sizePolicy3.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy3)
        self.pushButton_save.setMaximumSize(QSize(200, 16777215))
        self.pushButton_save.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.pushButton_save)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.tableWidget = QTableWidget(self.tab_warehouses)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_4.addWidget(self.tableWidget)

        self.tabWidget_warehouses.addTab(self.tab_warehouses, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_warehouses.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget_warehouses)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tableWidget.cellChanged.connect(self.pushButton_pull.animateClick)

        self.tabWidget_warehouses.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_origin.setText(QCoreApplication.translate("MainWindow", u"Origen:", None))
        self.label_destiny.setText(QCoreApplication.translate("MainWindow", u"Destino:", None))
        self.pushButton_pull.setText(QCoreApplication.translate("MainWindow", u"Traer", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.tabWidget_warehouses.setTabText(self.tabWidget_warehouses.indexOf(self.tab_warehouses), QCoreApplication.translate("MainWindow", u"Almacenes", None))
        self.tabWidget_warehouses.setTabText(self.tabWidget_warehouses.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

