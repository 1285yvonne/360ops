#! /bin/bash


while [ 1 -eq 1 ]
do
    sleep 30s
    timetag=$(date +"[%D %R:%S]")
    filename=$(date +"%y-%m-%d")
    cpuinfo=$(vmstat 1 1 | sed -n "3p" | awk '{printf "us:%d\tsy:%d\tid:%d\twa:%d\tst:%d\t\n",$13,$14,$15,$16,$17}')
    echo $timetag $cpuinfo >> ${filename}.txt
done
