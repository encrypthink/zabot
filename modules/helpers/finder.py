import inspect
import os


class Finder:

    def __init__(self, path):
        self.path = path

    def get_directory_list(self):
        files = {}
        list_dir = os.listdir(self.path)
        list_dir.remove("__pycache__")
        
        i = 0
        for file in list_dir:
            files[i] = {
                "filename": self.get_only_name(file),
                "fullfilename": file,
                "fullpath": self.path + file
            }
            i = i+1
        
        return files

    def get_only_name(self, file):
        return file.split(".")[0]

       
