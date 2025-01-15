#
# PyBCK
#
# beállítások
#


# beállítások objektum
class pybck_config_obj:
  # fejlesztői mód
  BCK_DEV_MODE=True

  # felhasználó fájljai
  BCK_DIR_USER=['Dokumentumok',
                'Asztal']

  # felhasználók alapkönyvtára
  BCK_DIR_USER_HOME="/home"

  # mentésből kizárt könyvárak - 
  BCK_DIR_EXCLUDE_MAINDIR=['_']

  # rendszer könyvtárak
  BCK_DIR_SYS=['/etc',
               '/var/www/html',
               '/var/www']

  # mentési célkönyvtár
  BCK_DIR_DEST="/opt/pybck"

  # log fájlj #BCK_FILE_LOG="/var/log/pybck.log"
  BCK_FILE_LOG="pybck.log"

  # archiválás: az eddig kizárt könyvtárak mentése
  BCK_ARCH_MODE=False

  # nyelvi adatok
  #BCK_LANG={}

  # létrehozáskori beállítások
  def __init__(self):
    self.BCK_LANG={}

  # változó módosítása
  def newdest(self,d):
    print(d)
    self.BCK_DIR_DEST=d



# objektum létrehozása
pycfg=pybck_config_obj()


# nyelvi modul
try:
  from pybck_hu_HU import *
  pycfg.BCK_LANG=pydict.dict_lang
except:
  if pycfg.BCK_DEV_MODE:
    print("nolang")
  

#

