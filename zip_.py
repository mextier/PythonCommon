# https://docs.python.org/3/library/zipfile.html

import zipfile

def compress_files(dbfilename, loginsfilename, archivename):
    try:
        print('[Compressing using zipfile module]')
        print_time_mark()
        print('[Archiving.....]')
        with zipfile.ZipFile(archivename, 'w', zipfile.ZIP_DEFLATED, True) as archive:
            archive.write(dbfilename, split(dbfilename)[1])
            archive.write(loginsfilename, 'logins.txt')
        print_time_mark()
        print('[Complete]')
        print('[File compressed at: {}]'.format(archivename))
        pass
    except:
        print('[General error while compressing!]')
        remove(archivename)
