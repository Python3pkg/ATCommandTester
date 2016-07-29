#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- author: chat@jat.email -*-

# from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, qApp, QAction, QMainWindow, QStatusBar, QMenuBar, QVBoxLayout
from PyQt5.QtGui import QIcon


class Main():
    def run(self, argv):
        app = QApplication(argv)

        w = MainWindow()

        return app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # http://doc.qt.io/qt-5/linguist-translators.html#alt-key-accelerators
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.resize(400, 300)
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())

        self.setWindowTitle('AT Command Tester')
        self.setWindowIcon(QIcon('logo.png'))

        self.show()

        self.windowHandle().setScreen(qApp.screens()[0])
