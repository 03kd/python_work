# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:04:04 2019

@author: keshav singh
"""

#Speech Recogniton
import speech_recognition as sr

AUDIO_FILE =("k.wav")

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio =r.record(source)

try:
    print("audio files contain "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Audio cannot understand")
except sr.RequestError:
    print("Get not result")