import pytube as t
import tkinter as tk
import os

# variables:
url = None
path = None

# the root of window:
root = tk.Tk()
root.geometry('800x600')

# window frame declaration:
frame = tk.Frame(root)

# widget, label, and other stuff:
l1 = tk.Label(text="Y O U T U B E  T O  M P 4!", font=('roboto', 25))
l1.pack()

# functions:

def getUrl(event):
    global url
    url = tb.get('1.0', 'end-1c')
    print(url)
    print(type(url))

def getPath(event):
    global path
    path = tb1.get('1.0', 'end-1c')

def download(_url, _path):
    yt = t.YouTube(str(_url))
    stream = yt.streams.get_highest_resolution()
    if _path == '':
        _path = os.getcwd()
    else:
        pass
    stream.download(_path)

def buttonFunction():
    getUrl(0)
    getPath(0)
    download(url, path)

tb = tk.Text(root, height=1, width=50, font=('roboto', 11))
tb.pack()
tb.bind("<Return>", getUrl)

tb1 = tk.Text(root, height=1, width=50, font=('roboto', 11))
tb1.pack()
tb1.bind("<Return>", getPath)

b1 = tk.Button(text="Download", command=buttonFunction)
b1.pack()

# main window loop
frame.mainloop()
