# used this file to compile fils in src folder and put them in the dist folder
# used following command: "python compiler.py py2exe"

from distutils.core import setup
import py2exe

setup(windows=['main.py'])
