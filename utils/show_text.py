from machine import I2C,Pin
from ssd1306 import SSD1306_I2C
import math

chine=[
#/*--  文字:  执  --*/
#/*--  新宋体12;  此字体下对应的点阵为：宽x高=16x16   --*/
0x10,0x10,0x10,0xFF,0x10,0x90,0x00,0x10,0x10,0xFF,0x10,0x10,0xF0,0x00,0x00,0x00,
0x04,0x44,0x82,0x7F,0x01,0x80,0x40,0x21,0x1A,0x07,0x18,0x00,0x3F,0x40,0xF0,0x00,

#/*--  文字:  念  --*/
#/*--  新宋体12;  此字体下对应的点阵为：宽x高=16x16   --*/
0x40,0x40,0x20,0x20,0x90,0x88,0x94,0xE3,0x84,0x88,0x90,0x20,0x20,0x40,0x40,0x00,
0x40,0x30,0x00,0x00,0x38,0x40,0x40,0x44,0x5A,0x41,0x40,0x70,0x00,0x08,0x30,0x00,

#/*--  文字:  执  --*/
#/*--  新宋体12;  此字体下对应的点阵为：宽x高=16x16   --*/
0x10,0x10,0x10,0xFF,0x10,0x90,0x00,0x10,0x10,0xFF,0x10,0x10,0xF0,0x00,0x00,0x00,
0x04,0x44,0x82,0x7F,0x01,0x80,0x40,0x21,0x1A,0x07,0x18,0x00,0x3F,0x40,0xF0,0x00,

#/*--  文字:  战  --*/
#/*--  新宋体12;  此字体下对应的点阵为：宽x高=16x16   --*/
0x00,0x00,0x00,0xFF,0x08,0x08,0x08,0x40,0x40,0x40,0xFF,0x20,0x22,0xAC,0x20,0x00,
0x00,0x7F,0x21,0x21,0x21,0x21,0x7F,0x80,0x40,0x20,0x17,0x18,0x26,0x41,0xF0,0x00,


    ]
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c)
def ByteOpera(num,dat):
    byte= [0x01,0x02,0x04,0x8,0x10,0x20,0x40,0x80]
    if dat&byte[num]:
        return 1
    else:
        return 0
def hline(x0,y0,le,color):
    for i in range(le):
        oled.pixel(x0+i,y0,color)

def shuline(x0,y0,le,color):
    for i in range(le):
        oled.pixel(x0,y0+i,color)






class GUI:
    #画点
    def DrawDot(x,y):
        oled.pixel(x,y)
    #横线
    def hline(x0,y0,le,color):
        for i in range(le):
            oled.pixel(x0+i,y0,color)
     #竖线
    def shuline(x0,y0,le,color):
        for i in range(le):
            oled.pixel(x0,y0+i,color)

     ##########################
     #函数：Line
     #功能：任意画线
     #描述：
     #      x0,y0:起始位置
     #      x1,y1：终止位置
     #      color:颜色
     #
    def Line(x0,y0,x1,y1,color):
        dx=x1-x0
        if(dx>0):
            s1=1
        else:
            s1=-1
        dy=y1-y0
        if(dy>0):
            s2=1
        else:
            s2=-1
        dx=math.fabs(x1-x0)
        dy=math.fabs(y1-y0)
        if(dy>dx):
            temp=dx
            dx=dy
            dy=temp
            status=1
        else:
            status=0


        if(dx==0):
            hline(x0,y0,y1-y0,color)
        if(dy==0):
            shuline(x0,y0,x1-x0,color)

        sub=2*dy-dx
        for i in range(dx):
            oled.pixel(x0,y0,color)
            if(sub>0):
                if(status==1):
                    x0+=s1
                else:
                    y0+=s2
                sub-=2*dx
            if(status==1):
                y0+=s2
            else:
                x0+=s1
            sub+=2*dy
          #oled.show()

          #######################
          #画矩形函数
          #fill为是否填充，默认不填充
    def DrawBox(x0,y0,x1,y1,color=1,fill=0):
        if (fill==1):
            for i in range(y1-y0):
                hline(x0,y0+i,x1-x0,color)
        else:
            hline(x0,y0,x1-x0,color)
            hline(x0,y1,x1-x0,color)
            shuline(x0,y0,y1-y0,color)
            shuline(x1,y0,y1-y0,color)

        ##############################
        #画圆函数，很占CPU
        #fill 为是否填充
        #画两遍，是因为只画一遍的话中间有点画不上
    def DrawCircle_math(x,y,r,color,fill=0):
        if(fill==0):
            for i in range(x-r,x+r+1):
                oled.pixel(i,int(y-math.sqrt(r*r-(x-i)*(x-i))),color)
                oled.pixel(i,int(y+math.sqrt(r*r-(x-i)*(x-i))),color)
            for i in range(y-r,y+r+1):
                oled.pixel(int(x-math.sqrt(r*r-(y-i)*(y-i))),i,color)
                oled.pixel(int(x+math.sqrt(r*r-(y-i)*(y-i))),i,color)
        else:
            for i in range(x-r,x+r+1):
                a=int(math.sqrt(r*r-(x-i)*(x-i)))
                shuline(i,y-a,a*2,color)

            for i in range(y-r,y+r+1):
                a=int(math.sqrt(r*r-(y-i)*(y-i)))
                hline(x-a,i,a*2,color)


    #########################
    #画圆函数
    #网上的算法，不怎么圆
    def DrawCircle(x,y,r,color):
        a=0
        b=r
        di=3-2*r
        while a<b:
            oled.pixel(x-b,y-a,color)
            oled.pixel(x+b,y-a,color)
            oled.pixel(x-a,y+b,color)
            oled.pixel(x-b,y-a,color)
            oled.pixel(x-a,y-b,color)
            oled.pixel(x+b,y+a,color)
            oled.pixel(x+a,y-b,color)
            oled.pixel(x+a,y+b,color)
            oled.pixel(x-b,y+a,color)
            a=a+1
            if(di<0):
                di+=4*a+6
            else:
                di+=10+4*(a-b)
                b=b-1
            oled.pixel(x+a,y+b,color)
        #oled.show()
    ############################
    #16x16中文字符函数
    def ShowChar16x16(x,y,n):
        for i in range(2):
            for a in range(16):
                for b in range(8):
                    if(ByteOpera(b,chine[n*32+i*16+a])):
                        oled.pixel(x+a,y+i*8+b,1)
                    else:
                        oled.pixel(x+a,y+i*8+b,0)
        #oled.show()
    ######################
    #任意大小图片显示
    def ShowPic(x,y,w,h,color,pic):
        a=h/8
        if(h%8>0):
            a+=1
        for i in range(a):
            for n in range(w):
                for z in range(8):
                    if(ByteOpera(z,pic[a*w+n])):
                        oled.pixel(w,y+a*8+z,1)
                    else:
                        oled.pixel(w,y+a*8+z,0)





    #奇数时反相显示，偶数时正常显示
    def invert(n):
        oled.invert(n)
    #调整亮度。0最暗，255最亮
    def contrast(n):
        oled.contrast(n)
    #在(x, y)处显示字符串，注意text()函数内置的字体是8x8的，暂时不能替换
    def text(char,x,y):
        oled.text(char,x,y)
     #n=0，清空屏幕，n大于0，填充屏幕
    def fill(n):
        oled.fill(n)
          #######################
      #显示函数
    def show():
        oled.show()
        #关屏函数
    def poweroff():
        oled.poweroff()
    def poweron():
        oled.poweron()

if __name__ == "__main__":
    GUI.DrawBox(0,0,20,20,1,0)
    GUI.text('ok',0,25)
    GUI.show()
