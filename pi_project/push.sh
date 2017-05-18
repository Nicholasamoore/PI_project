#!/bin/bash

MESSAGE="Pushing /test/"

git add pi_project/test/
git commit -m "pushing /test/"
echo $MESSAGE

git push origin master

