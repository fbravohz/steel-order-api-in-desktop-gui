# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
        MainWindow.resize(1450, 1000)
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
        self.gridLayout = QGridLayout(self.tab_warehouses)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.label_destiny = QLabel(self.tab_warehouses)
        self.label_destiny.setObjectName(u"label_destiny")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_destiny.sizePolicy().hasHeightForWidth())
        self.label_destiny.setSizePolicy(sizePolicy1)
        self.label_destiny.setMinimumSize(QSize(60, 0))
        self.label_destiny.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_destiny, 3, 0, 1, 1)

        self.pushButton_pull = QPushButton(self.tab_warehouses)
        self.pushButton_pull.setObjectName(u"pushButton_pull")

        self.gridLayout.addWidget(self.pushButton_pull, 2, 3, 1, 1)

        self.label_origin = QLabel(self.tab_warehouses)
        self.label_origin.setObjectName(u"label_origin")
        sizePolicy1.setHeightForWidth(self.label_origin.sizePolicy().hasHeightForWidth())
        self.label_origin.setSizePolicy(sizePolicy1)
        self.label_origin.setMinimumSize(QSize(60, 0))
        self.label_origin.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_origin, 0, 0, 1, 1)

        self.pushButton_save = QPushButton(self.tab_warehouses)
        self.pushButton_save.setObjectName(u"pushButton_save")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_save.sizePolicy().hasHeightForWidth())
        self.pushButton_save.setSizePolicy(sizePolicy2)
        self.pushButton_save.setMaximumSize(QSize(200, 16777215))
        self.pushButton_save.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_save, 4, 3, 1, 1)

        self.comboBox_origin = QComboBox(self.tab_warehouses)
        self.comboBox_origin.setObjectName(u"comboBox_origin")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_origin.sizePolicy().hasHeightForWidth())
        self.comboBox_origin.setSizePolicy(sizePolicy3)
        self.comboBox_origin.setMinimumSize(QSize(150, 0))
        self.comboBox_origin.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.comboBox_origin, 2, 0, 1, 1)

        self.comboBox_destiny = QComboBox(self.tab_warehouses)
        self.comboBox_destiny.setObjectName(u"comboBox_destiny")
        sizePolicy3.setHeightForWidth(self.comboBox_destiny.sizePolicy().hasHeightForWidth())
        self.comboBox_destiny.setSizePolicy(sizePolicy3)
        self.comboBox_destiny.setMinimumSize(QSize(150, 0))
        self.comboBox_destiny.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.comboBox_destiny, 4, 0, 1, 1)

        self.tableWidget = QTableWidget(self.tab_warehouses)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(9)
        self.tableWidget.setFont(font)
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)

        self.gridLayout.addWidget(self.tableWidget, 6, 0, 1, 4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_loading = QLabel(self.tab_warehouses)
        self.label_loading.setObjectName(u"label_loading")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_loading.sizePolicy().hasHeightForWidth())
        self.label_loading.setSizePolicy(sizePolicy5)
        self.label_loading.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.label_loading)

        self.progressBar = QProgressBar(self.tab_warehouses)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy3.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy3)
        self.progressBar.setMaximumSize(QSize(16777215, 10))
        self.progressBar.setValue(100)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.progressBar)


        self.gridLayout.addLayout(self.verticalLayout, 7, 3, 1, 1)

        self.tabWidget_warehouses.addTab(self.tab_warehouses, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_warehouses.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget_warehouses)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget_warehouses.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Baymed API", None))
        self.label_destiny.setText(QCoreApplication.translate("MainWindow", u"Destino:", None))
        self.pushButton_pull.setText(QCoreApplication.translate("MainWindow", u"Traer", None))
        self.label_origin.setText(QCoreApplication.translate("MainWindow", u"Origen:", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_loading.setText("")
        self.tabWidget_warehouses.setTabText(self.tabWidget_warehouses.indexOf(self.tab_warehouses), QCoreApplication.translate("MainWindow", u"Almacenes", None))
        self.tabWidget_warehouses.setTabText(self.tabWidget_warehouses.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

