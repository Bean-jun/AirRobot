"""
驱动文字显示

接线注意点：
    SDA-->D2
    SCL-->D1
"""

# 字体
fonts= {
    0xe585b3:
    [0x10, 0x08, 0x08, 0x00, 0x3F, 0x01, 0x01, 0x01, 0xFF, 0x01, 0x02, 0x02, 0x04, 0x08, 0x30, 0xC0,
     0x10, 0x10, 0x20, 0x00, 0xF8, 0x00, 0x00, 0x00, 0xFE, 0x00, 0x80, 0x80, 0x40, 0x20, 0x18, 0x06],  # 关",0
    0xe788b1:
    [0x00, 0x01, 0x7E, 0x22, 0x11, 0x7F, 0x42, 0x82, 0x7F, 0x04, 0x07, 0x0A, 0x11, 0x20, 0x43, 0x1C,
        0x08, 0xFC, 0x10, 0x10, 0x20, 0xFE, 0x02, 0x04, 0xF8, 0x00, 0xF0, 0x10, 0x20, 0xC0, 0x30, 0x0E],  # 爱",1
    0xe58d95:
    [0x10, 0x08, 0x04, 0x3F, 0x21, 0x21, 0x3F, 0x21, 0x21, 0x3F, 0x01, 0x01, 0xFF, 0x01, 0x01, 0x01,
        0x10, 0x20, 0x40, 0xF8, 0x08, 0x08, 0xF8, 0x08, 0x08, 0xF8, 0x00, 0x00, 0xFE, 0x00, 0x00, 0x00],  # 单",2
    0xe8baab:
    [0x02, 0x04, 0x1F, 0x10, 0x1F, 0x10, 0x1F, 0x10, 0x10, 0x7F, 0x00, 0x00, 0x03, 0x1C, 0xE0, 0x00,
        0x00, 0x00, 0xF0, 0x10, 0xF0, 0x10, 0xF2, 0x14, 0x18, 0xF0, 0x50, 0x90, 0x10, 0x10, 0x50, 0x20],  # 身",3
    0xe78b97:
    [0x00, 0x44, 0x29, 0x11, 0x2A, 0x4C, 0x89, 0x09, 0x19, 0x29, 0x49, 0x89, 0x08, 0x08, 0x50, 0x20,
     0x80, 0x80, 0x00, 0xFC, 0x04, 0x04, 0xE4, 0x24, 0x24, 0x24, 0xE4, 0x24, 0x04, 0x04, 0x28, 0x10],  # 狗",4
    0xe68890:
    [0x00, 0x00, 0x00, 0x3F, 0x20, 0x20, 0x20, 0x3E, 0x22, 0x22, 0x22, 0x22, 0x2A, 0x44, 0x40, 0x81,
     0x50, 0x48, 0x40, 0xFE, 0x40, 0x40, 0x44, 0x44, 0x44, 0x28, 0x28, 0x12, 0x32, 0x4A, 0x86, 0x02],  # 成",5
    0xe995bf:
    [0x08, 0x08, 0x08, 0x08, 0x08, 0x09, 0x08, 0xFF, 0x0A, 0x09, 0x08, 0x08, 0x09, 0x0A, 0x0C, 0x08,
        0x00, 0x10, 0x20, 0x40, 0x80, 0x00, 0x00, 0xFE, 0x00, 0x00, 0x80, 0x40, 0x20, 0x18, 0x06, 0x00],  # 长",6
    0xe58d8f:
    [0x20, 0x20, 0x20, 0x20, 0xFB, 0x20, 0x20, 0x22, 0x22, 0x24, 0x28, 0x20, 0x21, 0x21, 0x22, 0x24,
     0x80, 0x80, 0x80, 0x80, 0xF0, 0x90, 0x90, 0x98, 0x94, 0x92, 0x92, 0x90, 0x10, 0x10, 0x50, 0x20],  # 协",7
    0xe4bc9a:
    [0x01, 0x01, 0x02, 0x04, 0x08, 0x30, 0xCF, 0x00, 0x00, 0x7F, 0x02, 0x04, 0x08, 0x10, 0x3F, 0x10,
     0x00, 0x00, 0x80, 0x40, 0x20, 0x18, 0xE6, 0x00, 0x00, 0xFC, 0x00, 0x00, 0x20, 0x10, 0xF8, 0x08]  # 会",8
}

def _chinese(ch_str, x_axis, y_axis, OLED): 
   offset_ = 0 
   y_axis = y_axis*8  # 中文高度一行占8个  
   x_axis = (x_axis*16)  # 中文宽度占16个 
   for k in ch_str: 
       code = 0x00  # 将中文转成16进制编码 
       data_code = k.encode("utf-8") 
       code |= data_code[0] << 16 
       code |= data_code[1] << 8
       code |= data_code[2]
       byte_data = fonts[code]
       for y in range(0, 16):
           a_ = bin(byte_data[y]).replace('0b', '')
           while len(a_) < 8:
               a_ = '0'+a_
           b_ = bin(byte_data[y+16]).replace('0b', '')
           while len(b_) < 8:
               b_ = '0'+b_
           for x in range(0, 8):
               OLED.pixel(x_axis+offset_+x, y+y_axis, int(a_[x]))   
               OLED.pixel(x_axis+offset_+x+8, y+y_axis, int(b_[x]))   
       offset_ += 16
       


def show(context):
    from machine import Pin, I2C
    from ssd1306 import SSD1306_I2C 
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    OLED= SSD1306_I2C(128, 64, i2c)
    _chinese('关爱单身狗成长协会',0,0, OLED) 
    OLED.show()