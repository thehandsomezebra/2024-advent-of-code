#!/usr/bin/env bash


if [[ $1 == "" ]]; then
    DATA="/app/inputs/4-input.txt"
# elif [[ $1 == "test" ]]; then
#     DATA="/app/inputs/day-4-example"
else
    DATA=$1
fi

    mapfile -t lines < "$DATA"
    w="${#lines[0]}"

    for (( y = 1; y < ${#lines[@]} - 1; y++ )); do
        for (( x = 1; x < w - 1; x++ )); do
            [[ "${lines[y]:x:1}" != "A" ]] && continue

            above="${lines[y-1]:x-1:1}${lines[y-1]:x+1:1}"
            below="${lines[y+1]:x-1:1}${lines[y+1]:x+1:1}"

            [[ "${above}${below}" =~ (MMSS|SSMM|MSMS|SMSM) ]] || continue
            (( count++ ))
        done
    done



echo "Advent of Code 2024 Day 4b Solution...."
echo "+-----------------------------------+"
echo "|        Total Times: $count          |"
echo "+-----------------------------------+"
