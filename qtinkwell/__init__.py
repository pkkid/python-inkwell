# -*- coding: utf-8 -*-
import logging
import os
import sass
import sys
from os.path import dirname, normpath
from string import Template
from PySide6 import QtGui

VERSION = '1.0.0'
ROOT = dirname(__file__)
DEFAULT_STYLESHEET = normpath(f'{ROOT}/inkwell.sass')
DEFAULT_FONTDIR = normpath(f'{ROOT}/fonts')
OUTLINE_STYLE = '\nQWidget { border:1px solid rgba(255,0,0,0.3) !important; }'


# Custom logging formatter
class MyFormatter(logging.Formatter):
    def format(self, record):
        if 'module' in record.__dict__.keys():
            record.module = record.module[:10]
        return super(MyFormatter, self).format(record)


# Logging configuration
log = logging.getLogger(__name__)
logformat = MyFormatter('%(asctime)s %(module)10s:%(lineno)-4s %(levelname)-7s %(message)s')
streamhandler = logging.StreamHandler(sys.stdout)
streamhandler.setFormatter(logformat)
log.addHandler(streamhandler)
log.setLevel(logging.INFO)


def applyStyleSheet(qobj, filepath=DEFAULT_STYLESHEET, context=None, outline=False):
    """ Apply the specified stylesheet via libsass and add it to qobj. """
    context = {} if context is None else context
    context.update({'dir':dirname(filepath).replace('\\','/')})
    template = Template(open(filepath).read())
    styles = template.safe_substitute(context)
    styles = sass.compile(string=styles)
    styles += OUTLINE_STYLE if outline else ''
    qobj.setStyleSheet(styles)


def addApplicationFonts(dirpath=DEFAULT_FONTDIR):
    """ Load all ttf fonts from the specified dirpath. """
    for filename in os.listdir(dirpath):
        if filename.endswith('.ttf'):
            filepath = normpath(f'{dirpath}/{filename}')
            fontid = QtGui.QFontDatabase.addApplicationFont(filepath)
            fontname = QtGui.QFontDatabase.applicationFontFamilies(fontid)[0]
            log.info(f'Loading font {fontname}')
