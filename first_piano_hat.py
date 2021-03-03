#!/usr/bin/env python3

import pianohat
import time

from pygame import mixer

def handle_note(channel, pressed):
    if pressed:
        print("You pressed a key {}".format(channel))
    else:
        print("You released key {}".format(channel))

mixer.init(22050, -16, 2, 512)
mixer.set_num_channels(13)

pianohat.on_note(handle_note)

while True:
    time.sleep(0.001)
