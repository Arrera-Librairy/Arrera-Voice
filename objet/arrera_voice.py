from gtts import gTTS as gt
from playsound3 import playsound as pl
import os
import threading as th


class CArreraVoice:
    def __init__(self):
        pass

    def say(self,text:str):
        tts = gt(text, lang='fr')
        thCreate = th.Thread(target=tts.save, args=('voc.mp3',))
        thCreate.start()
        thCreate.join()
        del thCreate
        pl('voc.mp3')
        thRemove = th.Thread(target=os.remove, args=('voc.mp3',))
        thRemove.start()
        thRemove.join()
        del thRemove
