import sys
import os
from os.path import isfile, join

def main(args):
    
    # Folder path sent as a part of the argument.
    folder_path = args[0]
    

    all_files_folders = os.listdir(folder_path)
    only_files = [f for f in all_files_folders if isfile(join(folder_path, f))]
    

if __name__ == "__main__":
    main(sys.argv[1:])
