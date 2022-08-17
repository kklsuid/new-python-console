# new-python-console

一个简单的 Python 控制台。

文档版本：v2.1.0

## 自定义

#### 在 main.py 中添加命令

首先添加字典对应：

```python
cmd_dict = { # 命令字典
    "exit":0,
    "help":1,
    "echo":2
}
```

然后添加执行函数：

```python
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
        ......
```

#### 添加语言文件

在 `lang` 文件夹下添加对应json。

```json
{
    "lang_help":"你好！",
    "lang_badcmd":"不是内部或外部命令，也不是可运行的程序或批处理文件。"
}
```

键值命名必须为 `lang_` 开头。

## 设置文件

设置文件为根目录下的`options.json`。

```json
{
    "version": "2.1.0",
    "con_name": "Python Console",
    "lang": "zh_cn",
    "debug": false
}
```

version：版本号

con_name：控制台名字

lang：语言（必须与lang文件夹下的json名字一样）

debug：调试模式
