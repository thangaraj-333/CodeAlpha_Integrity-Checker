import sys
import hashlib
import PySimpleGUI as pygui
import os
buffer_size = 65536
md5 = hashlib.md5()
sha256 = hashlib.sha256()
sha512 = hashlib.sha512()
def output_func(calculated_hash, given_hash):
    if calculated_hash == given_hash:
        pygui.popup('hash of the file is: \n'+md5.hexdigest()+"\n the given hash is: \n"+hash_value+"\n The hash matches and the file is intact!")
    if calculated_hash != given_hash:
        pygui.popup('hash of the file is: \n'+md5.hexdigest()+"\n the given hash is: \n"+hash_value+"\n The hash does not match so, the file is either corrupt or the hash is wrong!")
    return None
def func_md5(file, hash_value):
    with open(file, 'rb') as f:
        while True:
            data = f.read(buffer_size)
            if not data:
                break
            md5.update(data)
        output_func(md5.hexdigest(),hash_value)
    return None
def func_sha_256(file, hash_value):
    with open(file, 'rb') as f:
        while True:
            data = f.read(buffer_size)
            if not data:
                break
            sha256.update(data)
        output_func(sha256.hexdigest(),hash_value)
    return None
def func_sha_512(file, hash_value):
    with open(file, 'rb') as f:
        while True:
            data = f.read(buffer_size)
            if not data:
                break
            sha512.update(data)
        output_func(sha512.hexdigest(),hash_value)
    return None
def reinitialize():
    path = os.path.abspath(__file__)
    os.system("python {}".format(path))
pygui.theme('reddit')
layout = [[pygui.T("Welcome to Integrity Checker")], [pygui.Text("Choose the file: "), pygui.Input(), pygui.FileBrowse(key="-path-")],[pygui.Text("Enter the hash: "), pygui.Input(key="-hash-")],
          [pygui.Text("Choose the hashing algorithm: "),pygui.T("   "), pygui.Radio('MD5', "RADIO1", default=False, key="-md5-"),pygui.T("         "), pygui.Radio('sha-256', "RADIO1", default=True, key="-sha256-"),pygui.T("         "), pygui.Radio('sha-512', "RADIO1", default=True, key="-sha512-")],
          [pygui.Button("Submit")]]
window = pygui.Window("Integrity Checker", layout)
event, values = window.read()
if event == pygui.WIN_CLOSED or event=="Exit": print("exiting")
elif event == "Submit" and values["-md5-"] == True and len(values["-hash-"]) != 0:
    file_path=values["-path-"]
    hash_value=values["-hash-"]
    func_md5(file_path, hash_value)
    window.close()
    reinitialize()
elif event == "Submit" and values["-sha256-"] == True and len(values["-hash-"]) != 0:
    file_path=values["-path-"]
    hash_value=values["-hash-"]
    func_sha_256(file_path, hash_value)
    window.close()
    reinitialize()
elif event == "Submit" and values["-sha512-"] == True and len(values["-hash-"]) != 0:
    file_path=values["-path-"]
    hash_value=values["-hash-"]
    func_sha_512(file_path, hash_value)
    window.close()
    reinitialize()
        