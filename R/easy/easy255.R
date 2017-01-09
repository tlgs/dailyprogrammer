#09/01/2017

countBulbs <- function(input){
    input <- as.numeric(unlist(strsplit(input, "[ \n]")))
    bulbs <- array(FALSE, input[1])
    for (i in seq(2,length(input),2)){
        a <- seq(min(input[i], input[i+1]), max(input[i], input[i+1])) + 1
        bulbs[a] <- !bulbs[a]
    }
    sum(bulbs, na.rm = TRUE)
}