#!/usr/bin/sh
 
for d in `find . -type d -name "aws*"`
do
    ( cd $d && pwd )
done