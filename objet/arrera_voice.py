from gtts import gTTS as gt
from playsound3 import playsound as pl
import os
import threading as th
from librairy.travailJSON import jsonWork
import speech_recognition as sr


class CArreraVoice:
    def __init__(self,configFile:jsonWork):
        self.__configFile = configFile
        self.__emplacementSoundMicro = self.__configFile.lectureJSON("fileMicro")
        self.__soundMicro = True
        self.__outPutText = ""

    def loadConfig(self):
        if (self.__configFile.lectureJSON("soundMicro") == 1 ):
            self.__soundMicro = True
        else:
            self.__soundMicro = False

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

    def playFile(self,file:str):
        pl(file)

    def listen(self):
        if self.__soundMicro:
            pl(self.__emplacementSoundMicro)

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='fr-FR')
            self.__outPutText = text
            return 0
        except sr.UnknownValueError:
            return -1
        except sr.RequestError as e:
            return -2

    def getTextMicro(self):
        return self.__outPutText