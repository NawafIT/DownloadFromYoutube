import ttkbootstrap as tkk
from tkinter import *
from PIL import Image, ImageTk
from pytube import YouTube
import tkinter.messagebox

root = tkk.Window()
root.title("DownloadVid")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 1000
window_height = 400
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position - 60}")

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


frame = tkk.Frame(root, width=1219, height=585, style="dark")
frame.place(x=0, y=0)
image = Image.open("C:/Users/nawaf/Downloads/nawaf.png")
# Resize the image using resize() method
resize_image = image.resize((250, 250))
img = ImageTk.PhotoImage(resize_image)
image = Label(frame, image=img)
image.place(x=5, y=15)


link = tkk.Label(frame,
                 text="\t     Use this Python script to download a video \n\t   from YouTube with the highest quality available.\n  Simply paste the video link, and the script will handle the rest!",
                 font=("Overpass Mono", 12, "bold"), bootstyle="inverse")
link.place(x=280, y=15)

text = tkk.Label(frame, text="Put Your Link here:",
                 font=("Overpass Mono", 13, "bold"), bootstyle="inverse-primary")
text.place(x=520, y=150)

enterLink = tkk.Entry(frame, font=("Overpass Mono", 13, "bold"), justify=CENTER,
                      width=60, bootstyle="info")
enterLink.place(x=300, y=200)

button = Button(frame, width=50, text="Download Video", font=("Overpass Mono", 11, "bold"),
                command=lambda: downloadVid(enterLink.get()))

button.place(x=385, y=270)

button2 = Button(frame, width=50, text="Download Audio", font=("Overpass Mono", 11, "bold"),
                 command=lambda: downloadAudio(enterLink.get()))
button2.place(x=385, y=320)

text2 = tkk.Label(frame, text="Nawaf Al-Jehani",
                  font=("Overpass Mono", 13, "bold"), bootstyle="inverse-danger")
text2.place(x=50, y=300)

root.mainloop()
