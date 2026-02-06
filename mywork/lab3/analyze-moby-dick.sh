#!/bin/bash
SEARCH_PATTERN="$1"
OUTPUT="$2"

if [ -z "$OUTPUT" ]; then
  OUTPUT="results.txt"
fi

if [ -e "$OUTPUT"]; then
   echo "Output file already exists."
   exit 1
fi

curl https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt > mobydick.txt
OCCURRENCES=$(grep -oi "$SEARCH_PATTERN" mobydick.txt | wc -l)

{
  echo "The search pattern \"$SEARCH_PATTERN\" was found $OCCURRENCES time(s)."
} > "$OUTPUT"
