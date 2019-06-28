# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtJson.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
import threading

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from time import sleep
import time
import example as ex
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QBoxLayout
from WeatherSync import WeatherSync


class Ui_QtJsonClass(object):

    def setupUi(self, QtJsonClass):
        QtJsonClass.setObjectName("QtJsonClass")
        QtJsonClass.setWindowModality(QtCore.Qt.ApplicationModal)
        QtJsonClass.resize(1280, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QtJsonClass.sizePolicy().hasHeightForWidth())
        QtJsonClass.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        # palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        # palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        # palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        QtJsonClass.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(96)
        font.setBold(False)
        # font.setWeight(75)
        QtJsonClass.setFont(font)
        QtJsonClass.setAutoFillBackground(False)
        self.gridLayoutWidget = QtWidgets.QWidget(QtJsonClass)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(100, 0, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        self.lblTime = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTime.sizePolicy().hasHeightForWidth())
        self.lblTime.setSizePolicy(sizePolicy)
        self.lblTime.setMinimumSize(QtCore.QSize(0, 450))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(180)
        self.lblTime.setFont(font)

        self.lblTime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTime.setScaledContents(True)
        self.lblTime.setAlignment(QtCore.Qt.AlignRight)
        self.lblTime.setObjectName("lblTime")
        self.gridLayout.addWidget(self.lblTime, 1, 0, 1, 1)
        self.lblDate = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDate.sizePolicy().hasHeightForWidth())
        self.lblDate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(100)
        self.lblDate.setFont(font)
        self.lblDate.setToolTipDuration(0)
        self.lblDate.setLineWidth(0)
        self.lblDate.setTextFormat(QtCore.Qt.PlainText)
        self.lblDate.setAlignment(QtCore.Qt.AlignLeft)
        self.lblDate.setObjectName("lblDate")
        self.gridLayout.addWidget(self.lblDate, 0, 0, 1, 2)

        self.lblSeconds = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblDate.sizePolicy().hasHeightForWidth())
        self.lblSeconds.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(75)
        self.lblSeconds.setFont(font)
        self.lblSeconds.setMinimumSize(QtCore.QSize(0, 75))
        # self.lblSeconds.setMaximumSize(QtCore.QSize(200,0))
        self.lblSeconds.setToolTipDuration(0)
        self.lblSeconds.setLineWidth(0)
        self.lblSeconds.setTextFormat(QtCore.Qt.PlainText)
        self.lblSeconds.setObjectName("lblSeconds")
        self.lblSeconds.setAlignment(QtCore.Qt.AlignLeft)
        self.gridLayout.addWidget(self.lblSeconds, 1, 1, 1, 1)

        self.lblWeather = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblWeather.sizePolicy().hasHeightForWidth())
        self.lblWeather.setSizePolicy(sizePolicy)
        self.lblWeather.setMaximumSize(250, 250)
        # self.lblWeather.resize(50,50)
        self.lblWeather.setObjectName("lblWeather")

        pixmap = self.set_weathericon(0)
        self.lblWeather.setPixmap(QPixmap(pixmap))

        self.gridLayout.addWidget(self.lblWeather, 0, 1, 1, 2)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(QtJsonClass)

    upper_line = ""
    lower_line = ""

    def retranslateUi(self):
        current_time = set_time()
        upper_line = '\n' + current_time[0] + " " + current_time[1]
        lower_time = get_time(current_time[2], current_time[3])
        lower_seconds = '\n' + " " + current_time[4]
        self.lblTime.setText(lower_time)
        self.lblDate.setText(upper_line)
        self.lblSeconds.setText(lower_seconds)

    def set_weathericon(self, weather_condition):
        if weather_condition == 0:
            self.lblWeather.setPixmap(QPixmap("Sunny1"))
        if weather_condition == 1:
            self.lblWeather.setPixmap(QPixmap("Cloudy1"))
        if weather_condition == 2:
            self.lblWeather.setPixmap(QPixmap("Rainy1"))
        if weather_condition == 3:
            self.lblWeather.setPixmap(QPixmap("Snowy"))

    colon = False


def colon_shift():
    if Ui_QtJsonClass.colon:
        string = " "
    else:
        string = ":"
    Ui_QtJsonClass.column = ~Ui_QtJsonClass.column
    return string


def get_time(hour, minute):
    # return colon_shift() + " " + minute.__str__() + " " + second.__str__()
    return hour.__str__() + " : " + minute.__str__()


def set_time() -> (str, str, str, str, str):
    date = time.strftime('%m-%d')
    weekday = getWeekday()
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    # now = datetime.datetime.now()
    # date = now.strftime('%m-%d')
    # weekday = getWeekday()
    # hour = now.strftime('%H')
    # minute = now.strftime('%M')

    return date, weekday, hour, minute, second


def getWeekday():
    now = datetime.date.today().weekday()
    if now == 0:
        return "MON"
    if now == 1:
        return "TUE"
    if now == 2:
        return "WED"
    if now == 3:
        return "THU"
    if now == 4:
        return "FRI"
    if now == 5:
        return "SAT"
    if now == 6:
        return "SUN"
    assert False, "Invalid WeekDay"


def set_stripcolor(weather_condition):
    ex.set_stripcolor(weather_condition)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    QtJsonClass = QtWidgets.QWidget()
    ui = Ui_QtJsonClass()
    ui.setupUi(QtJsonClass)
    QtJsonClass.showFullScreen()


    def time_refresh():
        ws = WeatherSync()
        condition = ws.get_weather_main()

        i = 0
        weather_refresh(condition)
        while True:
            i += 1
            if i % 16 == 0:
                weather_refresh(3)
            elif i % 12 == 0:
                weather_refresh(2)
            elif i % 8 == 0:
                weather_refresh(1)
            elif i % 4 == 0:
                weather_refresh(0)
            ui.retranslateUi()
            sleep(1)


    def weather_refresh(weather_condition):
        set_stripcolor(weather_condition)
        ui.set_weathericon(weather_condition)


    time_thread = threading.Thread(target=time_refresh)
    time_thread.start()
    app.exec_()
