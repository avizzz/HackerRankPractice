#unix cat command in python
#Author: Avinandan behera
#This applicaition is developed for educational purpose and can be reused by anyone in need.
'''
Usage:
python CatCommand.py <fileName> <--n=True>

--n is an optional argument if user wanted to pring the file content with line number associated for everyline.

'''
import argparse
import os
def catCommand(args):
    #step1: check if file exist.
    status = False
    if not os.path.isfile(args.filename):
        print("File:%s does not exist" % args.filename)
        status = False
        return status
    #step2:open the file and read the contents to stdout.
    try:
        filehandle = open(args.filename,'r')
        print("Reading file:%s contents" % args.filename)
        print("########################################################################")
        if not args.n:
            for line in filehandle:
                print(line)
        else:
            count = 1
            for line in filehandle:
                #if len(line) > 0 or line != '\n':
                header = str(count) + '\t'
                line = header + line
                count += 1
                print(line)

        print("########################################################################")
    finally:
        filehandle.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename",help="Enter filename",type=str)
    parser.add_argument("--n",help="Number all output lines",default=False,type=bool)
    args = parser.parse_args()
    print(args.filename)
    catCommand(args)
