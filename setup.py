from distutils.core import setup
import py2exe

setup(
  console=['iviewultimate.py'],
  options={
    "py2exe": {
      "unbuffered":True,
      "optimize": 2
    }
  }
)

'''import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["tkinter", "urllib3", "bs4"], "excludes": []}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "iviewultimate",
        version = "1.0",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("iviewultimate.py", base=base)])
'''
