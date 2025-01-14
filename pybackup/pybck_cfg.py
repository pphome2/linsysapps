#
# beállítások
#

# fejlesztői mód
BCK_DEV_MODE=True

# felhasználó fájljai
BCK_DIR_USER=['Dokumentumok',
              'Asztal']

# mentésből kizárt könyvárak - 
BCK_DIR_EXCLUDE_MAINDIR=['_']

# rendszer könyvtárak
BCK_DIR_SYS=['/etc',
             '/var/www/html',
             '/var/www']

# mentési célkönyvtár
BCK_DIR_DEST="/opt/pybck"

# log fájlj
#BCK_FILE_LOG="/var/log/pybck.log"
BCK_FILE_LOG="pybck.log"

# archiválás: az eddig kizárt könyvtárak mentése
BCK_ARCH_MODE=False

# nyelvi modul
try:
  from pybck_hu_HU import *
except:
  BCK_LANG={}
  

#

