import os
import time

source_folder = "/Users/jeffr/Desktop/Sort"
destination_folder = "/Users/jeffr/Desktop/destination"

with os.scandir(source_folder) as entries:
    for entry in entries:
        name = entry.name
        print(name)
        if name.endswith('.txt'):
            name = name[:len(name)-4]+'2.txt'
            os.rename(entry,source_folder+'/'+name)
            time.sleep(1)
            print(entry.name)
            


print()
