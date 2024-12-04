#!/bin/bash

safe_count=0

while read -r line; do

checkLine() {
  local line="$1"
  local prev=""
  local trend=""
  local is_safe=1

  echo "############################################"
  echo "Line: $line"
  # is_safe=1  # Assume the report is safe initially
  # prev=""
  # trend=""
  # Iterate over the numbers on the line

  for curr in $line; do
    echo "------------------------"
    echo "Previous: $prev"
    echo "Current: $curr"
    if [[ -n "$prev" ]]; then
      diff=$((curr - prev))

      echo "DIFF CHECK Diff: $diff"
      #check diff safe
      # if ((diff > 0 && diff < 4)); then
      if ((((diff > 0 ? diff : -diff) > 0) && ((diff > 0 ? diff : -diff) < 4))); then

        echo "Diff check passed; seems safe so far"
      else
        is_safe=0
        echo "NOT SAFE DUE TO RULE:"
        echo "   Any two adjacent levels differ by at least one and at most three."
        echo "   Previous: $prev"
        echo "   Current: $curr"
        echo "   Diff: $diff"
        break
      fi

      # Check trend safe
      if [[ -z "$trend" ]]; then # First comparison happens at third number, as diff will be available
        if ((diff > 0)); then
          trend="increasing"
          echo "Initial trend set as increasing"
        elif ((diff < 0)); then
          trend="decreasing"
          echo "Initial trend set as decreasing"
        fi
      else
        echo "TREND CHECK! We were marked as $trend"
        if [[ "$trend" == "increasing" && diff -lt 0 ]]; then
          echo "We were increasing, now we're decreasing!!"
          is_safe=0
          echo "NOT SAFE DUE TO RULE:"
          echo "   The levels are either all increasing or all decreasing."
          echo "    DIFF: $diff"
          break
        elif [[ "$trend" == "decreasing" && diff -gt 0 ]]; then
          echo "We were decreasing, now we're increasing!!"
          is_safe=0
          echo "NOT SAFE DUE TO RULE:"
          echo "   The levels are either all increasing or all decreasing."
          echo "    DIFF: $diff"
          break
        fi
      fi
    fi

    prev=$curr
    # echo "determined safe?!: $is_safe"
  done

  return $is_safe
}

# line="1 2 3 4 5" #increasing, safe
# line="80 82 84 86 88" #increasing, safe
# line="88 86 84 82 80" #decreasing by 2, safe
# line="5 4 3 2 1" #decreasing by 2, safe
# line="100 103 106 109 112" #increasing by 3, safe
# line="100 97 94 91 88" #decreasing by 3, safe
# line="40 44 48 52 56" #increasing by 4, NOT safe
# line="40 36 32 28 24" #decreasing by 4, NOT safe
# line="37 38 39 40 41 42 40 39 38" #increasing then decreasing, NOT safe
# line="42 41 40 39 38 40 41" #decreasing then increasing, NOT safe

checkLine "$line"
# echo "FINAL SAFETY CHECK RESULT: $?"
is_safe=$?
# echo "############################################"

((is_safe)) && ((safe_count++))
done < 2-input.txt

echo "Advent of Code 2024 Day 2a Solution...."
echo "+-----------------------------------+"
echo "|    Safe Reports: $safe_count       |"
echo "+-----------------------------------+"
