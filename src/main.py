from work import Assistent
import time


class Helper:
    def __init__(self):
        self.jhosh = Assistent()
        self.jhosh.talking("Добрый день")
        self.jhosh.talking("Я Джош, ваш ассистент")
        self.jhosh.talking("Готов распознавать ваши команды")

    def main(self):
        self.jhosh.r.listen_in_background(self.jhosh.m, self.jhosh.backer)
        while True:
            time.sleep(0.05)


if __name__ == "__main__":
    helper = Helper()
    helper.main()
