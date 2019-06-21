# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Notebook.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, Qt
from PyQt5.QtGui import QPixmap, QIcon, QFont, QPalette, QBrush
import ctypes
import sys
import os
import yolo3_predict
import threading
from timeit import default_timer as timer
import time


def GetFileName(file_dir):
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                file_list.append(os.path.join(root, file).replace('\\', '/'))
    return file_list


class ThreadPredict(QThread):
    def __init__(self, img_list, save_path):
        self.img_list = img_list
        self.save_path = save_path
        super(ThreadPredict, self).__init__()

    def run(self):
        yolo3_predict.detect_img_for_test(self.img_list, self.save_path)


class UiMainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("img/background.png")))
        self.setPalette(palette)  # 设置窗口背景

        self.setGeometry(50, 50, 1024, 633)
        self.setWindowTitle('Object Detection')
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("icon/icon.ico")  # 设置任务栏图标
        self.setWindowIcon(QtGui.QIcon('icon/icon.ico'))  # 设置窗口图标

        self.label = QtWidgets.QLabel("请选择图片所在文件夹", self)
        self.label1 = QtWidgets.QLabel(self)
        self.label2 = QtWidgets.QLabel(self)
        self.text_label1 = QtWidgets.QLabel(self)
        self.text_label2 = QtWidgets.QLabel(self)
        self.cnt = 0
        self.save_path = ""
        self.path = ""
        self.img_list = GetFileName(self.path)
        self.threads = [True, True]
        self.initui()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 816, 23))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_setting = QtWidgets.QMenu(self.menubar)
        self.menu_setting.setObjectName("menu_setting")
        self.menu_start = QtWidgets.QMenu(self.menubar)
        self.menu_start.setObjectName("menu_start")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Open = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/folder-open-fill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Open.setIcon(icon)
        self.action_Open.setObjectName("action_Open")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_save_path = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/folder"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_save_path.setIcon(icon1)
        self.action_save_path.setObjectName("action_save_path")
        self.action_start = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/caret-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_start.setIcon(icon2)
        self.action_start.setObjectName("action_start")
        self.action_last = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/arrowleft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_last.setIcon(icon3)
        self.action_last.setObjectName("action_last")
        self.action_next = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/arrowright.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_next.setIcon(icon4)
        self.action_next.setObjectName("action_next")
        self.menu_file.addSeparator()
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_Open)
        self.menu_file.addAction(self.action_Exit)
        self.menu_setting.addAction(self.action_save_path)
        self.menu_start.addAction(self.action_start)
        self.menu_start.addAction(self.action_last)
        self.menu_start.addAction(self.action_next)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_setting.menuAction())
        self.menubar.addAction(self.menu_start.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Open)
        self.toolBar.addAction(self.action_save_path)
        self.toolBar.addAction(self.action_last)
        self.toolBar.addAction(self.action_start)
        self.toolBar.addAction(self.action_next)

        self.retranslateui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_file.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_setting.setTitle(_translate("MainWindow", "设置"))
        self.menu_start.setTitle(_translate("MainWindow", "开始"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_Open.setText(_translate("MainWindow", "打开文件(&CTRL+O)"))
        self.action_Open.setShortcut('CTRL+O')
        self.action_Open.triggered.connect(self.opendir)
        self.action_Exit.setText(_translate("MainWindow", "退出(&ALT+F4)"))
        self.action_Exit.setShortcut('ALT+F4')
        self.action_Exit.triggered.connect(self.close)
        self.action_save_path.setText(_translate("MainWindow", "存储路径"))
        self.action_save_path.triggered.connect(self.save_dir)
        self.action_save_path.setEnabled(False)
        self.action_start.setText(_translate("MainWindow", "开始"))
        self.action_start.setShortcut('CTRL+S')
        self.action_start.setEnabled(False)
        self.action_start.triggered.connect(self.start_event)
        self.action_last.setText(_translate("MainWindow", "上一张(&LEFT)"))
        self.action_last.setShortcut('LEFT')
        self.action_last.setEnabled(False)
        self.action_last.triggered.connect(self.on_clicked_last)
        self.action_next.setText(_translate("MainWindow", "下一张(&RIGHT)"))
        self.action_next.setShortcut('RIGHT')
        self.action_next.setEnabled(False)
        self.action_next.triggered.connect(self.on_clicked_next)

    def initui(self):
        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.red)  # 设置字体颜色
        # pe.setColor(QPalette.Window, Qt.lightGray)  # 设置背景颜色

        self.label.setFont(QFont("Roman times", 12, QFont.Bold))
        # 设置标签颜色背景字体等
        self.label.setStyleSheet("QLabel{background:rgb(95,158,160);}"
                                 "QLabel{color:white;font-size:16px;font-weight:bold;font-family:宋体;}")
        self.label.setGeometry(0, 60, 300, 50)
        self.label.setAlignment(Qt.AlignCenter)  # 文字居中

        self.label1.setPixmap(QPixmap('img/background11.png').scaled(800, 800))
        self.label1.setScaledContents(True)
        self.label1.setGeometry(155, 120, 800, 800)

        self.label2.setPixmap(QPixmap('img/background11.png').scaled(800, 800))
        self.label2.setScaledContents(True)
        self.label2.setGeometry(955, 120, 800, 800)

        # self.text_label1.setText('原图')
        # self.text_label1.setFont(QFont("Roman times", 12, QFont.Bold))
        # self.text_label1.setAutoFillBackground(True)
        # self.text_label1.setPalette(pe)
        # self.text_label1.setAlignment(Qt.AlignCenter)
        # self.text_label1.setGeometry(550, 90, 100, 20)

        # self.text_label2.setText('检测结果')
        # self.text_label2.setFont(QFont("Roman times", 12, QFont.Bold))
        # self.text_label2.setAutoFillBackground(True)
        # self.text_label2.setPalette(pe)
        # self.text_label2.setAlignment(Qt.AlignCenter)
        # self.text_label2.setGeometry(1355, 90, 100, 20)

    def opendir(self):
        self.action_save_path.setEnabled(True)
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "选择文件夹", r"C:\Users\17020\dp_learning\keras-yolo3")
        self.label.setText("请选择图片保存路径")
        self.path = directory
        self.img_list = GetFileName(directory)
        print(len(self.img_list))
        print(directory)

    def save_dir(self):
        self.action_start.setEnabled(True)
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "选择文件夹", r"C:\Users\17020\dp_learning\keras-yolo3")
        self.label.setText("点击按钮开始检测")
        self.save_path = directory
        print(directory)

    def predict(self):
        img_list = GetFileName(self.path)
        save_img_list = GetFileName(self.save_path)
        predict_list = []
        imgnamelist = []
        for j in range(len(save_img_list)):
            imgnamelist.append(save_img_list[j].split('/')[-1])
        for i in range(len(img_list)):
            if img_list[i].split('/')[-1] not in imgnamelist:
                predict_list.append(img_list[i])

        if len(predict_list) is not 0:
            yolo3_predict.detect_img_for_test(predict_list, self.save_path)

    def check(self):
        """判断检测是否完成"""
        start = timer()
        while True:
            time.sleep(0.05)
            length1 = len(GetFileName(self.path))
            length2 = len(GetFileName(self.save_path))
            if length1 == length2:
                # self.button_last.setEnabled(True)
                # self.button_next.setEnabled(True)
                self.label.setText("检测完成")
                self.action_last.setEnabled(True)
                self.action_next.setEnabled(True)
                break
            if length2 is 0:
                self.label.setText("模型加载中......")

            if length2:
                # self.button_last.setEnabled(False)
                # self.button_next.setEnabled(False)
                self.label.setText("检测正在进行中...{}/{}".format(length2, length1))
                self.label1.setPixmap(QPixmap(self.img_list[length2 - 1]))
                self.label2.setPixmap(QPixmap(
                    "{}/{}".format(self.save_path, self.img_list[length2 - 1].split('/')[-1])))
        end = timer()
        self.label.setText("检测{}张图片完成 耗时:{}s".format(length1, int(end - start)))

    def start_event(self):
        self.action_start.setEnabled(False)
        self.img_list = GetFileName(self.path)
        self.label.setText("检测正在进行中......")
        t = threading.Thread(target=self.predict)  # 检测的线程
        t.start()
        t_check = threading.Thread(target=self.check)  # 检测是否完成的线程
        t_check.start()
        self.threads = [t, t_check]
        # self.start_button.setEnabled(False)

    def on_clicked_last(self):
        """点击上一张"""
        self.cnt -= 1
        self.label1.setPixmap(QPixmap(self.img_list[self.cnt % len(self.img_list)]))
        self.label2.setPixmap(QPixmap(
            "{}/{}".format(self.save_path, self.img_list[self.cnt % len(self.img_list)].split('/')[-1])))

    def on_clicked_next(self):
        """点击下一张"""
        self.cnt += 1
        self.label1.setPixmap(QPixmap(self.img_list[self.cnt % (len(self.img_list))]))
        self.label2.setPixmap(QPixmap(
            "{}/{}".format(self.save_path, self.img_list[self.cnt % len(self.img_list)].split('/')[-1])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UiMainWindow()
    ex.show()
    app.exec_()
