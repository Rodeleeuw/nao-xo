#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Playing tic-tac-toe with NAO, v1.0
As of 18.3.2014.

@author: FP
'''

## import nao_xo class
from nao_xo import NaoXO
## import option parser
from optparse import OptionParser
## import sys
import sys

import time

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('logs/main_xo.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

#stream_handler = logging.StreamHandler()
#stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
#logger.addHandler(stream_handler)

# logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

if __name__ == '__main__':

    ## parse input arguments
    parser = OptionParser()
    parser.add_option("-i", "--ip", help="Robot IP", dest="ip", default="192.168.0.102")
    parser.add_option("-p", "--port", help="Port to connect to NaoQi", dest="port", type="int", default=9559)
    (opts, args_) = parser.parse_args()
    ip = opts.ip
    port = opts.port

    print("Connecting to robot on {}:{}".format(ip, port))

    ## play the game
    player = []
    #import pdb; pdb.set_trace()
    try:
        ## create player
        player = NaoXO(ip, port)

        # ## initialize robot stance
        # player.stanceInit()

        # ## initialize game, if the game does not start then exit
        # if not player.gameInit():
        #     player.cleanup()
        #     player=[]
        #     sys.exit()
        # print('Initialized game!!!')
        # time.sleep(2)

        # ## play the game
        # while True:
        #     if not player.play():
        #         ## Game is over
        #         ## TODO: ask if the opponent wants a rematch
        #         break

        # ## cleanup
        # player.cleanup()
        # player=[]
        # sys.exit()

    ## catch all errors
    except:
        ## if player was created, do cleanup
        if player:
            player.cleanup()
        ## reraise error
        raise

