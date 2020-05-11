#unix copy command in python
#Author: Avinandan behera
#This applicaition is developed for educational purpose and can be reused by anyone in need.
import argparse
import os
import shutil
import errno
#fun: copycommand
#input: [1] Source file name with full path.
#input[2] Destination Filename with full path.
#if file path is not mentioned then the application will copy the destination file at the current working directory.
#return: Success/Failure
#Enhance copy utility to support copy all files inside a directory to others.
def copycommand(src,dst):
    #Validate the inputs
    print("copying source File:\"{0}\" content to destination File:\"{1}\" ".format(src,dst))
    #print("Current Working directory is:", os.getcwd())
    #absPath = os.getcwd()
    status = False
    if len(src) == 0 or len(dst) == 0:
        print("Source or destination path is empty")
        return status

    #check if user requested copy directory or copy file operation.
    if not args.copydirectory:
        #open source file and read contents.
        try:
            # Now since the sourcefile is not empty, lets check if the source file exist.
            fileStat = os.path.isfile(src)
            if not fileStat:
                status = fileStat
                print("Source File doesnt exist")
                return status

            with open(src) as f:
                data = f.read()
            with open(dst,"w") as df:
                df.write(data)

            status = True
        except FileNotFoundError:
            print("source file: \"{0}\" does not exist".format(src))
            status = False
        return status
    else:
        #when user pass command to perform copy directory operation.
        #step1: Check the source and destination path is a valid directory.
        srcdirstat = os.path.isdir(src)
        if not srcdirstat:
            status = False
            print("Source Directory doesnt exist.")
            return status
        '''step2: check if destination directory already exists. if not then create one as shutils.copy_tree() need
        the destination folder to be exist'''
        dstdirstat = os.path.isdir(dst)
        if dstdirstat:
            status = False
            print("destination dir:%s already exists" % dst)
            return status
        '''step3: Now perform the recursive copying of files and directories'''
        try:
            shutil.copytree(src, dst)
            status = True
        except OSError as err:
            if err.errno == errno.ENOTDIR:
                shutil.copy2(src, dst)
                status = True
            else:
                print("Error:%s" % err)
                status = False
        return status

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='please provide source and destination file name with space separated')
    parser.add_argument('sourceFile', help='SourceFileName', type=str)
    parser.add_argument('destFile', help='DestinationFileName', type=str)
    parser.add_argument('--copydirectory',help='copy all files inside the directory to destination directory',default=False,type=bool)
    args = parser.parse_args()
    print(copycommand(args.sourceFile, args.destFile))
    print(args.copydirectory)
