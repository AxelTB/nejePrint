#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Usage:"
    echo " nejePrint.sh SERIALDEVICE IMAGE [BURNINGTIME]"
    exit
fi

if [ "$#" -eq 3 ]; then
   btime=`echo "obase=16; $3" | bc`
else
   btime=20
fi

#echo $btime
#echo -e "\x$btime"


actualsize=$(wc -c <"$2")

if [ $actualsize -ne 32830 ]; then
    echo "Image must be 512x512 BMP 1 bit color depth"
   exit
fi


echo setting port...
stty 57600 min 1 line 0 time 0 -brkint -icrnl ixoff -imaxbel -opost -onlcr -opost -onlcr -isig -icanon -echo -echoe  < $1
sleep 1
#stty < $1
#read -p "Press Enter to continue"
echo a > ./rep.tmp
echo Handshake...
 #read -n 2 rep < $1 & echo -e '\xF6' > $1
dd of=rep.tmp if=$1 bs=2 count=1 status=noxfer &
echo -e '\xF6' > $1
sleep 2
if [ "`cat ./rep.tmp`" = "ep" ]; then
  echo "Done"
else
  echo "Handshake Failed (Error 0):"
  stty < $1
  exit
fi

echo Sending Image
echo -e '\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE' >$1
sleep 3
cat $2 > $1
echo done
sleep 1

echo home
echo -e '\xF3' > $1
sleep 5

echo Burning Time 0x$btime
echo -e '\x$btime' > $1

read -p "Press Enter to Preview"
echo -e '\xF4' > $1


echo "Press Button on the printer to print"
