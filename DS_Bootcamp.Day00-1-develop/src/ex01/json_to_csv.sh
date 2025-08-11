#!/bin/bash

INPUT_JSON="../ex00/hh.json"  
OUTPUT_CSV="hh.csv"
if [ ! -f "$INPUT_JSON" ]; then
    echo "Ошибка: файл $INPUT_JSON не найден!"
    exit 1
fi
echo '"id", "created_at", "name", "has_test", "alternate_url"' > "$OUTPUT_CSV"
jq -r -f filter.jq "$INPUT_JSON" >> "$OUTPUT_CSV"