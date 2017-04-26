# 26/04/2017
library(combinat)

next_biggest_int <- function(n){
    p<- combinat::permn(unlist(strsplit(as.character(n), "")))
    p <- sort(as.numeric(sapply(p, paste, collapse="")))
    p[which(p > n)[1]]
}