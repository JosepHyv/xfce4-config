#!/usr/bin/bash

curren_layout=$(setxkbmap -query | grep layout | awk '{print $2}')

if [ "$curren_layout" = "us" ]; then 
    setxkbmap es
else
    setxkbmap us
fi 


