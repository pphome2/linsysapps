#
# PyBCK
#
# indító
#


# python modulok betöltése
try:
  import os,io,sys,json,gzip,tarfile,datetime
except:
  print("Szükséges modulok nem találhatók. A program nem indítható.")
  quit()


# a program beállításainak betöltése
try:
  import pybck_cfg
  from pybck_lib import *
  from pybck_bck import *
except:
  print("Szükséges modulok nem található (config). A program nem indítható.")
  quit()



# nyelvi fájl betőltés ellenőrzése
# print(pylib.pybck_lang("első"))

# indítási argmentumok feldolgozása
pylib.pybck_arg()

# mentési könyvtár ellenőrzése
pylib.pybck_dircheck()



# indítás
if (pycfg.BCK_DEV_MODE):
  print(pylib.pybck_print("\n"))
  n=datetime.datetime.now()
  print(pylib.pybck_print(n.strftime("%Y.%m.%d %H:%M")))
print(pylib.pybck_print("\n"))
print(pylib.pybck_lang("Mentés indítása."))
print(pylib.pybck_print("\n"))


# könyvtárak mentése
if not pycfg.BCK_ARCH_MODE:
  pybcko.pybck_backupdir_sys()
pybcko.pybck_backupdir_user()



# mentés befejezése
print(pylib.pybck_print("\n"))
print(pylib.pybck_lang("Mentés befejezve."))
if (pycfg.BCK_DEV_MODE):
  print(pylib.pybck_print("\n"))
  n=datetime.datetime.now()
  print(pylib.pybck_print(n.strftime("%Y.%m.%d %H:%M")))



# kilépés
print(pylib.pybck_print("\n"))



#

