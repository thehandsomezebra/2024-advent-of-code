#!/bin/bash 

if [[ $1 == "" ]]; then
    DATA="/app/inputs/2-input.txt"
# elif [[ $1 == "test" ]]; then
#     DATA="/app/inputs/day-2-example"
else
    DATA=$1  
fi

TOTAL=0
while read -u 3 -r report ; do 
    SAFE=1
    DIRECTION=0
    START=1
    n=0
    nn=0
    for level in $report; do
        if [[ $START -eq 1 ]]; then
            n=$level
            START=0
            continue
        fi
        
        
        nn="$n"
        n="$level"
        
        DIFF=$(( nn - n ))
        if [[ $DIRECTION -eq 0 ]]; then
            if [[ DIFF -lt 0 ]]; then
                DIRECTION=-1
            elif [[ DIFF -gt 0 ]]; then
                DIRECTION=1
            fi
        elif [[ $DIRECTION -eq -1 ]] && [[ DIFF -gt 0 ]]; then
            ERR="DIRECTION CHANGED"
            SAFE=0
        elif [[ $DIRECTION -eq 1 ]] && [[ DIFF -lt 0 ]]; then
            ERR="DIRECTION CHANGED"
            SAFE=0
        fi

        DIFF="${DIFF#-}"
        if [[ $DIFF -eq 0 ]] || [[ $DIFF -gt 3 ]]; then
            ERR="Out of range ${DIFF}"
            SAFE=0
        fi
    done
    if [[ $SAFE -eq 1 ]]; then
        TOTAL=$((TOTAL + 1))
    fi
done 3< $DATA


echo "Advent of Code 2024 Day 2a Solution...."
echo "+-----------------------------------+"
echo "|     Total Safe Reports: $TOTAL       |"
echo "+-----------------------------------+"

if [[ $TOTAL -eq 0 ]]; then
    exit 1
fi





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
