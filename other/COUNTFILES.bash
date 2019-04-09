#!/bin/bash

find . -mindepth 3 -type f   |  # list files starting from depth 3
awk '!/\.git\// && !/\.gif/' |  # ignore .git/* and *.gif
sed 's/^.*\.//'              |  # remove everything before the '.' (inclusive)
uniq -c                      |  # count repeated lines
sort -nr                        # sort in descending order
