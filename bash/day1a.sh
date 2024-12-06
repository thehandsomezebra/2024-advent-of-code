#!/bin/bash

# So we're gunna use sort with -k to specify the field to sort on..
#By default, it sorts from the beginning of the line, but we can specify a field to sort on with -k.

#Then we'll just use awk to dump what we need into a file that we'll read from laterz

if [[ $1 == "" ]]; then
    file="/app/inputs/1-input.txt"
# elif [[ $1 == "test" ]]; then
#     DATA="../../data/day-2-example"
else
    file=$1  
fi

sort $file | awk '{ print $1 }' > /tmp/left
sort -k 2 $file | awk '{ print $2 }' > /tmp/right

TOTAL=0

# load in the files as file descriptors 3 and 4 to use with the While statement
while read -u 3 -r left \
   && read -u 4 -r right ;\
  do 
    diff="$((left - right))" #get the difference
    if [[ $diff -lt 1 ]]; then 
        diff="$(( diff * -1))" #clean up the negative numbers..only positive guys here lol
    fi
    TOTAL="$((TOTAL + diff))"
done 3</tmp/left 4</tmp/right  #remember line 13? dis how we input it.

echo "Advent of Code 2024 Day 1a Solution...."
echo "+-----------------------------------+"
echo "|       Total Difference: $TOTAL   |"
echo "+-----------------------------------+"
