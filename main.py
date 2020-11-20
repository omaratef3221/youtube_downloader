import pytube


url = input("Please enter the URL: ")
youtube = pytube.YouTube(str((url)))

for i in youtube.streams:
    if str(i.resolution) == "None":
        continue
    else:
        print(i.resolution)
quality = input("\nPlease choose a quality: ")
video = youtube.streams.get_by_resolution(str(quality))
video.download()