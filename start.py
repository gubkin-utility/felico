#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 22:11:26 2018

@author: zanettii

FELICO Mass Text File Editor V1

"""

from tkinter import Listbox,Label,Tk,END,LEFT,RIGHT,LabelFrame,Button,TOP,Y,Scrollbar,WORD,Text,StringVar,CURRENT,PhotoImage

from modules.alloptions.designoption import backgroundall,textcolor1,buttonbackground,buttonwidth,buttonobvodka,razmerbuttonobvodka,activebuttonbackground,favicon,donandlic,callback

import os
import platform

from modules.alloptions.examplestr import  example_razmnozenie



#ОСНОВНАЯ ФУНКЦИЯ ВЫБОРА
def getoption(evt):
    global viborpoz
    global examlpedisplay1
    getoption = mylistbox1.curselection()
    viborpoz = getoption[0]
    #ВЫВОД EXAMPLE FILE
    examlpedisplay1 = spisokopexample.get(str(viborpoz))

#ФУНКЦИЯ КНОПКИ ЗАПУСКА
def buttonpress():
    try:     
        startpath = spisokopforstart.get(str(viborpoz))
        #ОПРЕДЕЛЯЕМ ОПЕРАЦИОННУЮ СИСТЕМУ
        whyplatforms = platform.system()
        if whyplatforms == 'Windows':
            os.system(os.path.abspath("modules/" + startpath))
        else:
            os.system('python3 ' + os.path.abspath("modules/" + startpath))
    except:
        None

#ФУНКЦИЯ ДЛЯ ВЫВОДА EXAMPLE FILE
def help_upgrade():
    try:            
        eur.config(state='normal')
        eur.delete('1.0', END)
        examlpedisplay.set(examlpedisplay1)
        eur.insert(CURRENT, examlpedisplay.get())
        eur.config(state='disabled')
    except:
        None


window = Tk()
window.geometry("800x600")
window.title("FELICO | Mass Text File Editor ")

#FAVICON
try:
    window.iconphoto(True, PhotoImage(data=favicon))
except:
    None
    
window.configure(background=backgroundall)

#ДЛЯ МЕНЮ ОКНО
allframemenu = LabelFrame(text="menu",fg= textcolor1)
allframemenu.configure(background=backgroundall,fg= textcolor1)
                      
#ОКНО ВЫВОДА МЕТОДОВ                 
mylistbox1 = Listbox(allframemenu, width=40, height=20, font=("Helvetica", 12,),listvariable=getoption,exportselection=0)
mylistbox1.pack(side="left", fill="y")
scrollbar = Scrollbar(allframemenu, orient="vertical",background=backgroundall)
scrollbar.config(command=mylistbox1.yview)
scrollbar.pack(side="left", fill="y")
mylistbox1.config(yscrollcommand=scrollbar.set,background=buttonbackground)
mylistbox1.bind('<<ListboxSelect>>',getoption)

#СПИСОК ДЛЯ ЗАПУСКА
spisokopforstart = {
        '0':'razmnozenie.py',
        '1':'-----------------------',
        '2':'-----------------------',
        '3':'-----------------------',
        '4':'-----------------------',
        '5':'-----------------------',
        '6':'-----------------------',
        }

#СПИСОК ДЛЯ ВЫВОДА EXAMPLE FILE
spisokopexample = {
        '0':example_razmnozenie,
        '1':'-----------------------',
        '2':'-----------------------',
        '3':'-----------------------',
        '4':'-----------------------',
        '5':'-----------------------',
        '6':'-----------------------',
        }

#СПИСОК ДЛЯ ВЫВОДА НАЗВАНИЯ МЕТОДА НА ЭКРАН
spisokop = {
        '0':'замена по шаблону в общий файл',
        '1':'-----------------------',
        '2':'-----------------------',
        '3':'-----------------------',
        '4':'-----------------------',
        '5':'-----------------------',
        '6':'-----------------------',    
        }

#ЦИКЛ ДЛЯ ВЫВОДА НАЗВАНИЯ МЕТОДА НА ЭКРАН
for key,value in spisokop.items():
    mylistbox1.insert(END, value)


#FRAME ДЛЯ КНОПОК ВЫБОРА 
allframebuttton = LabelFrame(text="select",fg= textcolor1)
allframebuttton.configure(background=backgroundall)

#КНОПКА GO                   
Button(allframebuttton,text = "GO", command = buttonpress, width=buttonwidth,highlightbackground = buttonobvodka,highlightthickness = razmerbuttonobvodka, background = buttonbackground, activebackground=activebuttonbackground).pack(side=LEFT,padx = 80)
#КНОПКА example
Button(allframebuttton,text = "example", command = help_upgrade, width=buttonwidth,highlightbackground = buttonobvodka,highlightthickness = razmerbuttonobvodka, background = buttonbackground, activebackground=activebuttonbackground).pack(side=RIGHT,padx = 80)

#ДЛЯ ВЫБОРА ПЕРЕМЕННАЯ example file
examlpedisplay = StringVar()
examlpedisplay.set("")
quote = examlpedisplay.get()

#ОКНО ВЫВОДА EXAMPLE FILE
st = Scrollbar(allframemenu)
eur = Text(allframemenu, height=20, width=50,wrap=WORD,background=buttonbackground)
st.pack(side=RIGHT, fill=Y)
eur.pack(side=LEFT, fill=Y)
st.config(command=eur.yview,background=backgroundall)
eur.config(yscrollcommand=st.set)
eur.insert(END, quote)

allframemenu.pack(side=TOP,expand=True)
allframebuttton.pack(side=TOP,expand=True)

#ФУТЕР
openpage = Label(window, text=donandlic,background=backgroundall,fg= textcolor1, cursor="hand2")
openpage.pack()
openpage.bind("<Button-1>", callback)

window.mainloop()