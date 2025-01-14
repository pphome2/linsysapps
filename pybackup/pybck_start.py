#
# PyBCK start
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




# parancssori argumentumok
if (len(sys.argv)>0):
  for arg in sys.argv:
    if (arg=="-q")or(arg=="--quiet"):
      if (BCK_FILE_LOG==""):
        try:
          sys.stdout=open("pybck.log",'wt')
        except:
          if (BCK_DEV_MODE):
            print(pybck_lang("Hiba az argumentumok feldolgozása során. Kihagyva.")," - ",arg)
      else:
        try:
          sys.stdout=open(BCK_FILE_LOG,'wt')
        except:
          if (BCK_DEV_MODE):
            print(pybck_lang("Hiba a log áirányításakor. Kihagyva.")," - ",arg)
    elif (arg=="-a")or(arg=="--arch"):
      BCK_ARCH_MODE=True



# mentési könyvtár ellenőrzése
try:
  if (not os.path.isdir(BCK_DIR_DEST)):
    os.makedirs(BCK_DIR_DEST)
except:
  if (BCK_DEV_MODE):
    print(pybck_lang("Célkönyvtár nem elérhető, nem hozható létre. Jogosultsági probléma.")," - ",BCK_DIR_DEST)
  print(pybck_lang("Célkönyvtár nem létezik. Mentés nem készíthető."))
  quit()


# indítás
if (BCK_DEV_MODE):
  print("\n")
  n=datetime.datetime.now()
  print(n.strftime("%Y.%m.%d %H:%M"))
print("\n")
print(pybck_lang("Mentés indítása."))
print("\n")



# könyvtárak mentése
if not BCK_ARCH_MODE:
  pybck_backupdir_sys()
pybck_backupdir_user(BCK_ARCH_MODE)



# mentés befjezése



# kilépés
print("\n")
print(pybck_lang("Mentés befejezve."))
if (BCK_DEV_MODE):
  print("\n")
  n=datetime.datetime.now()
  print(n.strftime("%Y.%m.%d %H:%M"))
print("\n")



#

