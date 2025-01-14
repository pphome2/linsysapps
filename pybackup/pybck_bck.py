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




# kizárás a mentésből
def pybck_ffilter(tarinfo):
  for ex in BCK_DIR_EXCLUDE_MAINDIR:
    ex="/"+ex
    if ex in tarinfo.name:
      return(None)
  return(tarinfo)



# kizárás a mentésből
def pybck_ffilter_excl(tarinfo):
  for ex in BCK_DIR_EXCLUDE_MAINDIR:
    ex="/"+ex
    if ex in tarinfo.name:
      return(tarinfo)
  return(None)



# fájlok listája az adott könyvtárban (rekutzív)
def pybck_filelist(tf,da,archm):
  dl=os.listdir(da)
  for ud in dl:
    dn=da+"/"+ud
    if os.path.isdir(dn):
      pybck_filelist(tf,dn,archm)
    else:
      if archm:
        tf.add(dn,filter=pybck_ffilter_excl)
      else:
        tf.add(dn,filter=pybck_ffilter)
  return(True)



# felhasználói könyvárak mentése
def pybck_backupdir_user(archm=False):
  root="/home"
  try:
    if archm:
      an="_"
    else:
      an=""
    dl=os.listdir(root)
    for ud in dl:
      dn=root+"/"+ud
      udl=os.listdir(dn)
      for udd in udl:
        if udd in BCK_DIR_USER:
          if (BCK_DIR_DEST==""):
            tarf=an+ud+"-"+udd+".tar.gz"
          else:
            tarf=BCK_DIR_DEST+"/"+an+ud+"-"+udd+".tar.gz"
          pybck_log(udd+" - "+tarf)
          print(udd," - ",tarf)
          try:
            if (os.path.isfile(tarf)):
              os.remove(tarf)
            tf=tarfile.open(tarf,"w:gz")
            da=dn+"/"+udd
            pybck_filelist(tf,da,archm)
            #tf.add(da,arcname=udd)
            tf.close()
          except:
            if (BCK_DEV_MODE):
              print(pybck_lang("Tömörítési hiba.")," - ",dn) 
            print(pybck_lang("Hiba történt.")," - ",dn) 
            print("\n")
  except:
    print("\n")
    if (BCK_DEV_MODE):
      print(pybck_lang("Jogosultsági probléma.")," - ",dn)
    print(pybck_lang("Kihagyva.")," - ",dn)
  return(True)



# rendszer könyvtárak mentése
def pybck_backupdir_sys():
  for udd in BCK_DIR_SYS:
    tfn=udd[1:]
    tfn=tfn.replace("/","_")
    if (BCK_DIR_DEST==""):
      tarf=tfn+".tar.gz"
    else:
      tarf=BCK_DIR_DEST+"/"+tfn+".tar.gz"
    pybck_log(udd+" - "+tarf)
    print(udd," - ",tarf)
    try:
      if (os.path.isfile(tarf)):
        os.remove(tarf)
      tf=tarfile.open(tarf,"w:gz")
      tf.add(udd,arcname=udd)
      tf.close()
    except:
      if (BCK_DEV_MODE):
        print(pybck_lang("Tömörítési hiba. Jogosultsági probléma.")," - ",tarf) 
      print(pybck_lang("Hiba történt.")) 
      print("\n")
  return(True)




#

