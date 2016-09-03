import sys
import os
from os.path import isfile, join

def main(args):
    
    # Folder path sent as a part of the argument.
    folder_path = args[0]

    all_files_folders = os.listdir(folder_path)

    # Fetching all files using list comprehension
    only_files = [f for f in all_files_folders if isfile(join(folder_path, f))]
    print "Total number of files in " + folder_path + " - " + str(len(only_files))

    # Only files can be fetched in the following manner without using list comprehension
    only_files = []
    for each_file in all_files_folders:
	if isfile(join(folder_path, each_file)):
    	    only_files.append(each_file)


if __name__ == "__main__":
    main(sys.argv[1:])
