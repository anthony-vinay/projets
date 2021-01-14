# -*- coding: utf-8 -*-

import os

os.system('cat edt.txt|head -44|tail -11 > tmp_edt.txt')
#os.system('cat tmp_edt.txt|grep DT|cut -d : -f2|cut -c1-8|tail -1>tmp_cours.txt')#date
os.system('cat tmp_edt.txt|grep SUMMARY|cut -d : -f2|cut -d - -f1 > tmp_cours.txt') #Module
os.system('cat tmp_edt.txt|grep SUMMARY|cut -d : -f2|cut -d - -f2 >> tmp_cours.txt') #recuperer le nom des profs
os.system(' cat tmp_edt.txt | grep DTSTART|cut -d : -f2|cut -c10-13 >> tmp_cours.txt' ) #Récuperer les heures de début de cours
os.system('cat tmp_edt.txt | grep DTEND|cut -d : -f2|cut -c10-13 >> tmp_cours.txt') #Recupérer les heures de fin du cours
