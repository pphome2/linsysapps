#
# PyBCK
#
# mentés modul
#

# modulok betöltése
try:
  import os,gzip,io,tarfile
  from pybck_cfg import *
  from pybck_lib import *
except:
  print("Szükséges modulok nem található (lib). A program nem indítható.")
  quit()



# mentés objektum
class pybck_backup_obj:
  # kizárás a mentésből
  def pybck_ffilter(self,tarinfo):
    for ex in pycfg.BCK_DIR_EXCLUDE_MAINDIR:
      ex="/"+ex
      if ex in tarinfo.name:
        return(None)
    return(tarinfo)

  # kizárás a mentésből
  def pybck_ffilter_excl(self,tarinfo):
    for ex in pycfg.BCK_DIR_EXCLUDE_MAINDIR:
      ex="/"+ex
      if ex in tarinfo.name:
        return(tarinfo)
    return(None)

  # fájlok listája az adott könyvtárban (rekutzív)
  def pybck_filelist(self,tf,da):
    dl=os.listdir(da)
    for ud in dl:
      dn=da+"/"+ud
      if os.path.isdir(dn):
        self.pybck_filelist(tf,dn)
      else:
        if pycfg.BCK_ARCH_MODE:
          tf.add(dn,filter=self.pybck_ffilter_excl)
        else:
          tf.add(dn,filter=self.pybck_ffilter)
    return(True)

  # felhasználói könyvárak mentése
  def pybck_backupdir_user(self):
    root=pycfg.BCK_DIR_USER_HOME
    try:
      if pycfg.BCK_ARCH_MODE:
        an="_"
      else:
        an=""
      dl=os.listdir(root)
      for ud in dl:
        dn=root+"/"+ud
        udl=os.listdir(dn)
        for udd in udl:
          if udd in pycfg.BCK_DIR_USER:
            if (pycfg.BCK_DIR_DEST==""):
              tarf=an+ud+"-"+udd+".tar.gz"
            else:
              tarf=pycfg.BCK_DIR_DEST+"/"+an+ud+"-"+udd+".tar.gz"
            pylib.pybck_log(udd+" - "+tarf)
            out=udd+" - "+tarf
            print(pylib.pybck_print(out))
            try:
              if (os.path.isfile(tarf)):
                os.remove(tarf)
              tf=tarfile.open(tarf,"w:gz")
              da=dn+"/"+udd
              self.pybck_filelist(tf,da)
              tf.close()
            except:
              if (pycfg.BCK_DEV_MODE):
                print(pylib.pybck_lang("Tömörítési hiba.")," - ",dn) 
              print(pylib.pybck_lang("Hiba történt.")," - ",dn) 
              print(pylib.pybck_print("\n"))
    except:
      print(pylib.pybck_print("\n"))
      if (pycfg.BCK_DEV_MODE):
        print(pylib.pybck_lang("Jogosultsági probléma.")," - ",dn)
      print(pylib.pybck_lang("Kihagyva.")," - ",dn)
    return(True)

  # rendszer könyvtárak mentése
  def pybck_backupdir_sys(self):
    for udd in pycfg.BCK_DIR_SYS:
      tfn=udd[1:]
      tfn=tfn.replace("/","_")
      if (pycfg.BCK_DIR_DEST==""):
        tarf=tfn+".tar.gz"
      else:
        tarf=pycfg.BCK_DIR_DEST+"/"+tfn+".tar.gz"
      pylib.pybck_log(udd+" - "+tarf)
      out=udd+" - "+tarf
      print(pylib.pybck_print(out))
      try:
        if (os.path.isfile(tarf)):
          os.remove(tarf)
        tf=tarfile.open(tarf,"w:gz")
        tf.add(udd,arcname=udd)
        tf.close()
      except:
        if (pycfg.BCK_DEV_MODE):
          print(pylib.pybck_lang("Tömörítési hiba. Jogosultsági probléma.")," - ",tarf) 
        print(pylib.pybck_lang("Hiba történt.")) 
        print(pylib.pybck_print("\n"))
    return(True)



# objektum létrehozása
pybcko=pybck_backup_obj()


#

