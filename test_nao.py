import sys
from naoqi import ALProxy

IP = "192.168.0.102"
PORT = 9559

try:
    tts = ALProxy("ALTextToSpeech", IP, PORT)
except Exception,e:
    print "Could not create proxy to ALTextToSpeech"
    print "Error was: ",e
    sys.exit(1)


print sys.version_info


tts.setVolume(0.9)  ##Volume set to 90%
tts.setParameter("pitchShift", 1.2) #Applies a pitch shifting to the voice
tts.setParameter("doubleVoice", 0.0) #Deactivates double voice

tts.say("get me a coffee ")

