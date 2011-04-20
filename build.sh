#!/bin/bash
find . -name "*.pyc" -exec rm '{}' ';'
rm dist/expense.zip
rm dist/expense.tar.gz
mv src expense
tar -pczf dist/expense.tar.gz   --exclude=".*" --exclude="/.*" --exclude="/*/.*" --exclude="*.pyc" ./expense
mv expense/expense expense/expense.py
zip -r dist/expense.zip expense/[!\.]* -x \*/\.*
mv expense/expense.py expense/expense
mv expense src