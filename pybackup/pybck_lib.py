#
# PyBCK
#
# rendszer modul
#

# gpg -c --batch --pinentry-mode loopback --passphrase Teszt1 pybck.log
# gpg -d --batch --pinentry-mode loopback --passphrase Teszt1 pybck.log.gpg



try:
  import os,sys,datetime
  from pybck_cfg import *
except:
  print("Szükséges modulok nem található (config). A program nem indítható.")
  quit()



# segéd eljárások objektum
class pybck_lib_obj:
  # első futás
  LOGFIRST=True

  # könyvtár ellenőrzés
  def pybck_dircheck(self):
    try:
      if (not os.path.isdir(pycfg.BCK_DIR_DEST)):
        os.makedirs(pycfg.BCK_DIR_DEST)
    except:
      if (pycfg.BCK_DEV_MODE):
        print(self.pybck_lang("Célkönyvtár nem elérhető, nem hozható létre. Jogosultsági probléma.")," - ",pycfg.BCK_DIR_DEST)
      print(self.pybck_lang("Célkönyvtár nem létezik. Mentés nem készíthető."))
      quit()
    return(True)

  # parancssori argumentumok
  def pybck_arg(self):
    if (len(sys.argv)>0):
      for arg in sys.argv:
        if (arg=="-q")or(arg=="--quiet"):
          if (pycfg.BCK_FILE_LOG==""):
            try:
              sys.stdout=open("pybck.log",'wt')
            except:
              if (pycfg.BCK_DEV_MODE):
                print(self.pybck_lang("Hiba az argumentumok feldolgozása során. Kihagyva.")," - ",arg)
          else:
            try:
              sys.stdout=open(pycfg.BCK_FILE_LOG,'wt')
            except:
              if (pycfg.BCK_DEV_MODE):
                print(self.pybck_lang("Hiba a log áirányításakor. Kihagyva.")," - ",arg)
        elif (arg=="-a")or(arg=="--arch"):
          pycfg.BCK_ARCH_MODE=True
    return(True)

  # szöveg kiírása
  def pybck_print(self,l):
    return(l)

  # szöveg fordítása
  def pybck_lang(self,l=""):
    try:
      ll=pycfg.BCK_LANG[l]
      self.pybck_log(ll)
    except:
      ll="."+l+"."
    return(ll)

  # logba írás
  def pybck_log(self,l=""):
    if (pycfg.BCK_FILE_LOG!=""):
      try:
        try:
          tf=open(pycfg.BCK_FILE_LOG,'a')
        except:
          tf=open(pycfg.BCK_FILE_LOG,'wt')
        if self.LOGFIRST:
          self.LOGFIRST=False
          n=datetime.datetime.now()
          lo="\n"+n.strftime("%Y.%m.%d %H:%M")+"\n\t"+l+"\n"
        else:
          lo="\t"+l+"\n"
        tf.write(lo)
        tf.close()
      except:
        return(False)
    return(True)



# objekum létrehozása
pylib=pybck_lib_obj()

#

