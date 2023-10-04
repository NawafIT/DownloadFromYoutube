import tkinter
from tkinter import *
from PIL import Image, ImageTk
from pytube import YouTube
import tkinter.messagebox

root = Tk()
root.title("DownloadVid")
root.geometry("1000x400+500+200")
root.resizable(False, False)
root.iconbitmap("C:/Users/nawaf/Downloads/Ava.ico")


# ////---------------////


def downloadVid(url: str):
    if url == "":
        tkinter.messagebox.showwarning("Error", "You should enter the link")
    else:
        yt = YouTube(url)
        # Select the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        # Define the path where you want to save the video
        video_path = "C:/Users/nawaf/Downloads"

        # Download the video
        video_stream.download(output_path=video_path)
        tkinter.messagebox.showinfo("Video", "Download completed")


def downloadAudio(url: str):
    if url == "":
        tkinter.messagebox.showwarning("Error", "You should enter the link")
    else:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        if audio_stream is not None:
            # Define the path where you want to save the audio
            audio_path = "C:/Users/nawaf/Downloads"

            # Define the filename (you can customize this)
            filename = f"{yt.title}.mp3"

            # Download the audio
            audio_stream.download(output_path=audio_path, filename=filename)
            tkinter.messagebox.showinfo("Audio", "Download completed")


frame = Frame(root, width=1219, height=585, bg="#394867")
frame.place(x=0, y=0)
image = Image.open("C:/Users/nawaf/Downloads/nawaf.png")
# Resize the image using resize() method
resize_image = image.resize((250, 250))
img = ImageTk.PhotoImage(resize_image)
image = Label(frame, image=img)
image.place(x=5, y=15)

link = Label(frame,
             text="Use this Python script to download a video \nfrom YouTube with the highest quality available.\nSimply paste the video link, and the script will handle the rest!",
             font=("Overpass Mono", 13, "bold"), fg="white", bg="#212A3E")
link.place(x=280, y=15)

text = Label(frame, text="Put Your Link here:",
             font=("Overpass Mono", 13, "bold"), fg="white", bg="#212A3E")
text.place(x=520, y=150)

enterLink = Entry(frame, bg="#B0DAFF", fg="#3E497A", font=("Overpass Mono", 13, "bold"), justify=CENTER,
                  highlightbackground="#3E497A",
                  highlightcolor="#D4ADFC", highlightthickness=2, width=60)
enterLink.place(x=300, y=200)

button = Button(frame, width=50, bg="#B0DAFF", fg="#3E497A", text="Download Video", font=("Overpass Mono", 10, "bold"),
                activebackground="#5C469C", activeforeground="white"
                , command=lambda: downloadVid(enterLink.get()))
button.place(x=400, y=270)

button2 = Button(frame, width=50, bg="#B0DAFF", fg="#3E497A", text="Download Audio", font=("Overpass Mono", 10, "bold"),
                 activebackground="#5C469C", activeforeground="white"
                 , command=lambda: downloadAudio(enterLink.get()))
button2.place(x=400, y=320)

text = Label(frame, text="Nawaf Al-Jehani",
             font=("Overpass Mono", 13, "bold"), fg="white", bg="#212A3E")
text.place(x=50, y=300)

root.mainloop()
