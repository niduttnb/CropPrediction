# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ls.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from PyQt5 import QtCore, QtWidgets
df = pd.read_excel('results.xlsx', sheetname='Sheet1')

ph = df.columns[0]
rain = df.columns[1]
temp = df.columns[2]
rh = df.columns[3]
area = df.columns[4]
lastcrop = df.columns[5]
net_n = df.columns[6]
net_p = df.columns[7]
net_k = df.columns[8]
cost_n = df.columns[9]
cost_p = df.columns[10]
cost_k = df.columns[11]
yield1 = df.columns[12]
cropname = df.columns[13]
price = df.columns[14]
totalyield = (area*yield1)
profit= (totalyield*price)/100
t = totalyield/1000
#print(cropname)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_Formo(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 200, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 90, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 150, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 400, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 210, 150, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form","Crop Predicted =  "+ cropname, None))
        self.label_2.setText(_translate("Form","yield = "+ str(t)+" ton", None))
        self.label_3.setText(_translate("Form", "Profit = Rs "+str(profit), None))
        self.label_4.setText(_translate("Form", "N:P:K required "+net_n+": "+net_p+": "+net_k+" kg/ha", None))
        self.label_5.setText(_translate("Form", "Field area "+str(area)+" ha", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formo()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

