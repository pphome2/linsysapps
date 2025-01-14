#
# rendszer modul
#


try:
  import datetime
  from pybck_cfg import *
except:
  print("Szükséges modulok nem található (config). A program nem indítható.")
  quit()



# első futás
LOGFIRST=True

# szöveg fordítása
def pybck_lang(l=""):
  try:
    ll=BCK_LANG[l]
  except:
    ll="."+l+"."
  pybck_log(ll)
  return(ll)



# logba írás
def pybck_log(l=""):
  global LOGFIRST

  if (BCK_FILE_LOG!=""):
    try:
      try:
        tf=open(BCK_FILE_LOG,'a')
      except:
        tf=open(BCK_FILE_LOG,'wt')
      if LOGFIRST:
        LOGFIRST=False
        n=datetime.datetime.now()
        lo="\n"+n.strftime("%Y.%m.%d %H:%M")+"\n\t"+l+"\n"
      else:
        lo="\t"+l+"\n"
      tf.write(lo)
      tf.close()
    except:
      return(False)
  return(True)



#

