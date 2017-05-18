#!/bin/bash

# sync with repo git@github.com:ACC-COSC2325-001-SP17/groupproject1-team-alpha.git
git pull

# run record for length seconds else record 5 seconds
if [[ -n "$1" ]]; then
	length=$1
else
	length=5
fi

# record for length seconds
python3 "record wav/record.py" $length

# define message to echo
MESSAGE="pushing wav file to transcribe"

# we only want to update whats going up to test directory
git add pi_project/test/
git commit -m "added wav file to transcribe"
echo $MESSAGE
git push origin master
