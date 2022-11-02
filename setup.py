import sys
import os

from cx_Freeze import setup, Executable

files = ['images/baymed_logo_final.jpg',
        'ui/ui_mainwindow.py',
        'PandasToPyside.py',
        'SteelOrderToPandas.py']

Executable(script='main.py', base='Win32GUI')