from pytube import YouTube
#where to save
SAVE_PATH = "E:/"
#your youtube download link
link = input("enter the youtube link here:")
try:
    #object creation
    yt = YouTube(link)
    #file location
    SAVE_PATH = input('''enter where to you want save your file:''')
    #file name
    fname = input('''video will be saved as
file name (with extention .mp4):''')
except:
    print("connection error")
try:
    #now download the link
    #filter to filter mp4 file only
    yt.streams.filter(progressive= True, file_extension = "mp4").first().download(output_path = SAVE_PATH, filename=fname)
except:
    print("error")
print("task Completed")