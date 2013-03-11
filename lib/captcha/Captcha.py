__author__ = 'Dipak Malla'
import Image, ImageDraw, ImageFont
import random
import string
class Captcha:
    def __init__(self):
        #Call All Necessary Functions With Default Values.
        #TODO Need to change way of default value assignment of setText :)
        self.setFont().setColor().setSize().setText((self.__token()[0],self.__token()[0],self.__token()[0],self.__token()[0],self.__token()[0]))
    def setFont(self,font=("/media/Backup/Projects/UbuntuMono-RI.ttf",38)):
        #Will set Font and Font size.
        self.__font = font
        return self
    def setSize(self,size=(200,100)):
        #Will Set Size of the image.
        self.__size = size
        return self
    def setColor(self,color=(24,68,90)):
        #Will Set color of image.
        self.__color = color
        return self
    def setText(self,text=()):
        #Will Set Text
        self.__text = text
        return self
    def __token(self):
        #TODO
        #Just to Generate Random Character.
        st = ''
        for i in range(1,40):
            st = st + random.choice(string.ascii_uppercase)
        return st + str(random.randrange(1,98887776783883,1)) + random.choice(string.ascii_lowercase)
    def CreateImage(self):
        try:
            im = Image.new("RGB",self.__size)
            draw = ImageDraw.Draw(im)
            fonts = ImageFont.truetype(self.__font[0],self.__font[1])
            #TODO
            #Write text on image background ;)
            for d in range(0,self.__size[0]):
                for i in range(0,self.__size[1]):
                    draw.text((d*8,i*8),self.__token()[0])
            #Free draw object
            draw.text((20,5),self.__text[0],font=fonts,fill=(0,0,255))
            draw.text((40,5),self.__text[1],font=fonts,fill=(0,0,255))
            draw.text((90,45),self.__text[2],font=fonts,fill=(0,0,255))
            draw.text((110,45),self.__text[3],font=fonts,fill=(0,0,255))
            del draw
            #return image.
            return im
        except Exception,e:
            return e[0]


