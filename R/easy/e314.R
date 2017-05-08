# 08/05/2017
library(combinat)

int_concat <- function(v){
    p <- combinat::permn(v)
    p <- sort(as.numeric(sapply(p, paste, collapse="")))
    result <- p[p > 10**(nchar(paste(v, collapse=""))-1)]
    c(result[1], result[length(result)])
}