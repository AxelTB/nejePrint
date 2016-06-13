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
    echo "Image must be 520x520 BMP 1 bit color depth"
   exit
fi


echo setting port...
stty 57600 < $1
sleep 1
stty < $1
echo done

echo Handshake...
echo -e '\xF6' > $1
sleep 1
echo done

echo Sending
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
sleep 1

echo preview
echo -e '\xF4' > $1


echo All Done
