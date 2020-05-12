#unix mv command in python
#Author: Avinandan behera
#This applicaition is developed for educational purpose and can be reused by anyone in need.
'''
Usage:
python MoveCommand.py <source> <destination> <--copydirectory=True/False>


--copydirectory is an optional argument if user wanted to move directories recursively pass True, else by default it will
be FALSE.

'''

import os
import argparse
import shutil


def MoveCommand(args):
    #step1: validate input if source exist.
    status = False
    isDir = None
    if os.path.isdir(args.source):
        #source is a directory.
        isDir = True
    elif os.path.isfile(args.source):
        #else its a file
        isDir = False

    if isDir == None:
        print("Source file/directory does not exists")
        status = False
        return status

    dest = shutil.move(args.source,args.destination,copy_function=shutil.copytree)
    if len(dest):
        status = True
    return status


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="Enter source file/directory",type=str)
    parser.add_argument("destination", help="Enter destination file/directory", type=str)
    args = parser.parse_args()

    if os.path.isdir(args.source):
        print("Moving content of source directory:{0} to destination directory:{1}".format(args.source,args.destination))
    else:
        print("moving source filename:{0} to destination filename:{1}".format(args.source,args.destination))

    print(MoveCommand(args))
