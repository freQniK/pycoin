#!/bin/env python3

import os
import qrcode
from os import getcwd, path
from PIL import Image
from PIL import ImageDraw, ImageFont
from PIL import ImageOps
    
local_dir = getcwd()    
IMGDIR = path.join(local_dir, "coin_imgs")

def QRCode(DepositCoin, DepositAddress):
    

    coinLogo =  DepositCoin + '.png'
    logo = Image.open(coinLogo)
    basewidth = 100
     
    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize))
    
    QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    QRcode.add_data(DepositAddress)
    QRcode.make()

    QRimg = QRcode.make_image(fill_color='Black', back_color="white").convert('RGB')
     
    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
           (QRimg.size[1] - logo.size[1]) // 2)
    
    QRimg.paste(logo, pos)
    
    # crop a bit
    border = (0, 4, 0, 30) # left, top, right, bottom
    QRimg = ImageOps.crop(QRimg, border)
    
    
    # Next Process is adding and centering the Deposit address on the image
    # Creating a background a little larger and pasting the QR
    # Image onto it with the text
    if len(DepositAddress) <= 50:
        fontSize = 12
    elif len(DepositAddress) <=75:
        fontSize = 11
    else:
        fontSize = 10
        
    background = Image.new('RGBA', (QRimg.size[0], QRimg.size[1] + 15), (255,255,255,255))
    robotoFont = ImageFont.truetype('Roboto-BoldItalic.ttf', fontSize)

    draw = ImageDraw.Draw(background)
    w,h  = draw.textsize(DepositAddress)
    draw.text(((QRimg.size[0]+15 - w)/2,QRimg.size[1]-2),DepositAddress, (0,0,0), font=robotoFont)
    
    background.paste(QRimg, (0,0))
    background.save(os.path.join(IMGDIR, DepositCoin + "-TO" + ".png"))
    to_coin_img = os.path.join(IMGDIR, DepositCoin + "-TO" + ".png")
    print(os.path.isfile(to_coin_img)) 
    #display
    img = Image.open(to_coin_img)
    img.show()
    
    
def main():
    DepositCoin = input("Coin: ")
    DepositAddress = input("Address: ")
    QRCode(DepositCoin, DepositAddress)

if __name__ == '__main__': 
    main()
