#!/bin/bash

INPUT="../ex03/hh_positions.csv"

tail -n +2 "$INPUT" | cut -d ',' -f 2 | cut -d 'T' -f 1 | sort | uniq | while read -r date; do
     clean_date=$(echo "$date" | tr -d '"')
    {
        head -n 1 "$INPUT"
        grep "$date" "$INPUT"
    } > $clean_date.csv 
done