# printer
# pip install pywin32
import os,sys
import win64print
import win32api

printer_name = win64print.GetDefaultPrinter()
print(printer_name)