#!/bin/bash

user=$(whoami)
proc=$(ps -f)

host=$(hostname)
mdate=$(date +%Y-%m-%d_%H:%M:%S)

apath=$host"_"
bpath=$apath$mdate

fullpath="logs/"$bpath".ini"

echo "[USER]" >> $fullpath
echo "user = $user" >> $fullpath

echo "" >> $fullpath
echo "[PROCESS]" >> $fullpath
# liste des processus un peu longue pour etre stockée