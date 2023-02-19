from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self,event):
        for filename in os.listdir(folder_to_track):
            print(filename)
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

folder_to_track = "/Users/jeffr/Desktop/Sort"
folder_destination = "/Users/jeffr/Desktop/destination"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()