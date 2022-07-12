# -*- coding: utf-8 -*-
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import speech_recognition as sr

def func6():
    print("Скажите: ВЫКЛЮЧИТЬ ЗВУК или ВКЛЮЧИТЬ ЗВУК", '\n')
    mic = sr.Microphone(device_index=2)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    a = r.recognize_google(audio, language="ru-RU")

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    b = 100
    proverka = False
    if a == 'выключить звук':
        while(proverka == False):
            try:
                volume.SetMasterVolumeLevel(-b, None)
            except:
                b -= 1
            else:
                proverka = True

    if a == 'Включить звук':
        volume.SetMasterVolumeLevel(-25.0, None)