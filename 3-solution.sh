
# inputfile="$1"

# omg=$(grep -Eo 'mul\(([0-9]){1,3},([0-9]){1,3}\)' "$inputfile" | sed -E 's/mul\(([0-9]{1,3}),([0-9]{1,3})\)/\1*\2/g')

# omg=$(echo "$omg" | tr ' ' '+')

# output=$((omg))

# echo $output



#!/bin/bash

# Part 1
# cat 3-input.txt | grep -oE "mul\\(\d+,\d+\\)" | grep -oE '\d+,\d+' | awk -F, '{ sum += $1 * $2 } END { print sum }'

# Part 2
cat 3-input.txt | grep -oE "mul\\((\d+),(\d+)\\)|do\(\)|don't\(\)" | sed 's/mul//g' | sed 's/(\|)//g' | sed 's/,/ /g' > /tmp/what.txt
cat /tmp/what.txt | awk -v flag=1 -v sum=0 '{ if ($1 == "do") { flag=1 } else if ($1 == "don'\''t") { flag=0 } else { if (flag == 1) {sum += $1 * $2} } } END { print sum }'
