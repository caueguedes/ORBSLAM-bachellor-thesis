import sys                
import argparse
import cv2
import os
import numpy as np
import re

def extractImages(pathIn, frameRate=1000, fps=0):
    if fps is None:
        fps = 1
        print ( 'Extracting at', frameRate, 'at', str(fps), 'frame per seconds.')

    frameRate = frameRate/fps

    
    match = re.match('(.*\/)(.*)', pathIn)
    folder = match.group(1)
    file_name = match.group(2)
    output = folder + file_name[:-4]

    print( "Folder", folder, "file:", file_name)
    
    if os.path.exists(output):
        if os.listdir(output) > 0:
            for file in os.listdir(output):
                os.remove(output + '/' + file)
                print('Removed all files from ' + output)
    else: 
        os.mkdir(output)
        print('Dir ' + output)
    
    time = 0
    vidcap = cv2.VideoCapture(pathIn)
    time += frameRate
    vidcap.set(cv2.cv.CV_CAP_PROP_POS_MSEC, time)
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    cv2.imwrite( output + r"/image%.0f.jpg" % (time/frameRate), image)
    print ( output + "Image written  image%.0f.jpg" % (time/frameRate))

    previous_image = image
    while success:
        time += frameRate
        vidcap.set(cv2.cv.CV_CAP_PROP_POS_MSEC, time) 
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
      
#        cv2.imwrite( output + r"/image%.0f.jpg" % (time/frameRate), image)
#        print ( output + " Image written  image%.0f.png" % (time/frameRate))
#        previous_image = image
        
        if not np.array_equal(previous_image, image):
            cv2.imwrite( output + r"/image%.0f.jpg" % (time/frameRate), image)
            print ( output + " Image written  image%.0f.jpg" % (time/frameRate))
            previous_image = image
        else:
            success = False
        
if __name__=="__main__":
    argument = argparse.ArgumentParser()
    argument.add_argument( 
            "--pathIn", 
            help="path to video",
            )
    argument.add_argument(
            "--frameRate", 
            help="video capture frameRate in miliseconds",
            type=float
            )
    argument.add_argument(
            "--fps", 
            help="number of frame per seconds",
            type=int
            )
    args = argument.parse_args()
    print(args)

    extractImages(args.pathIn, args.frameRate, args.fps)  


#def extractImages(pathIn, frameRate=100):
##def extractImages(pathIn, pathOut, frameRate=100):
#    time = 0
##    print(type(frameRate))
#    vidcap = cv2.VideoCapture(pathIn)
#    success = True
#    while success:
#      success = False
#      time += frameRate
#      print("timeeeee "+ str(time/1000))
#      vidcap.set(cv2.cv.CV_CAP_PROP_POS_MSEC, time) 
#      success,image = vidcap.read()
#      print ('Read a new frame: ', success)
#      if success:
#          cv2.imwrite( pathIn[:-4] + r"_frame%.0f.jpg" % (time/frameRate), image)
#          print ("Image written"+pathIn[:-4]+ "_frame%.0f.png" % (time/frameRate)) 
#  
#
#if __name__=="__main__":
#    argument = argparse.ArgumentParser()
#    argument.add_argument( 
#            "--pathIn", 
#            help="path to video",
#            )
#    argument.add_argument(
#            "--frameRate", 
#            help="video capture frameRate in miliseconds",
#            type=float,
#            )
#    args = argument.parse_args()
#    print(args)
#    
#    extractImages(args.pathIn, args.frameRate)  


#def extractImages(pathIn, pathOut, frameRate=100):
#    time = 0
#    vidcap = cv2.VideoCapture(pathIn)
#    success = True
#    while success:
#        time += frameRate
#        vidcap.set(cv2.cv.CV_CAP_PROP_POS_MSEC, time) 
#        success,image = vidcap.read()
#        print ('Read a new frame: ', success)
#        if success:
#            cv2.imwrite( pathOut + r"frames/frame%.0f.jpg" % (time/frameRate), image)
#            print ("Image written  frame%.0f.jpg" % (time/frameRate))
#            #success, image = vidcap.read()
#
#if __name__=="__main__":
#    argument = argparse.ArgumentParser()
#    argument.add_argument( 
#            "--pathIn", 
#            help="path to video",
#            )
#    argument.add_argument(
#            "--pathOut", 
#            help="path to images",
#            )
#    argument.add_argument(
#            "--frameRate", 
#            help="video capture frameRate in miliseconds",
#            type=float
#            )
#    args = argument.parse_args()
#    print(args)
#
#    pathOutput = args.pathOut + 'frames'
#	
#    if os.path.exists(pathOutput):
#        if os.listdir(pathOutput) > 0:
#             for file in os.listdir(pathOutput):
#                 os.remove(pathOutput + '/' + file)
#             print('Removed all files from ' + pathOutput)
#    else: 
#        os.mkdir(pathOutput)
#        print('Dir ' + pathOutput)
#
#    extractImages(args.pathIn, args.pathOut, args.frameRate)  
