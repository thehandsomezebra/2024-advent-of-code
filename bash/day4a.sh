#!/usr/bin/env bash

if [[ $1 == "" ]]; then
    DATA="/app/inputs/4-input.txt"
# elif [[ $1 == "test" ]]; then
#     DATA="/app/inputs/day-4-example"
else
    DATA=$1
fi

mapfile -t lines <$DATA
w="${#lines[0]}"

for ((y = 0; y < ${#lines[@]}; y++)); do
    for ((x = 0; x < w; x++)); do
        [[ "${lines[y]:x:1}" != "X" ]] && continue

        # EAST
        if ((x <= w - 3)); then
            [[ "${lines[y]:x:4}" == "XMAS" ]] && ((count++))
        fi

        # WEST
        if ((x >= 3)); then
            [[ "${lines[y]:x-3:4}" == "SAMX" ]] && ((count++))
        fi

        # NORTH
        if ((y >= 3)); then
            word="${lines[y]:x:1}${lines[y - 1]:x:1}${lines[y - 2]:x:1}${lines[y - 3]:x:1}"
            [[ "${word}" == "XMAS" ]] && ((count++))
        fi

        # SOUTH
        if ((y <= ${#lines[@]} - 3)); then
            word="${lines[y]:x:1}${lines[y + 1]:x:1}${lines[y + 2]:x:1}${lines[y + 3]:x:1}"
            [[ "${word}" == "XMAS" ]] && ((count++))
        fi

        # NE
        if ((x <= w - 3 && y >= 3)); then
            word="${lines[y]:x:1}${lines[y - 1]:x+1:1}${lines[y - 2]:x+2:1}${lines[y - 3]:x+3:1}"
            [[ "${word}" == "XMAS" ]] && ((count++))
        fi

        # NW
        if ((x >= 3 && y >= 3)); then
            word="${lines[y]:x:1}${lines[y - 1]:x-1:1}${lines[y - 2]:x-2:1}${lines[y - 3]:x-3:1}"
            [[ "${word}" == "XMAS" ]] && ((count++))
        fi

        # SE
        if ((y <= ${#lines[@]} - 3 && x <= w - 3)); then
            word="${lines[y]:x:1}${lines[y + 1]:x+1:1}${lines[y + 2]:x+2:1}${lines[y + 3]:x+3:1}"
            [[ "${word}" == "XMAS" ]] && ((count++))
        fi

        # SW
        if ((y <= ${#lines[@]} - 3 && x >= 3)); then
            word="${lines[y]:x:1}${lines[y + 1]:x-1:1}${lines[y + 2]:x-2:1}${lines[y + 3]:x-3:1}"
            [[ "${word}" == "XMAS" ]] && ((count++))
        fi
    done
done

echo "Advent of Code 2024 Day 4a Solution...."
echo "+-----------------------------------+"
echo "|        Total Times: $count          |"
echo "+-----------------------------------+"
