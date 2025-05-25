#intall qr code module for the qr code import 

import qrcode as qr
from PIL import Image
#function to generate qr code & the link is attached.
img = qr.make("https://github.com/cracktivities1/Python")
#image created 
img.save("qrcode.png")
