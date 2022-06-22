import pyqrcode
from pyqrcode import QRCode

address = 'https://www.mobile.bg/pcgi/mobile.cgi?act=4&adv=11564561642177549&slink=n96fep'
url = pyqrcode.create(address)
url.png('Ferrari.png', scale=8)
