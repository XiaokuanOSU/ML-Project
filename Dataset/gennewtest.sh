#!/bin/bash

bash genattrlist.sh $1

rm -rf newtestadd
mkdir newtestadd

python mutate_test_multiple.py train/data0.addattr test/data0.test newtest/data0.newtest