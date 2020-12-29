# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import math
import json
import os
from tkinter import filedialog
import tkinter as tk
from PIL import Image
from PyQt5.QtGui import QPixmap, QImage


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 598)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 53, 53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 57, 57))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 53, 53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 57, 57))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(53, 53, 53))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 47, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Title = QtWidgets.QLabel(self.page)
        self.Title.setMaximumSize(QtCore.QSize(769, 140))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setTextFormat(QtCore.Qt.RichText)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.verticalLayout_2.addWidget(self.Title)
        self.widget = QtWidgets.QWidget(self.page)
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(150, 150, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 170, 0);\n"
"    font-color:\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 150, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 170, 0);\n"
"    font-color:\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.widget)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(9, 9, 250, 170))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(9, 360, 250, 170))
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(9, 185, 250, 169))
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(265, 185, 250, 169))
        self.label_4.setText("")
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(265, 360, 250, 170))
        self.label_5.setText("")
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(265, 9, 250, 170))
        self.label_6.setText("")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(521, 185, 250, 169))
        self.label_7.setText("")
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(521, 9, 250, 170))
        self.label_8.setText("")
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(521, 360, 250, 170))
        self.label_9.setText("")
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.button_click()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CBIR Using Color and Shape Dechiptors"))
        self.Title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#eaa400;\">CBIR Using Color and Shape Dechiptors</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Refresh Database"))
        self.pushButton_2.setText(_translate("MainWindow", "Search Image"))

    def button_click(self):
        self.pushButton.clicked.connect(self.refreshDatabase)
        self.pushButton_2.clicked.connect(self.searchImage)
        pass

    def displayImage(self, listImage):
        for index, img in enumerate(listImage):
            # print(img)
            # print('Successfull read')
            self.stackedWidget.setCurrentIndex(1)
            img = 'image/'+img

            if index == 0:
                self.label.setPixmap(QtGui.QPixmap(img))
            elif index == 1:
                self.label_2.setPixmap(QtGui.QPixmap(img))
            elif index == 2:
                self.label_3.setPixmap(QtGui.QPixmap(img))
            elif index == 3:
                self.label_4.setPixmap(QtGui.QPixmap(img))
            elif index == 4:
                self.label_5.setPixmap(QtGui.QPixmap(img))
            elif index == 5:
                self.label_6.setPixmap(QtGui.QPixmap(img))
            elif index == 6:
                self.label_7.setPixmap(QtGui.QPixmap(img))
            elif index == 7:
                self.label_8.setPixmap(QtGui.QPixmap(img))
            elif index == 8:
                self.label_9.setPixmap(QtGui.QPixmap(img))
            else:
                break

    def searchImage(self):
        fname = self.openWindow()
        _, _, moments, img = self.main(fname)
        Hasil = self.fetchDatabase(moments.tolist())
        Hasil = dict(sorted(Hasil.items(), key=lambda item: item[1]))
        # print(Hasil)
        self.displayImage(Hasil)

    def canberraDistance(self, A : list, B : list):
        total = 0
        for i in range(7):
            top = abs(A[i]-B[i])
            bottom = abs(A[i]) + abs(B[i])
            total += top/bottom
            pass
        return total

    def fetchDatabase(self, imageQquery : list):
        result = []
        object = {}
        fjson = open('DatabaseMoments.json')
        dataMoment = json.load(fjson)
        for i in dataMoment:
            fname = dataMoment[i]['Name']
            fmoments = dataMoment[i]['moments']
            value = self.canberraDistance(imageQquery, fmoments)
            object[fname] = value
        return object

    def refreshDatabase(self):
        dbImages = {}
        for index, img in enumerate(self.listImg()):
            dir = 'image/'+img
            stdValue, stdDotValue, moments, citra = self.main(dir)
            objImg = {
                "Name": img,
                # "value1": stdValue,
                # "value2": stdDotValue,
                "moments": moments.tolist()
            }
            dbImages[index] = objImg

        with open('DatabaseMoments.json', 'w') as outfile:
            json.dump(dbImages, outfile)

    def listImg(self):
        for (root, dirs, fname) in os.walk('image', topdown=True):
            return fname
        pass

    def main(self, fImg: str = 'image/flower1.jpg'):
        clrImg = cv.imread(fImg)
        # clrImg = cv.imread('image/flower1.jpg')

        scale_percent = 50
        #calculate the 50 percent of original dimensions
        width = int(clrImg.shape[1] * scale_percent / 100)
        height = int(clrImg.shape[0] * scale_percent / 100)
        dsize = (width, height)

        clrImg = cv.resize(clrImg, dsize)


        # #Plot
        # plt.imshow(cv.cvtColor(clrImg, cv.COLOR_BGR2RGB))
        # plt.show()

        # Convert to Lab
        labImg = cv.cvtColor(clrImg, cv.COLOR_BGR2RGB)
        labImg = cv.cvtColor(labImg, cv.COLOR_RGB2Lab)

        # Getting L Value from labImg
        splitImg = labImg
        L, a, b = cv.split(splitImg)
        # print(L[332,348])
        # splitImg[:,:,0] = 0
        # splitImg[:,:,2] = 0
        # splitImg[:,:,1] = 0

        # Convert to Grayscale
        grayImg = splitImg[:,:,0]

        # Gaussian Blur
        blrImg = cv.GaussianBlur(grayImg, (3,3), 0)

        # Gradient Image using Sobel
        kernelSize = 1
        sobelx = cv.Sobel(blrImg,cv.CV_64F,1,0,ksize=kernelSize)
        abs_sobelx = np.absolute(sobelx)
        sobel_x = np.uint8(abs_sobelx)
        sobely = cv.Sobel(blrImg,cv.CV_64F,0,1,ksize=kernelSize)
        abs_sobely = np.absolute(sobely)
        sobel_y = np.uint8(abs_sobely)

        sobelImg = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
        # gradient_magnitude = np.sqrt(np.square(sobel_x) + np.square(sobel_y))
        # gradient_magnitude *= 255.0 / gradient_magnitude.max()


        # Standard Deviation Gradient Image
        stdValue = np.std(sobelImg)
        ret,thresh1 = cv.threshold(sobelImg,stdValue,255,cv.THRESH_BINARY)
        dotImg = cv.multiply(sobelImg, thresh1)
        stdDotValue = np.std(dotImg)

        # menghitung Moment pada Gambar
        # countour, hierarchy = cv.findContours(dotImg, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        # countourImg = cv.drawContours(clrImg, countour, -1, (0,255,0), 1)
        MomentsImg = cv.HuMoments(cv.moments(dotImg)).flatten()
        #
        for i in range(7):
            MomentsImg[i] = -1 * math.copysign(1.0, MomentsImg[i]) * math.log10(abs(MomentsImg[i]))

        # cv.imshow('Original Image', clrImg)
        # cv.imshow('Lab Color Image', labImg)
        # cv.imshow('Blur Lab Image', blrImg)
        # cv.imshow('Grayscale form LabImg', grayImg)
        # cv.imshow('Sobel X', sobel_x)
        # cv.imshow('Sobel Y', sobel_y)
        # cv.imshow('Final Sobel', sobelImg)
        # cv.imshow('Binary Image', thresh1)
        # cv.imshow('Contour Image', countourImg)
        # # cv.imshow('2 Images. Sobel | Binary', dotImg)
        # cv.waitKey()
        # cv.destroyAllWindows()

        # clrImg = cv.cvtColor(clrImg, cv.COLOR_BGR2RGB)
        # print('RGB Value of (348,332) to (352,336): ')
        # print(clrImg[332:335, 348:351])
        # print()
        # print('Lab Value of (348,332) to (352,336): ')
        # print(labImg[331:336, 347:352])
        # print()
        # print('Grayscale Lab of (348,332) to (352,336): ')
        # print(grayImg[331:336, 347:352])
        # print()
        # print('Blur Lab Value of (348,332) to (352,336): ')
        # print(blrImg[331:336, 347:352])
        # print()
        # print('Sobel X Image of (348,332) to (352,336): ')
        # print(sobel_x[332:335, 348:351])
        # print()
        # print('Sobel Y Image of (348,332) to (352,336): ')
        # print(sobel_y[332:335, 348:351])
        # print()
        # print('Sobel Image of (348,332) to (352,336): ')
        # print(sobelImg[332:335, 348:351])
        # print()
        # print('Thresholding Image of (348,332) to (352,336): ')
        # print(thresh1[332:335, 348:351])
        # print()
        # print('Dot Product Image of (348,332) to (352,336): ')
        # print(dotImg[332:335, 348:351])
        # print(MomentsImg)

        # return stdValue

        # print(fImg, ': ', stdValue, ' ', stdDotValue)
        # print(MomentImg)
        return stdValue, stdDotValue, MomentsImg, dotImg

    def openWindow(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
