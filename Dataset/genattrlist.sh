#!/bin/bash

rm train/*.addattr train/*.subattr

for item in train/*;
do
	echo $item
	python distribution.py $item $1
done