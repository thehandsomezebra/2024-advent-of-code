
#!/bin/bash

# Part 2
if [[ $1 == "" ]]; then
    DATA="/app/inputs/3-input.txt"
# elif [[ $1 == "test" ]]; then
#     DATA="/app/inputs/day-3-example"
else
    DATA=$1  
fi

cat $DATA | grep -oP "mul\\((\d+),(\d+)\\)|do\(\)|don't\(\)" | sed 's/mul//g' | sed 's/(\|)//g' | sed 's/,/ /g' > /tmp/omg.txt
TOTAL=$(cat /tmp/omg.txt | awk -v flag=1 -v sum=0 '{ if ($1 == "do") { flag=1 } else if ($1 == "don'\''t") { flag=0 } else { if (flag == 1) {sum += $1 * $2} } } END { print sum }')


echo "Advent of Code 2024 Day 3b Solution...."
echo "+-----------------------------------+"
echo "|        Total: $TOTAL           |"
echo "+-----------------------------------+"
