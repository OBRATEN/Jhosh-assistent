class Const:
    def __init__(self):
        self.CMDS = ["sudo apt update",
                     "sudo apt upgrade"
                     "sudo apt install python3-pip",
                     "pip3 install pyttsx3",
                     "pip3 install SpeechRecognition",
                     "pip3 install fuzzywuzzy"]

        self.OPTS = {
            "names": ("джош", "джо", "джошуа", "джейджей", "dj", "josh", "дождь"),
            "tbr": ("скажи", "расскажи", "что ты думаешь", "покажи",
                    "сколько", "произнеси"),
            "cmds": {
                "hi": ("привет", "здаврова", "ку", "здравствуй"),
                "curtime": ("время", "который час", "сколько времени",
                            "сколько время", "что по времени"),
                "yt": ("youtube", "ютуб", "ютюб"),
                "random": ("число", "рандом", "случайное число"),
                "stop": ("стоп", "отключайся", "до свидания"),
                "stuff": ("как дела", "что как", "что думаешь"),
                "stupid": ("анекдот", "шутка", "шутку", "рассмеши"),
                "discord": ("discord", "дискорд"),
                "zoom": ("zoom", "зум"),
                "browser": ("browser", "браузер", "сайт", "интернет")
            }
        }

    def return_const(self):
        return f"{self.OPTS} \n {self.CMDS}"
