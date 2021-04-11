import os
import sys
from shutil import copyfile
import getpass
# ruta completa de AppData
path = "C:/Users/"+str(getpass.getuser())+"/AppData"
files_chrome = [
    'Cookies', # Todas las cookies
    'History', # Todo el historial
    'Bookmarks' # Todos los marcadores
]
len_files_chrome = len(files_chrome)
files_firefox = [
    'places.sqlite', # Marcadores, descargas e historial de navegación
    'formhistory.sqlite', # Historial de autocompletado
    'cookies.sqlite', # Todas las cookies
]
len_files_firefox = len(files_firefox)
def Chrome():
    for file in range(len_files_chrome):
        copyfile(path+"/Local/Google/Chrome/User Data/Default/"+files_chrome[file],'Chrome_data/'+files_chrome[file])
def Firefox():
   firefox_path = path+"/Roaming/Mozilla/Firefox/Profiles/"
   folder_name = os.listdir(firefox_path)[1]
   firefox_path = firefox_path+folder_name+'/'
   for file in range(len_files_firefox):
        copyfile(firefox_path+files_firefox[file],'Firefox_data/'+files_firefox[file])
while True:
    print("#1: Chrome")
    print("#2: Firefox")
    print("#3: Exit")
    val = input()
    if val == "1":
        try:
            os.mkdir('Chrome_data')
        except:
            print('Folder update')
        Chrome()
    elif val == "2":
        try:
            os.mkdir('Firefox_data')
        except:
            print('Folder update')
        Firefox()
    elif val == "3":
        break