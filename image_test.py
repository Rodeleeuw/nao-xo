'''
NaoXO, v1.0
As of 18.3.2014.

@author: FP
'''

## import ALProxy to connect to Naoqi on the robot
from naoqi import ALProxy

## import numpy for matrix operations and OpenCV
import numpy as np

## import OpenCV for visualization

## import definitions for xo class
from naoxo_definitions import *

## import image processing module

## import NAO vision definitions for image grabbing
from vision_definitions import kVGA, kBGRColorSpace

## import time module
import time

## import strategy modules
## TODO: rewrite strategy modules
from pobjeda import pobjeda
from krizic_kruzic_strategija import strategija_x
from krizic_kruzic_strategija import strategija_o

IP = "192.168.0.102"
PORT = 9559

import pdb; pdb.set_trace()
motion = ALProxy("ALMotion", IP, PORT)
memory = ALProxy("ALMemory", IP, PORT)
behavior = ALProxy("ALBehaviorManager", IP, PORT)
tts = ALProxy("ALTextToSpeech", IP, PORT)
videoProxy = ALProxy("ALVideoDevice", IP, PORT)
awareness = ALProxy("ALBasicAwareness", IP, PORT)
posture = ALProxy("ALRobotPosture", IP, PORT)

## set video parameters
## select bottom camera
videoProxy.setParam(18,1)
## subscribe to ALVideoDevice
subscriberID = "video"
video = videoProxy.subscribe("video", kVGA, kBGRColorSpace, 30)
## create image header
alimg = videoProxy.getImageRemote(video)
## alimg[0] -> witdth, alimg[1] -> height
## alimg[6] -> pixel array
size = (alimg[0], alimg[1])
#imgheader = cv2.cv.CreateImageHeader((alimg[0], alimg[1]), cv2.cv.IPL_DEPTH_8U, 3)
## create image processing object
imgproc = img.ImgProcessingXO(size)
print("[INFO ] Image processing initialized")
## state of the game
state = [0]*9
states = [[0]*9, [0]*9, [0]*9]
board = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
mode = 'x'
