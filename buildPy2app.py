"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
from glob import glob
import syncplay

APP = ['syncplayClient.py']
DATA_FILES = [
    ('resources', glob('resources/*.png') + glob('resources/*.rtf') + glob('resources/*.lua')),
]
OPTIONS = {
    'iconfile':'resources/icon.icns',
    'extra_scripts': 'syncplayServer.py',
    'includes': {'PySide2.QtCore', 'PySide2.QtUiTools', 'PySide2.QtGui','PySide2.QtWidgets', 'certifi'},
    'excludes': {'PySide', 'PySide.QtCore', 'PySide.QtUiTools', 'PySide.QtGui'},
    'qt_plugins': ['platforms/libqcocoa.dylib', 'platforms/libqminimal.dylib','platforms/libqoffscreen.dylib', 'styles/libqmacstyle.dylib'],
    'plist': {
        'CFBundleName':'Syncplay',
        'CFBundleShortVersionString':syncplay.version,
        'CFBundleIdentifier':'pl.syncplay.Syncplay',
        'LSMinimumSystemVersion':'10.11.0',
        'NSHumanReadableCopyright': '@ 2018 Syncplay All Rights Reserved'
        }
}

setup(
    app=APP,
    name='Syncplay',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
