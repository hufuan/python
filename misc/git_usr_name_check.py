#!/usr/bin/env python

import os
import traceback

file = []
dir = []
dir_res = []
give_path = 'C:\workspace\Github'
expected_usr_name = 'test'
expected_email_addr = 'test@test.com'
def list_dir(start_dir):
    dir_res = os.listdir(start_dir)
    for path in dir_res:
        temp_path = start_dir + '\\' + path
        if os.path.isfile(temp_path):
            file.append(temp_path)
        if os.path.isdir(temp_path):
            dir.append(temp_path)
            #list_dir(temp_path)

def check_dir(root_dir):
    res = 0
    print(f'checking {root_dir} ...')
    os.chdir(root_dir)
    cmd = ' git config user.name'
    file = os.popen(cmd, 'r')
    cmd_res = file.read().strip()
    file.close()
    #print(f"comand result: {cmd_res}")
    if (cmd_res != expected_usr_name):
        print(f'ERROR: wrong user name: {cmd_res}')
        res = 1
    cmd = ' git config user.email'
    file = os.popen(cmd, 'r')
    cmd_res = file.read().strip()
    file.close()
    #print(f"comand result: {cmd_res}")
    if (cmd_res != expected_email_addr):
        print(f'!!! ERROR: wrong email address: {cmd_res} !!!')
        res = 1
    return res
if __name__ == '__main__':
    try:
        list_dir(give_path)
        #print("file：", file)
        #print("dir：", dir)
    except Exception as e:
        print(traceback.format_exc(), flush=True)
    res_list = []
    for item in dir:
        res = check_dir(item)
        res_list.append(res)
    #print(f'res_list = {res_list}')
    if any(res_list):
        print("Wrong user name or email address found!")
    else:
        print("Congras, all checks return OK!")