#!/bin/bash

lettersum() {
  t=0
  [ -n "$1" ] && while read n; do
    t=$((t + n - 96))
  done <<<"$(echo -n "$1" | od -v -An -tuC -w1)"

  echo $t
}

echo 'lettersum("") =>' "$(lettersum '')"
echo 'lettersum("a") =>' "$(lettersum 'a')"
echo 'lettersum("z") =>' "$(lettersum 'z')"
echo 'lettersum("cab") =>' "$(lettersum 'cab')"
echo 'lettersum("excellent")' "$(lettersum 'excellent')"
echo 'lettersum("microspectrophotometries") =>' "$(lettersum 'microspectrophotometries')"
