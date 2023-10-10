import sys
import pyperclip
import hashlib
import PySimpleGUI as pygui
import os
buffer_size = 65536
md5 = hashlib.md5()
sha256 = hashlib.sha256()
sha512 = hashlib.sha512()
def func_md5(file):
    with open(file, 'rb') as f:
        while True:
            data = f.read(buffer_size)
            if not data:
                break
            md5.update(data)
        pygui.popup('hash of the file is: \n'+md5.hexdigest()+"\n Compare this hash with the given one!"+"\n the hash is copied to your clip board,\n paste it anywhere using Ctrl+V or right click -> paste")
        pyperclip.copy(md5.hexdigest())
    return None
def func_sha_256(file):
    with open(file, 'rb') as f:
        while True:
            data = f.read(buffer_size)
            if not data:
                break
            sha256.update(data)
        pygui.popup('hash of the file is: \n'+sha256.hexdigest()+"\n Compare this hash with the given one!"+"\n the hash is copied to your clip board,\n paste it anywhere using Ctrl+V or right click -> paste")
        pyperclip.copy(sha256.hexdigest())
    return None
def func_sha_512(file):
    with open(file, 'rb') as f:
        while True:
            data = f.read(buffer_size)
            if not data:
                break
            sha512.update(data)
        pyperclip.copy(sha512.hexdigest())
        pygui.popup('hash of the file is: \n'+sha512.hexdigest()+"\n Compare this hash with the given one!"+"\n the hash is copied to your clip board,\n paste it anywhere using Ctrl+V or right click -> paste")
    return None
def reinitialize():
    path = os.path.abspath(__file__)
    os.system("python {}".format(path))
pygui.theme('reddit')
layout = [[pygui.T("Welcome to Integrity Checker")], [pygui.Text("Choose a file: "), pygui.Input(), pygui.FileBrowse(key="-IN-")],
          [pygui.Text("Choose the hashing algorithm: "),pygui.T("   "), pygui.Radio('MD5', "RADIO1", default=False, key="-md5-"),pygui.T("         "), pygui.Radio('sha-256', "RADIO1", default=True, key="-sha256-"),pygui.T("         "), pygui.Radio('sha-512', "RADIO1", default=True, key="-sha512-")],
          [pygui.Button("Submit")]]
window = pygui.Window("Integrity Checker", layout)
event, values = window.read()
if event == pygui.WIN_CLOSED or event=="Exit": print("exiting")
elif event == "Submit" and values["-md5-"] == True:
    file_path=values["-IN-"]
    func_md5(file_path)
    window.close()
    reinitialize()
elif event == "Submit" and values["-sha256-"] == True:
    file_path=values["-IN-"]
    func_sha_256(file_path)
    window.close()
    reinitialize()
elif event == "Submit" and values["-sha512-"] == True:
    file_path=values["-IN-"]
    func_sha_512(file_path)
    window.close()
    reinitialize()
        