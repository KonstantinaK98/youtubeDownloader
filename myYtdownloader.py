from tkinter import *

root = Tk()
root.geometry('500x350')
root.title('My Youtube Downloader')
root.configure(background="#5f9ea0")
root.resizable(False,False)

option = StringVar()
option.set("mp3")



def download(value):  
    global infoLabel 
    if value == "": 
        infoLabel.config(text="Please fill the url field first!")
    else:
        if option.get() == "mp3":
            print("Einai mp3 kai exei to value: ")
            print(value)
            infoLabel.config(text="The url (mp3) successfully downloaded!")
        elif option.get() == "mp4":
            print("Einai mp4 kai exei to value: ")
            print(value)
            infoLabel.config(text="The url (mp4) successfully downloaded!")   
    urlEntry.delete(0,'end')             


titleLabel = Label(root, text="Youtube Downloader", font=("Arial" , 14),bg="#5f9ea0", pady=7)
titleLabel.pack()

urlLabel = Label(root, text="Enter the url of the video", font=("Arial" , 11),bg="#5f9ea0")
urlLabel.pack(padx=95, pady=5 ,anchor=W)

urlEntry = Entry(root, width=50)
urlEntry.pack()

downloadBtn = Button(root, text="Download", width=20, height=2, command=lambda: download(urlEntry.get()))
downloadBtn.pack(padx=20,pady=10)

Radiobutton(root, variable=option, value="mp3", text="mp3", bg="#5f9ea0").pack(anchor=W, padx=90)
Radiobutton(root, variable=option, value="mp4", text="mp4", bg="#5f9ea0").pack(anchor=W, padx=90)

infoLabel = Label(root, text="Download youtube videos at mp4 or mp3 format",font=("Arial" , 10), bg="#5f9ea0")
infoLabel.pack(pady=50)

root.mainloop()