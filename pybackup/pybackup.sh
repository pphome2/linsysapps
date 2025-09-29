#!/bin/bash

#
# PyBCK starter
#

dir=`pwd`
py=`command -v python`
pymain="pybck_start.py"

if [ ! -n "$py" ]; then
  py=`command -v python3`
fi

if [ -n "$py" ]; then
  echo "Python telepítés:$py"
else
  echo "Python telepítés nem található."
fi

if [ -f $dir/$pymain ]; then
  $py $dir/$pymain --arch
  rm -rf __pycache__
else
  echo "A program nem található..."
fi

cd $dir

#

