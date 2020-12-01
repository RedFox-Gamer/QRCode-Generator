#pip install pyqrcode
#pip install pypng
import pyqrcode
import png
from pyqrcode import QRCode

#This is the link where you want to get after scanning the QR code
QRstring = "Link goes here" 
url = pyqrcode.create(QRstring)
url.png(r"C:\Your\Directory\Goes\Here\qrcode.png", scale = 8)