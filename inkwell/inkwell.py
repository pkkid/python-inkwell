# -*- coding: utf-8 -*-
import os
import sass
from inkwell import ROOT, log
from os.path import dirname, normpath
from PySide6 import QtGui
from string import Template

DEFAULT_STYLESHEET = normpath(f'{ROOT}/inkwell.sass')
DEFAULT_FONTDIR = normpath(f'{ROOT}/fonts')
OUTLINE_STYLE = '\nQWidget { border:1px solid rgba(255,0,0,0.3) !important; }'


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
