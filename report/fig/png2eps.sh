#!/bin/bash

for f in *.png
do
	echo $f
	filename="${f%%.*}"
	echo $filename
	convert $f -background white -alpha remove $filename.eps
done