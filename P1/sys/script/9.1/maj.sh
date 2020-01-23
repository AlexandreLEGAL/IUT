#/!bin/bash
cat $1
touch MAJ.txt
tr abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ  < $1 > MAJ.txt
