#!/bin/bash

OUTPUT="hh_positions.csv"
INPUT="../ex02/hh_sorted.csv"

head -n 1 "$INPUT" > "$OUTPUT"
tail -n +2 "$INPUT"  | awk -F ',' 'BEGIN { OFS="," } {
    position = ""
    if ($3 ~ /Junior/) position = "Junior"
    if ($3 ~ /Middle/) position = (position == "" ? "Middle" : position "/Middle")
    if ($3 ~ /Senior/) position = (position == "" ? "Senior" : position "/Senior")
    if (position == "") position = "-"  # Если нет Junior/Middle/Senior, ставим "-"
    $3 = "\"" position "\""  # Заменяем 3-й столбец на найденное значение
    print $0
}' > "$OUTPUT"