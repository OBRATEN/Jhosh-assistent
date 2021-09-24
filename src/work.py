import sys
import webbrowser
import random
import speech_recognition as sr
import pyttsx3
import datetime
from fuzzywuzzy import fuzz
from os import system
from constants import Const


class Assistent():
    def __init__(self):
        self._n = int(input())
        self.r = sr.Recognizer()
        self.m = sr.Microphone(device_index=self._n)
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
        self.speak_engine = pyttsx3.init()
        self.voices = self.speak_engine.getProperty('voices')
        self.speak_engine.setProperty('voice', 'ru')
        self._OPTS = Const().OPTS

    def backer(self, recognizer, audio):
        try:
            voice = recognizer.recognize_google(audio,
                                                language="ru-RU").lower()
            print("[assistent] Распознано: " + voice)
            if voice.startswith(self._OPTS['names']):
                cmd = voice
                for x in self._OPTS['names']:
                    cmd = cmd.replace(x, "").strip()
                for x in self._OPTS['tbr']:
                    cmd = cmd.replace(x, "").strip()
                cmd = self.recognizing(cmd)
                self.execution(cmd['cmd'])
        except sr.UnknownValueError:
            print("[assistent] Голос не распознан!")
        except sr.RequestError:
            print("[assistent] Неизвестная ошибка, проверьте интернет!")

    def recognizing(self, cmd):
        Recogn_cmd = {'cmd': '', 'percent': 0}
        for c, v in self._OPTS['cmds'].items():
            for x in v:
                vrt = fuzz.ratio(cmd, x)
                if vrt > Recogn_cmd['percent']:
                    Recogn_cmd['cmd'] = c
                    Recogn_cmd['percent'] = vrt
        return Recogn_cmd

    def execution(self, cmd):
        if cmd == 'hi':
            self.talking("Здравствуй, пользователь")
        elif cmd == 'stuff':
            self.talking("Все системы работают исправно")
        elif cmd == 'curtime':
            now = datetime.datetime.now()
            self.talking(f"Сейчас {str(now.hour)}:{str(now.minute)}")
        elif cmd == 'stop':
            self.talking("Пока!")
            sys.exit()
        elif cmd == 'yt':
            self.talking("Открываю")
            webbrowser.open('https://www.youtube.com/')
        elif cmd == 'stupid':
            self.talking("Доделаю географию в школе")
        elif cmd == 'random':
            self.talking(str(random.randrange(1, 101)))
        elif cmd == 'browser':
            self.talking("Запускаю браузер")
            webbrowser.open("www.google.com")
        elif cmd == 'discord':
            self.talking("Запускаю дискорд")
            system("discord")
        elif cmd == 'zoom':
            self.talking("Запускаю зум")
            system("zoom")
        else:
            self.talking("Команда не распознана, повторите")

    def talking(self, what):
        print(what)
        self.speak_engine.say(what)
        self.speak_engine.runAndWait()
        self.speak_engine.stop()
