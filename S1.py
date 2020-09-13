# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'S1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import xlsxwriter
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset
workbook = xlsxwriter.Workbook('results.xlsx')
worksheet = workbook.add_worksheet()
row =0
col =0

dataset = pd.read_csv('crop_final.csv')
X = dataset.iloc[:, [1,2,3,4]].values
y = dataset.iloc[:, 5].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0, random_state = 0)

# Fitting Logistic Regression to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
classifier.fit(X_train,y_train) 
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

class Ui_Form1(QtWidgets.QWidget):

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(634, 569)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 440, 101, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(440, 140, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 240, 113, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 50, 111, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(330, 150, 91, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 250, 68, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 140, 113, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(440, 240, 113, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, 150, 68, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(297, 250, 131, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 340, 101, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 340, 113, 27))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(350, 350, 68, 17))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(450, 340, 101, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(340, 350, 68, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        temp=self.lineEdit
        rain=self.lineEdit_2
        ph=self.lineEdit_3
        rh=self.lineEdit_4
        ah=self.lineEdit_5
        crop=self.comboBox
        self.retranslateUi(Form)
        def greport(self):
            row = 0
            col = 0
            '''self.window=QtWidgets.QWidget()
            self.ui=Ui.Form3()
            self.ui.setupUi(self.window)
            self.window.show()'''
            print ("pH = "+str(ph.text()))
            print ("Rainfall = "+str(rain.text()))
            print ("Tempertaure = "+str(temp.text()))
            print ("Relative Humidity = "+str(rh.text()))
            print ("Area of land in hectres = "+str(ah.text()))
            print ("Last Crop = "+str(crop.currentText()))
            worksheet.write(row,col,float(str(ph.text())))
            worksheet.write(row,col+1,int(str(rain.text())))
            worksheet.write(row,col+2,int(str(temp.text())))
            worksheet.write(row,col+3,int(str(rh.text())))
            worksheet.write(row,col+4,float(str(ah.text())))
            worksheet.write(row,col+5,str(crop.currentText()))
            
            
            
            
            p=ph.text()
            t=temp.text()
            r=rain.text()
            rel=rh.text()
            size=str(ah.text())
            size1 = int(size)
            #print(type(size1))
            #print(type(size1)
            previous_crop = crop.currentIndex()
            n_cost_kg=119
            p_cost_kg=69
            k_cost_kg=169
           
            print(previous_crop)
            if previous_crop== 0:
                val=0
                n_lost=63 
                p_lost=28.5
                k_lost=16.5
                n_required=120
                p_required=60
                k_required=40
                yield1=3000
                net_n=size1*n_required-size1*n_lost
                net_p=size1*p_required-size1*p_lost
                net_k=size1*k_required-size1*k_lost
                
                
                
                print("Dear farmers, The amount of N to be added is " + str(round(net_n,2)) + " and its cost is " + str(round(net_n*n_cost_kg ,2)))
                print("Dear farmers, The amount of p to be added is " + str(round(net_p,2)) + " and its cost is " + str(round(net_p * p_cost_kg,2)))
                print("Dear farmers, The amount of k to be added is " + str(round(net_k,2)) + " and its cost is " + str(round(net_k *k_cost_kg,2)))
                worksheet.write(row,col+6,str(net_n))
                worksheet.write(row,col+7,str(net_p))
                worksheet.write(row,col+8,str(net_k))
                worksheet.write(row,col+9,str(round(net_n*n_cost_kg ,2)))
                worksheet.write(row,col+10,str(round(net_p*n_cost_kg ,2)))
                worksheet.write(row,col+11,str(round(net_k*n_cost_kg ,2)))
                worksheet.write(row,col+12,yield1)
            elif previous_crop== 1:
                val=1
                n_lost=39
                p_lost=20
                k_lost=10.8
                n_required=120
                p_required=60
                k_required=40
                yield1=3000
                net_n=size1*n_required-size1*n_lost
                net_p=size1*p_required-size1*p_lost
                net_k=size1*k_required-size1*k_lost
                
                
                
                print("Dear farmers, The amount of N to be added is " + str(round(net_n,2)) + " and its cost is " + str(round(net_n*n_cost_kg ,2)))
                print("Dear farmers, The amount of p to be added is " + str(round(net_p,2)) + " and its cost is " + str(round(net_p * p_cost_kg,2)))
                print("Dear farmers, The amount of k to be added is " + str(round(net_k,2)) + " and its cost is " + str(round(net_k *k_cost_kg,2)))    
                worksheet.write(row,col+6,str(net_n))
                worksheet.write(row,col+7,str(net_p))
                worksheet.write(row,col+8,str(net_k))
                worksheet.write(row,col+9,str(round(net_n*n_cost_kg ,2)))
                worksheet.write(row,col+10,str(round(net_p*n_cost_kg ,2)))
                worksheet.write(row,col+11,str(round(net_k*n_cost_kg ,2)))
                worksheet.write(row,col+12,yield1)
            elif previous_crop== 2:
                val=2
                n_lost=30   
                p_lost=15.8
                k_lost=11.3
                n_required=80
                p_required=40
                k_required=20
                yield1=2500
                net_n=size1*n_required-size1*n_lost
                net_p=size1*p_required-size1*p_lost
                net_k=size1*k_required-size1*k_lost
                print("Dear farmers, The amount of N to be added is " + str(round(net_n,2)) + " and its cost is " + str(round(net_n*n_cost_kg ,2)))
                print("Dear farmers, The amount of p to be added is " + str(round(net_p,2)) + " and its cost is " + str(round(net_p * p_cost_kg,2)))
                print("Dear farmers, The amount of k to be added is " + str(round(net_k,2)) + " and its cost is " + str(round(net_k *k_cost_kg,2)))   
                
                worksheet.write(row,col+6,str(net_n))
                worksheet.write(row,col+7,str(net_p))
                worksheet.write(row,col+8,str(net_k))
                worksheet.write(row,col+9,str(round(net_n*n_cost_kg ,2)))
                worksheet.write(row,col+10,str(round(net_p*n_cost_kg ,2)))
                worksheet.write(row,col+11,str(round(net_k*n_cost_kg ,2)))
                worksheet.write(row,col+12,yield1)
            elif previous_crop== 3:
                val=3
                n_lost=63
                p_lost=28.5
                k_lost=16.5
                n_required=120
                p_required=60
                k_required=40
                yield1=1200
                net_n=size1*n_required-size1*n_lost
                net_p=size1*p_required-size1*p_lost
                net_k=size1*k_required-size1*k_lost
                print("Dear farmers, The amount of N to be added is " + str(round(net_n,2)) + " and its cost is " + str(round(net_n*n_cost_kg ,2)))
                print("Dear farmers, The amount of p to be added is " + str(round(net_p,2)) + " and its cost is " + str(round(net_p * p_cost_kg,2)))
                print("Dear farmers, The amount of k to be added is " + str(round(net_k,2)) + " and its cost is " + str(round(net_k *k_cost_kg,2)))
                
                worksheet.write(row,col+6,str(net_n))
                worksheet.write(row,col+7,str(net_p))
                worksheet.write(row,col+8,str(net_k))
                worksheet.write(row,col+9,str(round(net_n*n_cost_kg ,2)))
                worksheet.write(row,col+10,str(round(net_p*n_cost_kg ,2)))
                worksheet.write(row,col+11,str(round(net_k*n_cost_kg ,2)))
                worksheet.write(row,col+12,yield1)
            elif previous_crop== 4:
                val=4
                n_lost=140
                p_lost=70
                k_lost=41.1
                n_required=220
                p_required=130
                k_required=69
                yield1=3500
                net_n=size1*n_required-size1*n_lost
                net_p=size1*p_required-size1*p_lost
                net_k=size1*k_required-size1*k_lost
                print("Dear farmers, The amount of N to be added is " + str(round(net_n,2)) + " and its cost is " + str(round(net_n*n_cost_kg ,2)))
                print("Dear farmers, The amount of p to be added is " + str(round(net_p,2)) + " and its cost is " + str(round(net_p * p_cost_kg,2)))
                print("Dear farmers, The amount of k to be added is " + str(round(net_k,2)) + " and its cost is " + str(round(net_k *k_cost_kg,2)))
                worksheet.write(row,col+6,str(net_n))
                worksheet.write(row,col+7,str(net_p))
                worksheet.write(row,col+8,str(net_k))
                worksheet.write(row,col+9,str(round(net_n*n_cost_kg ,2)))
                worksheet.write(row,col+10,str(round(net_p*n_cost_kg ,2)))
                worksheet.write(row,col+11,str(round(net_k*n_cost_kg ,2)))
                worksheet.write(row,col+12,yield1)
            elif previous_crop== 5:
                val=5
                n_lost=63
                p_lost=28.5
                k_lost=16.5
                n_required=135
                p_required=69
                k_required=58
                yield1=3100
                net_n=size1*n_required-size1*n_lost
                net_p=size1*p_required-size1*p_lost
                net_k=size1*k_required-size1*k_lost
                print("Dear farmers, The amount of N to be added is " + str(round(net_n,2)) + " and its cost is " + str(round(net_n*n_cost_kg ,2)))
                print("Dear farmers, The amount of p to be added is " + str(round(net_p,2)) + " and its cost is " + str(round(net_p * p_cost_kg,2)))
                print("Dear farmers, The amount of k to be added is " + str(round(net_k,2)) + " and its cost is " + str(round(net_k *k_cost_kg,2)))
                worksheet.write(row,col+6,str(net_n))
                worksheet.write(row,col+7,str(net_p))
                worksheet.write(row,col+8,str(net_k))
                worksheet.write(row,col+9,str(round(net_n*n_cost_kg ,2)))
                worksheet.write(row,col+10,str(round(net_p*n_cost_kg ,2)))
                worksheet.write(row,col+11,str(round(net_k*n_cost_kg ,2)))
                worksheet.write(row,col+12,yield1)
            elif previous_crop== 6:
                val=6
                n_lost=24
                p_lost=8.7
                k_lost=8.1
                n_required=35
                p_required=50
                k_required=35
                yield1=900
                net_n=size1*n_required-size1*n_lost
                net_p=size1*p_required-size1*p_lost
                net_k=size1*k_required-size1*k_lost
                print("Dear farmers, The amount of N to be added is " + str(round(net_n,2)) + " and its cost is " + str(round(net_n*n_cost_kg ,2)))
                print("Dear farmers, The amount of p to be added is " + str(round(net_p,2)) + " and its cost is " + str(round(net_p * p_cost_kg,2)))
                print("Dear farmers, The amount of k to be added is " + str(round(net_k,2)) + " and its cost is " + str(round(net_k *k_cost_kg,2)))
                worksheet.write(row,col+6,str(net_n))
                worksheet.write(row,col+7,str(net_p))
                worksheet.write(row,col+8,str(net_k))
                worksheet.write(row,col+9,str(round(net_n*n_cost_kg ,2)))
                worksheet.write(row,col+10,str(round(net_p*n_cost_kg ,2)))
                worksheet.write(row,col+11,str(round(net_k*n_cost_kg ,2)))
                worksheet.write(row,col+12,yield1)
            elif previous_crop == 7:
                val=7
                n_lost=42
                p_lost=28.5
                k_lost=21
                n_required=81
                p_required=64
                k_required=42
                yield1=3900
                net_n=size1*n_required-size1*n_lost
                net_p=size1*p_required-size1*p_lost
                net_k=size1*k_required-size1*k_lost
                print("Dear farmers, The amount of N to be added is " + str(round(net_n,2)) + " and its cost is " + str(round(net_n*n_cost_kg ,2)))
                print("Dear farmers, The amount of p to be added is " + str(round(net_p,2)) + " and its cost is " + str(round(net_p * p_cost_kg,2)))
                print("Dear farmers, The amount of k to be added is " + str(round(net_k,2)) + " and its cost is " + str(round(net_k *k_cost_kg,2)))
                worksheet.write(row,col+6,str(net_n))
                worksheet.write(row,col+7,str(net_p))
                worksheet.write(row,col+8,str(net_k))
                worksheet.write(row,col+9,str(round(net_n*n_cost_kg ,2)))
                worksheet.write(row,col+10,str(round(net_p*n_cost_kg ,2)))
                worksheet.write(row,col+11,str(round(net_k*n_cost_kg ,2)))
                worksheet.write(row,col+12,yield1)
            elif previous_crop== 8:
                val=8
                n_lost=41
                p_lost=12
                k_lost=12
                n_required=120
                p_required=60
                k_required=60
                yield1=1500
                net_n=size1*n_required-size1*n_lost
                net_p=size1*p_required-size1*p_lost
                net_k=size1*k_required-size1*k_lost
                print("Dear farmers, The amount of N to be added is " + str(round(net_n,2)) + " and its cost is " + str(round(net_n*n_cost_kg ,2)))
                print("Dear farmers, The amount of p to be added is " + str(round(net_p,2)) + " and its cost is " + str(round(net_p * p_cost_kg,2)))
                print("Dear farmers, The amount of k to be added is " + str(round(net_k,2)) + " and its cost is " + str(round(net_k *k_cost_kg,2)))
                worksheet.write(row,col+6,str(net_n))
                worksheet.write(row,col+7,str(net_p))
                worksheet.write(row,col+8,str(net_k))
                worksheet.write(row,col+9,str(round(net_n*n_cost_kg ,2)))
                worksheet.write(row,col+10,str(round(net_p*n_cost_kg ,2)))
                worksheet.write(row,col+11,str(round(net_k*n_cost_kg ,2)))
                worksheet.write(row,col+12,yield1)
            elif previous_crop== 9:
                val=9
                n_lost=75
                p_lost=37
                k_lost=162.5
                n_required=180
                p_required=60
                k_required=90
                yield1=2500
                net_n=size1*n_required-size1*n_lost
                net_p=size1*p_required-size1*p_lost
                net_k=size1*k_required-size1*k_lost
                print("Dear farmers, The amount of N to be added is " + str(round(net_n,2)) + " and its cost is " + str(round(net_n*n_cost_kg ,2)))
                print("Dear farmers, The amount of p to be added is " + str(round(net_p,2)) + " and its cost is " + str(round(net_p * p_cost_kg,2)))
                print("Dear farmers, The amount of k to be added is " + str(round(net_k,2)) + " and its cost is " + str(round(net_k *k_cost_kg,2)))
                worksheet.write(row,col+6,str(net_n))
                worksheet.write(row,col+7,str(net_p))
                worksheet.write(row,col+8,str(net_k))
                worksheet.write(row,col+9,str(round(net_n*n_cost_kg ,2)))
                worksheet.write(row,col+10,str(round(net_p*n_cost_kg ,2)))
                worksheet.write(row,col+11,str(round(net_k*n_cost_kg ,2)))
                worksheet.write(row,col+12,yield1)
            elif previous_crop== 10:
                val=10
                n_lost=70
                p_lost=49
                k_lost=126
                n_required=250
                p_required=75
                k_required=190
                yield1=7000
                net_n=size1*n_required-size1*n_lost
                net_p=size1*p_required-size1*p_lost
                net_k=size1*k_required-size1*k_lost
                print("Dear farmers, The amount of N to be added is " + str(round(net_n,2)) + " and its cost is " + str(round(net_n*n_cost_kg ,2)))
                print("Dear farmers, The amount of p to be added is " + str(round(net_p,2)) + " and its cost is " + str(round(net_p * p_cost_kg,2)))
                print("Dear farmers, The amount of k to be added is " + str(round(net_k,2)) + " and its cost is " + str(round(net_k *k_cost_kg,2)))  
                worksheet.write(row,col+6,str(net_n))
                worksheet.write(row,col+7,str(net_p))
                worksheet.write(row,col+8,str(net_k))
                worksheet.write(row,col+9,str(round(net_n*n_cost_kg ,2)))
                worksheet.write(row,col+10,str(round(net_p*n_cost_kg ,2)))
                worksheet.write(row,col+11,str(round(net_k*n_cost_kg ,2)))
                worksheet.write(row,col+12,yield1)
            elif previous_crop == 11:
                val=11
                n_lost=32
                p_lost=14
                k_lost=19
                n_required=120
                p_required=60
                k_required=60
                yield1=3200
                net_n=size1*n_required-size1*n_lost
                net_p=size1*p_required-size1*p_lost
                net_k=size1*k_required-size1*k_lost
                print("Dear farmers, The amount of N to be added is " + str(round(net_n,2)) + " and its cost is " + str(round(net_n*n_cost_kg ,2)))
                print("Dear farmers, The amount of p to be added is " + str(round(net_p,2)) + " and its cost is " + str(round(net_p * p_cost_kg,2)))
                print("Dear farmers, The amount of k to be added is " + str(round(net_k,2)) + " and its cost is " + str(round(net_k *k_cost_kg,2)))
                worksheet.write(row,col+6,str(net_n))
                worksheet.write(row,col+7,str(net_p))
                worksheet.write(row,col+8,str(net_k))
                worksheet.write(row,col+9,str(round(net_n*n_cost_kg ,2)))
                worksheet.write(row,col+10,str(round(net_p*n_cost_kg ,2)))
                worksheet.write(row,col+11,str(round(net_k*n_cost_kg ,2)))
                worksheet.write(row,col+12,yield1)
            elif previous_crop == 12:
                val=12    
                n_lost=14.4
                p_lost=3.2
                k_lost=13.6
                n_required=20
                p_required=60
                k_required=20
                yield1=788
                net_n=size1*n_required-size1*n_lost
                net_p=size1*p_required-size1*p_lost
                net_k=size1*k_required-size1*k_lost
                print("Dear farmers, The amount of N to be added is " + str(round(net_n,2)) + " and its cost is " + str(round(net_n*n_cost_kg ,2)))
                print("Dear farmers, The amount of p to be added is " + str(round(net_p,2)) + " and its cost is " + str(round(net_p * p_cost_kg,2)))
                print("Dear farmers, The amount of k to be added is " + str(round(net_k,2)) + " and its cost is " + str(round(net_k *k_cost_kg,2))) 
                worksheet.write(row,col+6,str(net_n))
                worksheet.write(row,col+7,str(net_p))
                worksheet.write(row,col+8,str(net_k))
                worksheet.write(row,col+9,str(round(net_n*n_cost_kg ,2)))
                worksheet.write(row,col+10,str(round(net_p*n_cost_kg ,2)))
                worksheet.write(row,col+11,str(round(net_k*n_cost_kg ,2)))
                worksheet.write(row,col+12,yield1)
            #size2=size1.text()
            #previous=previous1.text()
            values_test=[p,t,r,rel]
            y_pred_test = classifier.predict(values_test)
            
            print(y_pred_test)
            if(y_pred_test==0):
                print("Crop is Wheat")  
                worksheet.write(row,col+13,'Wheat')
                worksheet.write(row,col+14,1625)
            elif(y_pred_test==1):
               print ("Crop is Rice \n ")
               worksheet.write(row,col+13,'Rice')
               worksheet.write(row,col+14,1470)
        
      
        
            elif(y_pred_test==2):
                print ("Crop is Maize") 
                worksheet.write(row,col+13,'Maize')
                worksheet.write(row,col+14,1365)    
        
    
            elif(y_pred_test==3):
                print ("Crop is Green g")
                worksheet.write(row,col+13,'Green Gram')
                worksheet.write(row,col+14,4000)
                

          
    
    
            elif(y_pred_test==4):
                print ("Crop is Pea")
                worksheet.write(row,col+13,'Pea')
                worksheet.write(row,col+14,1410)
            elif(y_pred_test==5):
                print ("Crop is pigeon pea")     
                worksheet.write(row,col+13,'Pigeon Pea')
                worksheet.write(row,col+14,1410)
                
             
                
            elif(y_pred_test==6):
                print ("Crop is Sunflower")
                worksheet.write(row,col+13,'SunFlower')      
                worksheet.write(row,col+14,3300)    
    
            elif(y_pred_test==7):
                print ("Crop is Onion")
                worksheet.write(row,col+13,'Onion')
                worksheet.write(row,col+14,4000)
                
            
            elif(y_pred_test==8):
                print ("Crop is Millets")
                worksheet.write(row,col+13,'Millets')
                worksheet.write(row,col+14,2000)
      
    
            elif(y_pred_test==9):
                print ("Crop is Potato")
                worksheet.write(row,col+13,'Potato')
                worksheet.write(row,col+14,2200)
              
            
            elif(y_pred_test==10):
                print ("Crop is Sugarcane")
                worksheet.write(row,col+13,'Sugarcane')
                worksheet.write(row,col+14,400)
              
            
            elif(y_pred_test==11):
                print ("Crop is Cotton")
                worksheet.write(row,col+13,'Cotton')
                worksheet.write(row,col+14,5000)
              
            elif(y_pred_test==12):
                print ("Crop is Soyabean")
                worksheet.write(row,col+13,'Soyabean')
                worksheet.write(row,col+14,5000)
            workbook.close()    
        QtCore.QMetaObject.connectSlotsByName(Form)
        
            
        self.pushButton.clicked.connect(greport)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "GO", None))
        self.label.setText(_translate("Form", "CROP DETAILS", None))
        self.label_2.setText(_translate("Form", "Tempertaure", None))
        self.label_3.setText(_translate("Form", "Rainfall", None))
        self.label_4.setText(_translate("Form", "pH", None))
        self.label_5.setText(_translate("Form", "Relative Humidity", None))
        self.label_6.setText(_translate("Form", "Area(Hectres)", None))
        self.comboBox.setItemText(0, _translate("Form", "Wheat", None))
        self.comboBox.setItemText(1, _translate("Form", "Rice", None))
        self.comboBox.setItemText(2, _translate("Form", "Maize", None))
        self.comboBox.setItemText(3, _translate("Form", "Green Gram", None))
        self.comboBox.setItemText(4, _translate("Form", "Pea", None))
        self.comboBox.setItemText(5, _translate("Form", "Pigeon Pea", None))
        self.comboBox.setItemText(6, _translate("Form", "Sunflower", None))
        self.comboBox.setItemText(7, _translate("Form", "Onion", None))
        self.comboBox.setItemText(8, _translate("Form", "Millet", None))
        self.comboBox.setItemText(9, _translate("Form", "Potato", None))
        self.comboBox.setItemText(10, _translate("Form", "Sugarcane", None))
        self.comboBox.setItemText(11, _translate("Form", "Cotton", None))
        self.comboBox.setItemText(12, _translate("Form", "Soybean", None))
        self.label_8.setText(_translate("Form", "Last Crop", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

