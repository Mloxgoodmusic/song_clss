from pytube import YouTube

link = "https://youtu.be/nRawLIsb3Y8"
yt = YouTube(link)
yt.streams.first().download()
