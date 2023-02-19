import shutil
import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler


# source and destination filder paths
source_folder = "/Users/jeffr/OneDrive/Downloads"
text_folder = "/Users/jeffr/OneDrive/Documents/txt"
pdf_folder = "/Users/jeffr/OneDrive/Documents/txt/pdf"
image_folder = "/Users/jeffr/Pictures"
uni_folder = "/Users/jeffr/OneDrive/Documents/Uni\ 2023"
word_folder = "/Users/jeffr/OneDrive/Documents/txt/WordDocs"
video_folder = "/Users/jeffr/Videos"
installers_folder = "/Users/jeffr/OneDrive/Documents/Other/installation"
other_folder = "/Users/jeffr/OneDrive/Documents/Other"

def makeUnique(name):
    name = source_folder+'/'+name[:len(name)-4]+'dup.txt'
    return name

def move_to(dest, entry, name):
    file_exists = os.path.exists(f'{dest}/{name}')
    if file_exists:
        unique_name = makeUnique(name)
        os.rename(entry,unique_name)
    else:
        shutil.move(entry,dest)

# sifts through all files and sorts into folders
def sort():
    with os.scandir(source_folder) as entries:
        for entry in entries:
            name = entry.name
            print(name)
            if name.endswith('.txt'):
                dest = text_folder
            elif name.endswith('.pdf'):
                if '722' or '770' or '734' or '700A' in name:
                    dest = uni_folder
                else:
                    dest = pdf_folder
            elif name.endswith('.jpg') or name.endswith('.png') or name.endswith('.PNG') or name.endswith('.JPEG'):
                dest = image_folder
            elif name.endswith('.doc') or name.endswith('.docx'):
                dest = word_folder
            elif name.endswith('.exe'):
                dest = installers_folder            
            elif name.endswith('.mp4'):
                dest = video_folder
            else:
                dest = other_folder
            move_to(dest,entry,name)             


# responds to events by sorting all files in source folder
class Mover(FileSystemEventHandler):
    def on_modified(self, event):
        sort()
    
    def on_created(self, event):
        sort()        



# sets up folder modification listener
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_folder
    event_handler = Mover()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()