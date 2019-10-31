import sys                
import argparse
import cv2
import os


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


def extractImages(pathIn, pathOut, frameRate=100):
    time = 0
    vidcap = cv2.VideoCapture(pathIn)
    success = True
    while success:
        time += frameRate
        vidcap.set(cv2.cv.CV_CAP_PROP_POS_MSEC, time) 
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        if success:
            cv2.imwrite( pathOut + r"frames/frame%.0f.jpg" % (time/frameRate), image)
            print ("Image written  frame%.0f.jpg" % (time/frameRate))
            #success, image = vidcap.read()

if __name__=="__main__":
    argument = argparse.ArgumentParser()
    argument.add_argument( 
            "--pathIn", 
            help="path to video",
            )
    argument.add_argument(
            "--pathOut", 
            help="path to images",
            )
    argument.add_argument(
            "--frameRate", 
            help="video capture frameRate in miliseconds",
            type=float
            )
    args = argument.parse_args()
    print(args)

    pathOutput = args.pathOut + 'frames'
	
    if os.path.exists(pathOutput):
        if os.listdir(pathOutput) > 0:
             for file in os.listdir(pathOutput):
                 os.remove(pathOutput + '/' + file)
             print('Removed all files from ' + pathOutput)
    else: 
        os.mkdir(pathOutput)
        print('Dir ' + pathOutput)

    extractImages(args.pathIn, args.pathOut, args.frameRate)  
