#https://pythonworld.ru/moduli/modul-os.html
#https://pythonworld.ru/moduli/modul-os-path.html
#https://www.youtube.com/watch?v=ve2pmm5JqmI
#https://www.youtube.com/watch?v=tJxcKyFMTGo

from os import system, getcwd, makedirs, listdir, remove, getpid, name, chdir
from os.path import join, dirname, exists, splitext, isfile, getctime, split
import zipfile
from time import time
from datetime import datetime


print(name)

print(getpid())



wd = getcwd()
print(wd)

filename = join(getcwd(), 'Backups','1')
print(filename)

if not exists(dirname(filename)):
    makedirs(dirname(filename))

#system("notepad.exe {}".format(filename))




# def compress_files(dbfilename, loginsfilename, archivename):
#     try:
#         print('[Compressing using zipfile module]')
#         print_time_mark()
#         print('[Archiving.....]')
#         with zipfile.ZipFile(archivename, 'w', zipfile.ZIP_DEFLATED, True) as archive:
#             archive.write(dbfilename, split(dbfilename)[1])
#             archive.write(loginsfilename, 'logins.txt')
#         print_time_mark()
#         print('[Complete]')
#         print('[File compressed at: {}]'.format(archivename))
#         pass
#     except:
#         print('[General error while compressing!]')
#         remove(archivename)


# def clean_workspaces(workspaces, keep_days):
#     for workspace in workspaces:
#         for itm in [join(workspace, f) for f in listdir(workspace) if isfile(join(workspace, f))]:
#             ext = splitext(itm)[1]
#             if (ext == '.bak') \
#                     or (ext == '.txt') \
#                     or ((timedelta(seconds=time() - getctime(itm)).days > keep_days) and ext == '.zip'):
#                 print('[Delete file: {}]'.format(itm))
#                 remove(itm)
#





curDir='E:\\projects'
chdir(curDir)
while True:
    print('>',curDir)
    print('  x exit')
    print('  0 back')
    dirs = listdir()
    for (i,f) in enumerate(dirs):
        print('{:>3} {}'.format(i+1,f))
    print('-'*32)
    i=input("Your choice:")
    print('-'*32)
    if i[:1]=="x":
        print("Good bye!")
        break
    elif i=="0":
        chdir('..')
        curDir=getcwd()
    else:
        try:
            c=int(i)
            if c not in range(1,len(dirs)+1):
                raise ValueError 
            if not isfile(join(curDir,dirs[int(i)-1])):
                curDir=join(curDir,dirs[int(i)-1])
                chdir(curDir)
        except ValueError:
            print("Can't understand what you are saying!")
