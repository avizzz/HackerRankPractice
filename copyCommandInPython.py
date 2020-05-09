#implement your own copy command using python.
#unix copy command in python
#Author: Avinandan behera
#This applicaition is developed for educational purpose and can be reused by anyone in need.


#fun: copycommand
#input: [1] Source file name with full path.
#input[2] Destination Filename with full path.
#if file path is not mentioned then the application will copy the destination file at the current working directory.
#return: Success/Failure

import argparse
import os
def copycommand(src,dst):
    #Validate the inputs
    print("copying source File:\"{0}\" content to destination File:\"{1}\" ".format(src,dst))
    #print("Current Working directory is:", os.getcwd())
    #absPath = os.getcwd()
    status = False
    if len(src) == 0 or len(dst) == 0:
        return status

    #open source file and read contents.
    try:
        with open(src) as f:
            data = f.read()

        with open(dst,"w") as df:
            df.write(data)
        status = True
    except FileNotFoundError:
        print("source file: \"{0}\" does not exist".format(src))
        status = False

    return status

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='please provide source and destination file name with space separated')
    parser.add_argument('sourceFile', help='SourceFileName', type=str)
    parser.add_argument('destFile', help='DestinationFileName', type=str)
    args = parser.parse_args()
    print(copycommand(args.sourceFile, args.destFile))
