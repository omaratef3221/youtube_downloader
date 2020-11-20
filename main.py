import pytube


url = input("Please enter the URL: ")
youtube = pytube.YouTube(str((url)))

for i in youtube.streams:
    if str(i.resolution) == "None":
        continue
    else:
        print(i.resolution)