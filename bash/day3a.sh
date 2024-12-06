
#!/bin/bash

# Part 1

if [[ $1 == "" ]]; then
    DATA="/app/inputs/3-input.txt"
# elif [[ $1 == "test" ]]; then
#     DATA="/app/inputs/day-3-example"
else
    DATA=$1  
fi

TOTAL=$(cat $DATA | grep -oP "mul\\(\d+,\d+\\)" | grep -oP '\d+,\d+' | awk -F, '{ sum += $1 * $2 } END { print sum }')
# Use -P to enable Perl-compatible regex.. this is in the ubuntu image now that I containerized it
# use -E to enable extended regex.. this is available in my mac

echo "Advent of Code 2024 Day 3a Solution...."
echo "+-----------------------------------+"
echo "|        Total: $TOTAL           |"
echo "+-----------------------------------+"
