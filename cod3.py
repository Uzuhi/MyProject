# -*- coding: utf-8 -*-
import webbrowser as wb
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
'''
text = 'python'
url = 'https://google.com/search?q=' + text
wb.open("https://google.com/search?q="+text)
'''
def func3():
    print("Скажите, что вы хотите найти", '\n')
    mic = sr.Microphone(device_index=2)
    f = sr.Recognizer()
    with sr.Microphone() as source:
        Audio = f.listen(source)
    b = f.recognize_google(Audio, language="ru-RU")
    wb.open("https://google.com/search?q="+b)
