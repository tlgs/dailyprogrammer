# 31/12/2016

wordRank <- function(input){
    sums <- numeric(length(input))

    for(i in 1:length(input)) {
        for (j in 1:nchar(input[i])){
            sums[i] <- sums[i] + which(letters == tolower(substr(input[i], j, j)),
                                       arr.ind = TRUE)
        }
        sums[i] <- sums[i] / nchar(input[i])
    }

    input[order(sums)]
}
