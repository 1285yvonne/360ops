#! /bin/bash

set var
eval $(ifconfig | awk -f 2.awk)
echo ${var}
