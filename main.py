#!/usr/bin/env python
# -*- coding: utf-8 -*-

# new-python-console is licensed under the MIT License

# 导入模块

import os,sys,json
import color # 颜色输出库（仅Windows）

"""
New Python Console
by kkl.
"""

with open('options.json','r',encoding='utf-8') as f: # 导入设置
    options = json.load(f)
    lang_path = "lang\\" + options['lang'] + ".json"
    ver = options['version']
    con_name = options['con_name']
    debug = options['debug']

cmd_dict = { # 命令字典
    "exit":0,
    "help":1,
    "echo":2
}

with open(lang_path, 'r', encoding='utf-8') as f: # 导入语言文件
    texts = json.load(f)

def do_cmd(cmd_value,input_cmd):
    try:
        if cmd_value == 0:
            os._exit(0)
        elif cmd_value == 1:
            print(texts['lang_help'])
        elif cmd_value == 2:
            for i in input_cmd[1:]:
                print(i,end=' ')
            print()
    except:
        if debug: # 输出错误信息
            print(sys.exc_info())
        else:
            print("Error: %s" %sys.exc_info()[0])


def main():
    print(con_name+" [版本 %s]\nThis program is licensed under the MIT License\n" %ver)
    
    while True: # 主循环
        input_buf = input(os.getcwd()+">")
        try:
            input_cmd = input_buf.split() # 分割输入
        except:
            pass
        if input_buf != "": # 小写命令
            input_head = input_cmd[0].lower()
        else:
            input_head = ''
        
        i = 0
        for c in cmd_dict.keys(): # 检测对应命令
            if input_head == c:
                do_cmd(cmd_dict.get(c),input_cmd)
            else:
                i += 1
                # print(i," ",len(cmd_dict))
            if i == len(cmd_dict):
                if input_buf != '':
                    print(texts['lang_badcmd'])
                    print() # 输出一个空行


if __name__ == "__main__":
    main()