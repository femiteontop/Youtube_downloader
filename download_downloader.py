# This few lines of code help to download Youtube video, there will always be improvement.

from pytube import YouTube

youtube_link = input("Paste Youtube link here, then press enter: \n")


def youtube_download():

    url = YouTube(youtube_link)
    video = url.streams.first()
    result = video.download()

    return result


youtube_download()
