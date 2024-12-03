#!/bin/bash

safe_count=0

while read -r line; do
  echo "############################################"
  echo "Line: $line"
  is_safe=1  # Assume the report is safe initially
  prev=""
  trend="" 
  # Iterate over the numbers on the line

 
  for curr in $line; do
  echo "------------------------"
  echo "Current: $curr"
  echo "Previous: $prev"
    if [[ -n "$prev" ]]; then
      diff=$((curr - prev))

#check diff safe
      if ((diff < 1 || diff > 3)); then
        is_safe=1
        echo "seems safe"
        # break
    else
        is_safe=0
        echo "NOT SAFE"
        # break
      fi


# Check trend safe
      if [[ -z "$trend" ]]; then  # First comparison
        if ((diff > 0)); then
          trend="increasing"
          echo "trend set as increasing"
        elif ((diff < 0)); then
          trend="decreasing"
          echo "trend set as decreasing"
        else
          is_safe=0
          echo "what did you do ray?"
          break  # Not strictly increasing or decreasing
        fi
      elif
      # NEED TO SET NEW VAR $ptrend for previous trend.. then check if different
      

        #    [[ "$trend" == "increasing" && diff < 0 ]] || \
        #    [[ "$trend" == "decreasing" && diff > 0 ]]; then
        is_safe=0
        echo "trend changed - NO LONGER SAFE"
        break  # Trend changed
      fi
    fi



    prev=$curr
    echo "determined safe?!: $is_safe"
  done

  ((is_safe)) && ((safe_count++)) 
done < 2-testinput1.txt

echo "Advent of Code 2024 Day 2a Solution...."
echo "+-----------------------------------+"
echo "|    Safe Reports: $safe_count       |"
echo "+-----------------------------------+"
