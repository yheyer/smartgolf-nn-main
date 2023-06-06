import shutil
import os
import re

source_folder = "golfdata"
destination_folder = "golfdatanew"

pattern = re.compile(r'[0-2]_S(1[6-9]|2[0-7])_\d+\.csv')

# Iterate through all files in the source folder
for filename in os.listdir(source_folder):
    if pattern.match(filename):
        # Copy the file from source folder to destination folder
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)
        shutil.copy(source_file, destination_file)
        print(filename)