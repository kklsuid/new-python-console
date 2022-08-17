#!/usr/bin/env python
# -*- coding: utf-8 -*-

# new-python-console is licensed under the MIT License

# 导入模块

import os,sys,json
import color

"""
New Python Console
by kkl.
"""

ver = "2.0.1"

cmd_dict = {
    "exit":0,
    "help":1
}

with open('data.json', 'r') as f:
    data = json.load(f)

def do_cmd(cmd_value):
    try:
        if cmd_value == 0:
            os._exit(0)
        elif cmd_value == 1:
            print(data['zh_help'])
    except:
        print(sys.exc_info()[0])


def main():
    print("Python Console [版本 %s]\nThis program is licensed under the MIT License\n" %ver)
    
    while True:
        input_buf = input(os.getcwd()+">")
        try:
            input_cmd = input_buf.split()
        except:
            pass
        if input_buf != "":
            input_head = input_cmd[0].lower()
        
        i = 0
        for c in cmd_dict.keys():
            if input_head == c:
                do_cmd(cmd_dict.get(c))
            else:
                i += 1
                # print(i," ",len(cmd_dict))
            if i == len(cmd_dict):
                print("Bad Command.")
            
        print()

if __name__ == "__main__":
    main()