# 21/04/2017

isPangram <- function(s){
    x <- all(97:122 %in% sapply(tolower(s), utf8ToInt))
    x
}