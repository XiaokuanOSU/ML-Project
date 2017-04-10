#!/bin/bash

cd model

for item in ../train/*;
do
	svm-train $item
	echo $item
done