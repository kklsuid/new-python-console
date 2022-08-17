#-*- coding:utf-8 -*-#
 
#filename: prt_cmd_color.py
 
import ctypes,sys
  
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12
  
#字体颜色定义 text colors
FOREGROUND_BLUE = 0x09 # blue.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_RED = 0x0c # red.
FOREGROUND_YELLOW = 0x0e # yellow.
  
# 背景颜色定义 background colors
BACKGROUND_YELLOW = 0xe0 # yellow.
  
# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool
  
#reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

def printColor(mess,forecolor,backcolor=False):
    if forecolor == 'green':
        if backcolor == False:
            set_cmd_text_color(FOREGROUND_GREEN)
        else:
            set_cmd_text_color(BACKGROUND_YELLOW | FOREGROUND_GREEN)
    elif forecolor == 'red':
        if backcolor == False:
            set_cmd_text_color(FOREGROUND_RED)
        else:
            set_cmd_text_color(BACKGROUND_YELLOW | FOREGROUND_RED)
    elif forecolor == 'yellow':
            set_cmd_text_color(FOREGROUND_YELLOW)
    else:
        resetColor()
    sys.stdout.write(mess + '\n')
    resetColor()

if __name__ == '__main__':
    printColor('printGreen:Green Color Text','green')
    printColor('printRed:Red Color Text','red')
    printColor('printYellow:Yellow Color Text','yellow')