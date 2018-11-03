#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 22:37:26 2018

@author: zanettii

FELICO Mass Text File Editor V1

ЗАМЕНА ПО ШАБЛОНУ В ОБЩИЙ ФАЙЛ

"""

import allfunc
from alloptions.designoption import favicon,backgroundall,textcolor1,textcolor2,textcoloralert,buttonobvodka,razmerbuttonobvodka,buttonbackground,activebuttonbackground,buttonwidth,donandlic,callback

from alloptions.options import startworkdir
from alloptions.examplestr import example_razmnozenie
import os
import re
from tkinter import Frame,Tk,StringVar,Message,Button,filedialog,Entry,LabelFrame,Text,END,BOTTOM,LEFT,RIGHT,N,Y,Scrollbar,WORD,PhotoImage,Label,S
import platform

#КНОПКА ОБЗОР ФАЙЛ С ПЕРЕМЕННЫМИ ДЛЯ ЗАМЕНЫ
def browse_button():
    global file_path
    global file_path3
    global errorwindow
    try:
        file_path = filedialog.askopenfilename(initialdir = startworkdir,title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
        head, tail = os.path.split(file_path)
        head = re.sub(tail, '', file_path, flags=re.MULTILINE)
        file_path3 = head + 'output.txt'
    except:
        errorwindow = 'ФАЙЛ НЕ ВЫБРАН'
        print('ФАЙЛ НЕ ВЫБРАН')
    return file_path,file_path3


#ИЗМЕНЕНИЕ ТЕКСТА НА LABEL
def labelupgrade():
    pathlabel.config(text=file_path)
    window.after(100, labelupgrade)
    

#КНОПКА ОБЗОР ФАЙЛ ЗАГОТОВКА
def browse_button2():
    global file_path2
    global errorwindow
    try:
        file_path2 = filedialog.askopenfilename(initialdir = startworkdir,title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    except:
        errorwindow = 'ФАЙЛ НЕ ВЫБРАН'
        print('ФАЙЛ НЕ ВЫБРАН')
    return file_path2


#ИЗМЕНЕНИЕ ТЕКСТА НА LABEL
def labelupgrade2():
    pathlabel2.config(text=file_path2)
    window.after(100, labelupgrade2)
 
#ИЗМЕНЕНИЕ ТЕКСТА НА LABEL 
def labelupgrade3():
    pathlabel3.config(text=file_path3)
    window.after(100, labelupgrade3)

#ЗАПУСК
def allstart():
    global errorwindow
    if len(file_path) < 1:
        errorwindow = 'НЕ УКАЗАН ФАЙЛ С ПЕРЕМЕННЫМИ ДЛЯ ЗАМЕНЫ'
        print('НЕ УКАЗАН ФАЙЛ С ПЕРЕМЕННЫМИ ДЛЯ ЗАМЕНЫ')
    if len(file_path2) < 1:
        errorwindow = 'НЕ УКАЗАН ФАЙЛ ЗАГОТОВКА'
        print('НЕ УКАЗАН ФАЙЛ ЗАГОТОВКА')
    else:
        #ОПРЕДЕЛЯЕМ ОПЕРАЦИОННУЮ СИСТЕМУ
        whyplatforms = platform.system()
        #ЕСЛИ WIN ДОБАВЛЯЕМ В КОНЕЦ ФАЙЛОВ /n - WINDOWS OS
        if whyplatforms == 'Windows':
            allfunc.writefile(file_path,'a','\n')
            allfunc.writefile(file_path2,'a','\n')
            
        for i in range(allfunc.skolstrok(file_path)):
            #ОТКРЫВАЕМ ФАЙЛ С ПЕРМЕННЫМИ ДЛЯ ЗАМЕНЫ И БЕРЕМ СТРОКУ
            strone = allfunc.getnlinefromfile(file_path,1)
            #МЕНЯЕМ
            replaceok = allfunc.openfile(file_path2).replace(chtomenaem.get(),strone)
            #ЗАПИСЫВАЕМ В ФАЙЛ ГОТОВО
            allfunc.writefile(file_path3,'a',replaceok)
            errorwindow = 'All ok, Your file: ' + file_path3

#ИЗМЕНЕНИЕ ТЕКСТА НА LABEL
def labelupgrade5():
    pathlabel5.config(text=errorwindow)
    window.after(100, labelupgrade5)



window = Tk()
window.geometry("800x600")
window.title("FELICO | замена по шаблону в общий файл ")

#FAVICON
try:
    window.iconphoto(True, PhotoImage(data=favicon))
except:
    None

window.configure(background=backgroundall)

allframe = LabelFrame(text="menu")
allframe.configure(background=backgroundall,fg= textcolor1)

#ФАЙЛ С ПЕРЕМЕННЫМИ ДЛЯ ЗАМЕНЫ
framefile_path = LabelFrame(allframe,text="файл с переменными для замены",fg= textcolor1)
framefile_path.configure(background=backgroundall)
file_path = ''
pathlabel = Message(framefile_path, text = labelupgrade, aspect=300,background=backgroundall,fg = textcolor2,font=("Arial",12))
pathlabel.pack()

Button(framefile_path,text="Browse", command=browse_button, width=buttonwidth,highlightbackground = buttonobvodka,highlightthickness = razmerbuttonobvodka, background = buttonbackground, activebackground=activebuttonbackground).pack(padx = 25)
framefile_path.pack(pady = 10)

#ФАЙЛ ЗАГОТОВКА
framefile_path2 = LabelFrame(allframe,text="файл заготовка",fg= textcolor1)
framefile_path2.configure(background=backgroundall)
file_path2 = ''
pathlabel2 = Message(framefile_path2, text = labelupgrade2, aspect=300,background=backgroundall,fg = textcolor2,font=("Arial",12))
pathlabel2.pack()

Button(framefile_path2, text="Browse", command=browse_button2,width=buttonwidth,highlightbackground = buttonobvodka,highlightthickness = razmerbuttonobvodka, background = buttonbackground, activebackground=activebuttonbackground).pack(padx = 25)
framefile_path2.pack()

#ФИНАЛЬНЫЙ ОБЩИЙ ФАЙЛ
framefile_path3 = LabelFrame(allframe,text="путь к финальному файлу",fg= textcolor1)
framefile_path3.configure(background=backgroundall)
file_path3 = ''
pathlabel3 = Message(framefile_path3, text = labelupgrade3, aspect=300,background=backgroundall,fg = textcolor2,font=("Arial",12))
pathlabel3.pack(padx = 70,pady = 15)
framefile_path3.pack()

#ЧТО МЕНЯЕМ
framechtomenaem = LabelFrame(allframe,text="что меняем",fg= textcolor1)
framechtomenaem.configure(background=backgroundall)
chtomenaem = StringVar()
Entry(framechtomenaem, textvariable=chtomenaem, width=20,bd=3, background = 'AntiqueWhite').pack(padx = 32,pady = 15)
#ЗНАЧЕНИЕ ПО УМОЛЧАНИЮ
chtomenaem.set('*')
framechtomenaem.pack()

#КНОПКА ЗАПУСК
framestart = LabelFrame(allframe,text="select",fg= textcolor1)
framestart.configure(background=backgroundall)
Button(framestart, text='GO', command=allstart,width=buttonwidth,highlightbackground = buttonobvodka,highlightthickness = razmerbuttonobvodka, background = buttonbackground, activebackground=activebuttonbackground).pack(padx = 27,pady = 15)
framestart.pack()
allframe.pack(side=LEFT,anchor = N,ipadx =100, ipady = 150)

#ОКНО С ОШИБКАМИ
frameniz = LabelFrame(window,text="log",fg= textcolor1)
frameniz.configure(background=backgroundall)
errorwindow = ''
pathlabel5 = Message(frameniz, text = labelupgrade5,aspect=300,background=backgroundall,fg = textcoloralert,font=("Arial",12))
pathlabel5.pack()
frameniz.pack(side=BOTTOM,ipadx =500,ipady = 70)

#ОКНО СО СПРАВКОЙ
framehelp = LabelFrame(text="example",fg= textcolor1)
framehelp.configure(background=backgroundall)
st = Scrollbar(framehelp)
eur = Text(framehelp, height=120, width=70,wrap=WORD,background=buttonbackground)
st.pack(side=RIGHT, fill=Y)
eur.pack(side=LEFT, fill=Y)
st.config(command=eur.yview,background=backgroundall)
eur.config(yscrollcommand=st.set)
quote = example_razmnozenie
eur.insert(END, quote)
eur.config(state='disabled')
framehelp.pack()


labelupgrade()
labelupgrade2()
labelupgrade3()
labelupgrade5()

frame = Frame(window)
frame.pack()

#ФУТЕР
openpage = Label(allframe, text=donandlic,background=backgroundall,fg= textcolor1, cursor="hand2")
openpage.pack(side=BOTTOM,expand=True,anchor = S)
openpage.bind("<Button-1>", callback)


window.mainloop()