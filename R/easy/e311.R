# 18/04/2017

jollyJumper <- function(arr){
    x <- ifelse(all(sort(abs(arr[-c(1, arr[1]+1)] - arr[-(1:2)])) == 1:(arr[1]-1)), "JOLLY", "NOT JOLLY")
    x
}