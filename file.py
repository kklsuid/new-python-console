import os,shutil,runex

def cd(target):
    os.chdir(target)

def dir():
    return '\n'.join(os.listdir())

def mkdir(dir_name):
    os.mkdir(dir_name)

def rm(dir_name):
    if os.path.isfile(dir_name):
        os.remove(dir_name)
    elif os.path.isdir(dir_name):
        shutil.rmtree(dir_name)

def cat(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        str = f.read()
        return str.rstrip()

def copy(file_path,to_path):
    shutil.copy(file_path,to_path)

def move(file_path,to_path):
    shutil.move(file_path,to_path)

def rename(file_path,to_path):
    os.rename(file_path,to_path)

def tree():
    runex.run_cmd('tree')