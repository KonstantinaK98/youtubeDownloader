from tkinter import *
import pytube
import pafy

root = Tk()
root.geometry('500x350')
root.title('My Youtube Downloader')
root.configure(background="#5f9ea0")
root.resizable(False,False)
root.iconbitmap('youtubeIcon.ico')

option = StringVar()
option.set("audio")

def audioDownload(url):
    try:
        video = pafy.new(url)
        audiostreams = video.audiostreams
        bestaudio = video.getbestaudio()
        bestaudio.download(filepath='C:\YtVideosAndAudio')
        infoLabel.config(text="Your audio file was successfully downloaded!")
    except:
        infoLabel.config(text="There was an error in the downloading proccess")

def videoDownload(url):
    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.filter(progressive=True, file_extension="mp4").first()
        video.download('C:\YtVideosAndAudio')
        infoLabel.config(text="Your video was successfully downloaded!")
    except:
        infoLabel.config(text="There was an error in the downloading proccess")    


def download(urlValue):  
    global infoLabel 
    if urlValue == "": 
        infoLabel.config(text="Please fill the url field first!")
    else:
        if option.get() == "audio":
            audioDownload(urlValue)
        elif option.get() == "mp4":
            videoDownload(urlValue)   
    urlEntry.delete(0,'end')             


titleLabel = Label(root, text="Youtube Downloader", font=("Arial" , 15),bg="#5f9ea0", pady=7)
titleLabel.pack()

urlLabel = Label(root, text="Enter the url of the video", font=("Arial" , 11),bg="#5f9ea0")
urlLabel.pack(padx=95,anchor=W)

urlEntry = Entry(root, width=50)
urlEntry.pack()

downloadBtn = Button(root, text="Download", width=20, height=2, command=lambda: download(urlEntry.get()))
downloadBtn.pack(padx=20,pady=10)

Radiobutton(root, variable=option, value="audio", text="audio", bg="#5f9ea0").pack(anchor=W, padx=90)
Radiobutton(root, variable=option, value="mp4", text="mp4", bg="#5f9ea0").pack(anchor=W, padx=90)

infoLabel = Label(root, text="Download youtube videos at mp4 format or audio ",font=("Arial" , 12), bg="#5f9ea0")
infoLabel.pack(pady=50)

root.mainloop()