#!/bin/bash
$d = 'date +%y%m%d%H%M%S'

git add .
git config user.name "mincaeuro"
git config user.email "mincaeuro@gmail.com"
git commit -m "update"$d""
git push
