# -*- coding: utf-8 -*-
import sys
from os.path import dirname, normpath
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QCoreApplication

ROOT = dirname(dirname(__file__))
sys.path.append(ROOT)
import inkwell  # noqa

QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
QApplication.setStyle('default')


if __name__ == "__main__":
    app = QApplication()
    window = QUiLoader().load(normpath(f'{ROOT}/example/main.ui'))
    inkwell.applyStyleSheet(window)
    window.show()
    app.exec()
