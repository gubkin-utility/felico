#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 22:37:26 2018

@author: zanettii

felico mass text editor V1

ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ

"""

import re

#УДАЛИТЬ СТРОКИ И ВЕРНУТЬ ИХ СПИСКОМ
def getnlinefromfile(file,skolkostrok):
    sres = []
    with open(file,'r',encoding='utf-8') as f:
        jj = f.readlines()
    for i in range(skolkostrok):
        strok = jj.pop(0)
        sres.append(strok)
    with open(file,'w', encoding='utf-8') as f:
        f.writelines(jj)
    sres = ''.join(sres).lstrip().rstrip()
    return sres

#ОТКРЫТЬ ФАЙЛ        
def openfile(file):
    with open(file,'r', encoding='utf-8') as f:
        opentxtfile = f.read()
    return opentxtfile
    
#ЗАПИСАТЬ В ФАЙЛ        
def writefile(file,metod,zapis):
    with open(file,metod, encoding='utf-8') as f:
        opentxtfile = f.write(zapis)
    return opentxtfile

#ОПРЕДЕЛЯЕМ КОЛИЧЕСТВО СТРОК В ФАЙЛЕ
def skolstrok(file):    
    dlinakeyword = len(re.findall(r"[\n]+", openfile(file)))
    return dlinakeyword

