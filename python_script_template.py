
import Tkinter
import os
import shutil
import subprocess

## The template to rsync to remote server.
rsync_template = 'rsync -avhr --chmod=Du=rwx,go=rx,Fu=rwx,og=rx <src_dir> <dest_host>:<dest_dir>'

def execute(cmd):
    """
    :param cmd: The command line
    :return: Nothing
    Execute command line and output result to console.
    """
    p = subprocess.Popen(cmd, shell=True)
    output, err = p.communicate()
    print(output)


## Tkinter GUI
top = Tkinter.Tk()

def foo():
	pass

def exit_application():
    top.quit()

buttons = [
    { "text": "foo", "command": foo },
    { "text": "Exit", "command": exit_application },
    { }, # Seperator
]

for bInfo in buttons:
    if bInfo.get("text"):
        btn = Tkinter.Button(top, text = bInfo["text"], command = bInfo["command"])
        btn.pack()
    else:
        sep = Tkinter.Label(top, text="")
        sep.pack()

top.mainloop()