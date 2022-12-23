#!/bin/bash

change() {
  remainder=$1
  total=0

  for coin in 500 100 25 10 5 1; do
    total=$((total + remainder / coin))
    remainder=$((remainder % coin))
  done

  echo $total
}
