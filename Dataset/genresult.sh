#!/bin/bash
#usage: bash genresult.sh [foldername]

testdir=$1
resultdir=$testdir"result"
rm -rf $resultdir
mkdir $resultdir
echo "OUTPUT: "$resultdir

cd $testdir
for item in *;
do
	#get "dataX"
	echo $item
	cut1=(`echo $item | awk -F'.' '{print $1}'`)
	cut2=(`echo $cut1 | awk -F'_' '{print $1}'`)
	datafile=${cut2[0]}
	#echo ${cut2[0]}

	#svm-predict 
	svm-predict $item ../model/$datafile".train.model" ../$resultdir/$cut1".result" >> ../$resultdir/"log"
done
