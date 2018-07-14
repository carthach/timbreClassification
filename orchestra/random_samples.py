#!/usr/local/bin/python

#Handy template for doing file/folder processing
#Robbed from Sebastian at JCKU
import os
from myutils import *
from random import shuffle
import shutil

def parser():
    import argparse

    p = argparse.ArgumentParser()

    p.add_argument('inputPath', metavar='inputPath', nargs='+',
                   help='files to be processed')

    p.add_argument('outputPath', metavar='outputPath', nargs='+',
                   help='files to be processed')

    p.add_argument('noOfFiles', type=int, metavar='noOfFiles', nargs=1)

    p.add_argument('-v', dest='verbose', action='store_true',
                   help='be verbose')

        # parse arguments
    args = p.parse_args()
    # print arguments
    if args.verbose:
        print args
    # return args
    return args

def main():
    # only process .wav files
    # files = fnmatch.filter(files, '*.wav')
    # files.sort()

    args = parser()

    inputFilenames = getListOfFilesRecursive(args.inputPath[0], "*.mp3")
    outputDir = args.outputPath[0]
    noOfFilesToCopy = args.noOfFiles[0]

    # inputFilenames = random.shuffle(inputFilenames)

    shuffle(inputFilenames)

    print outputDir

    if not os.path.isdir(outputDir):
        print "HERE"
        try:            
            os.makedirs(outputDir)
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    for i in range(noOfFilesToCopy):                
        shutil.copy(inputFilenames[i], outputDir)
    
        
if __name__ == '__main__':
    main()