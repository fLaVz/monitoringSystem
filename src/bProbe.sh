#!/bin/bash

#who | python -c 'import getUser; print getUser.fonction1()'

#ps -f | python getProcess.py



#source <(grep = logs/flavUNIX_2017-05-21_14:27:07.ini | sed 's/ *= */=/g') 


host=$(hostname)
proc=$(ps -f)

echo "[USER]" >> "logs/flavUNIX_2017-05-21_14:27:12.ini"
echo "user = $host" >> "logs/flavUNIX_2017-05-21_14:27:12.ini"

echo ""
echo "[PROCESS]" >>
echo ""