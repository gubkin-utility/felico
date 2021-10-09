# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import re

from PySide2.QtGui import QGuiApplication, QIcon
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QThread, Slot, Signal


class Standart(QThread):
    def __init__(self):
        QThread.__init__(self)
        #АТРИБУТ СТОП
        self.running = False


    modPath = Signal(str, arguments=['modpath'])


    @Slot(str)
    #ПУТЬ ФИНАЛЬНОГО ФАЙЛА
    def make_path(self, path):
        head, tail = os.path.split(path)
        head = re.sub(tail, '', path, flags=re.MULTILINE)
        file_path = head + 'OUTput.txt'
        self.modPath.emit(file_path)


    @Slot(str)
   #ТЕСТ КОДИРОВКИ
    def test_codirovka(self,file,):
        file = file.lstrip("file:///")
        status = "True"
        try:
            with open(file,'r', encoding='utf-8') as f:
                opentxtfile = f.read()
        except:
            status = "False"
        self.forTectcoding.emit(status)


    #ОТКРЫТЬ ФАЙЛ
    def openfile(self, file):
        with open(file,'r', encoding='utf-8') as f:
            opentxtfile = f.read()
        return opentxtfile



    #ОТКРЫТЬ ФАЙЛ СПИСОК
    def openfilelist(self, file):
        with open(file,'r', encoding='utf-8') as f:
            opentxtfile = f.readlines()
        return opentxtfile


    #ОПРЕДЕЛЯЕМ КОЛИЧЕСТВО СТРОК В ФАЙЛЕ
    def skolstrok(self, file):
        with open(file,'r', encoding='utf-8') as f:
                return len(f.readlines())


    #ЗАПИСАТЬ В ФАЙЛ
    def writefile(self, file,metod,zapis):
        with open(file,metod, encoding='utf-8') as f:
            opentxtfile = f.write(zapis)
        return opentxtfile


    nowProgbar = Signal(int, arguments=['nowprogbar'])
    maxProgbar = Signal(int, arguments=['maxprogbar'])
    #СИГНАЛ ОКОНЧАНИЯ ПРОЦЕССА
    allOk = Signal(str, arguments=['allok'])
    #ТЕСТ КОДИРОВКИ
    forTectcoding = Signal(str, arguments=['fortectcoding'])


    @Slot(str, str, str, str)
    #ОБРАБОТЧИК (file_path - переменные, file_path2 - заготова, file_path3 - финал)
    def felico(self, file_path, file_path2, file_path3, chtomenaem):
        file_path = file_path.lstrip("file:///")
        file_path2 = file_path2.lstrip("file:///")
        file_path3 = file_path3.lstrip("file:///")
        #ДЛЯ ОСТАНОВКИ ЦИКЛА
        self.running = True
        max_progbar  = self.skolstrok(file_path)
        #ДЛЯ ПРОГРЕССБАРА MAX VALUE
        self.maxProgbar.emit(max_progbar)
        #ДЛЯ ПРОГРЕССБАРА MIN VALUE
        now_progbar = 0
        #ЛИСТ ПЕРЕМЕННЫХ ДЛЯ ЗАМЕНЫ
        lst_zamena = self.openfilelist(file_path)
        lst_zamena = [i.rstrip() for i in lst_zamena]
        for i in range(self.skolstrok(file_path)):
            #ДЛЯ ОСТАНОВКИ ЦИКЛА
            if self.running == False:
                break
            #МЕНЯЕМ
            replaceok = self.openfile(file_path2).replace(chtomenaem,lst_zamena.pop(0))
            if replaceok.endswith('\n') == False:
                replaceok +='\n'
            #ЗАПИСЫВАЕМ В ФАЙЛ ГОТОВО
            self.writefile(file_path3,'a',replaceok)
            now_progbar +=1
            self.nowProgbar.emit(now_progbar)
        #ПРОГРЕССБАР НА 0
        self.nowProgbar.emit(0)
        self.allOk.emit("OK")




if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon("img/icon.png"))
    app.setOrganizationName("null")
    app.setOrganizationDomain("null")
    standart = Standart()
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("standart", standart)
    engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
