# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic_v1.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(430, 600))
        MainWindow.setMaximumSize(QtCore.QSize(430, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 411, 531))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pte_idlist = QtWidgets.QPlainTextEdit(self.groupBox)
        self.pte_idlist.setReadOnly(True)
        self.pte_idlist.setObjectName("pte_idlist")
        self.verticalLayout.addWidget(self.pte_idlist)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 411, 36))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.le_blogurl = QtWidgets.QLineEdit(self.widget)
        self.le_blogurl.setText("")
        self.le_blogurl.setObjectName("le_blogurl")
        self.horizontalLayout.addWidget(self.le_blogurl)
        self.pb_sel = QtWidgets.QPushButton(self.widget)
        self.pb_sel.setObjectName("pb_sel")
        self.horizontalLayout.addWidget(self.pb_sel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Naver Blog 공감한 ID"))
        self.groupBox.setTitle(_translate("MainWindow", "공감 ID"))
        self.le_blogurl.setPlaceholderText(_translate("MainWindow", "네이버 블로그 포스팅 URL을 입력해 주세요"))
        self.pb_sel.setText(_translate("MainWindow", "조회"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
