# -*- coding: utf-8 -*-
import speech_recognition as sr

def func1():
    print('Скажите, что вам нужно поделить', '\n')
    mic = sr.Microphone(device_index=2)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    a = r.recognize_google(audio, language="ru-RU")
    a = a.split()
    print(a)
    return(int(a[0]) / int(a[2]))