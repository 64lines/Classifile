#!/usr/bin/python
import sys
import shutil
from os import listdir, makedirs
from os.path import isfile, join, exists
from properties import *
from extension_convention import DICT_EXT_CONV

# Organize all files of a directory
class Classifile:

    # Get extension from a file_name
    def get_extension(self, file_name):
        extension = ""
        splited_file = file_name.split(DOT)
        count_elem = len(splited_file)

        if count_elem > 1:
            extension = splited_file[count_elem - 1]
    
        return extension.lower()

    # Organize files on folders with a directory
    def organize_files(self, directory):
        list_files = []
        list_extensions = []
        list_files_and_folders = listdir(directory)

        print MESSAGE_1
        # Select only files
        for file_name in list_files_and_folders :
            full_name_file = join(directory, file_name)
        
            # If is a file and isn't hidden
            if isfile(full_name_file) and file_name[0] != DOT:
                list_files.append(file_name)

        if not list_files:
            print MESSAGE_6
            return

        print MESSAGE_2 
        # Get extensions
        for file_name in list_files:
            extension = self.get_extension(file_name)
            extension = extension if extension else NO_EXT

            if extension not in list_extensions:
                list_extensions.append(extension)

        print MESSAGE_3
        # Create directories
        for ext_dir in list_extensions:
            try:
                ext_dir = DICT_EXT_CONV[ext_dir]
            except KeyError:
                ext_dir = ext_dir.upper()

            absol_name_dir = join(directory, ext_dir)
            if not exists(absol_name_dir):
                makedirs(absol_name_dir)

        print MESSAGE_4
        # Move files to folders with the files extension
        for file_name in list_files:
            ext = self.get_extension(file_name)
            ext = ext if ext else NO_EXT

            try:
                ext = DICT_EXT_CONV[ext]
            except KeyError:
                ext = ext.upper()

            absol_dest_dir = join(directory, ext)
            absol_file = join(directory, file_name)

            shutil.move(absol_file, absol_dest_dir)
        
        print MESSAGE_5
        

def main():
    directory = None

    try: directory = sys.argv[1]
    except: pass
    
    if not directory: 
        print MESSAGE_7
        return

    classifile = Classifile()
    classifile.organize_files(directory)

if __name__ == "__main__":
    main()


			
