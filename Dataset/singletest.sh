#!/bin/bash
COUNTER=1
while [  $COUNTER -lt 101 ];
do

	python distribution.py train/data0.train $COUNTER
	let COUNTER=COUNTER+1
done

COUNTER=1
while [  $COUNTER -lt 101 ];
do	
	python mutate_test_multiple.py 1 train/data0.addattr$COUNTER test/data0.test newtest/data0.addattr$COUNTER
	echo data0result.addattr$COUNTER >> newtestresult/"log"
	svm-predict newtest/data0.addattr$COUNTER model/data0.train.model newtestresult/data0result.addattr$COUNTER >> newtestresult/"log"

	let COUNTER=COUNTER+1
done

COUNTER=1
while [  $COUNTER -lt 101 ];
do	
	python mutate_test_multiple.py 0 train/data0.subattr$COUNTER test/data0.test newtest/data0.subattr$COUNTER
	echo data0result.subattr$COUNTER >> newtestresult/"log"
	svm-predict newtest/data0.subattr$COUNTER model/data0.train.model newtestresult/data0result.subattr$COUNTER >> newtestresult/"log"

	let COUNTER=COUNTER+1
done