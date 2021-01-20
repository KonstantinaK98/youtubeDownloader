from tkinter import *

root = Tk()
root.geometry('500x350')
root.title('My Youtube Downloader')

titleLabel = Label(root, text="Youtube Downloader", font=("Arial" , 14), pady=10)
titleLabel.pack()

urlEntry = Entry(root, width=50)
urlEntry.pack()

downloadBtn = Button(root, text="Download", width=20, height=2)
downloadBtn.pack()

root.mainloop()