import PySimpleGUI as pygui
import os
import subprocess  # Import the subprocess module

pygui.theme('reddit')
layout = [[pygui.T("Welcome to Integrity Checker")],  [pygui.Button("Create hash of a file")],[pygui.Button("Check the file integrity(hash required)")]]
window = pygui.Window("Integrity Checker", layout)
event, values = window.read()
if event == "Create hash of a file":
    path = os.path.join(os.path.dirname(__file__), "hash_create.py")
    subprocess.run(["python", path], check=True)
elif event == "Check the file integrity(hash required)":
    path = os.path.join(os.path.dirname(__file__), "hash_compare.py")
    subprocess.run(["python", path], check=True)

window.close()
