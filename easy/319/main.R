# 15/06/2017

condense <- function(string){
    gsub("(\\w+)\\s\\1", "\\1", string)
}