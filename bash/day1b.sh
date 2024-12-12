#!/bin/bash
if [[ $1 == "" ]]; then
    file="/app/inputs/1-input.txt"
# elif [[ $1 == "test" ]]; then
#     DATA="../../data/day-2-example"
else
    file=$1  
fi
#see solution 1a for explanation on this
sort $file | awk '{ print $1 }' > /tmp/left
sort -k 2 $file | awk '{ print $2 }' > /tmp/right

TOTAL=0

for number in $(cat /tmp/left); do #for each number in the left file
    n=$(grep -c $number /tmp/right) #count how many times it appears in the right file
    TOTAL=$((TOTAL + number * n)) #add the number times the count to the total to get the similarity score
done


echo "Advent of Code 2024 Day 1b Solution...."
echo "+-----------------------------------+"
echo "|       Similarity Score: $TOTAL  |"
echo "+-----------------------------------+"
