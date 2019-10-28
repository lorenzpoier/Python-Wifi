'''
 Inhalt des Verzeichnis data auflisten bzw durchsuchen: os.walk
 alle .txt Dateien in das Verzeichnis 'import' moven <- regex
 beim 'moven' den namen auf kleinschreibung umstellen: shutil.move
 
 python lib: os
 funktioniert auf alle betriebssystemen
 python lib: shutil
 
(+ pfade aus der config Datei)

'''
import re
import os
import shutil
'''
pfad = 'H:/python/dateien/data/'
neuer_pfad = 'H:/python/dateien/import/'
for root, dirs, files in os.walk(pfad):
    dateien = files
    print(dateien) 
    
for dname in dateien:
    regexp_dateien = re.search(r'[.txt]{4}$', dname)
    if regexp_dateien:
        shutil.move(pfad + '/' + dname.lower(),neuer_pfad)
        
'''

#print(korrekte_endungen)
#print(regexp_dateien)

import datetime

target_dir = 'import'
source_dir = 'data'

dt = datetime.datetime.now()
new_targer_dir = "{:d}-{:d}-{:d}-{:d}{:d}_{:s}" \
    .format(dt.year, dt.month, dt.day, dt.hour, dt.minute, target_dir)

 
if not os.path.isdir(new_targer_dir):
    print('target dir does not exist - creating ...')
    os.mkdir(new_targer_dir)
 
for root, dirs, files in os.walk(source_dir):
    print(root, dirs, files)
    for file in files:
#        match = re.search(r'txt$',file)
        if file.endswith('.txt'):
            new_file_name = file.lower()
            #os.path.join macht je Betriebssystem einen gültigen Pfad
            shutil.move(os.path.join(source_dir, file), 
                        os.path.join(new_targer_dir, new_file_name))


