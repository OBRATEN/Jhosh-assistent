import os
from constants import Const


class Installer:
    def __init__(self):
        self.CMDS = Const().CMDS

    def main(self):
        for i in range(len(self.CMDS)):
            os.system(f"sudo apt search {self.CMDS[i]}")
            os.system(self.CMDS[i])
            print(f"Пакет {self.CMDS[i]} установлен.")
        print("Установка пакетов завершена.")


install = Installer()
install.main()
