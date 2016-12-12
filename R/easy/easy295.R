strSwitch <- function(a, b){
    print(a, quote=FALSE)
    a <- unlist(strsplit(a, split=""))
    b <- unlist(strsplit(b, split=""))
    for(i in 1:length(a)){
        if(a[i] != b[i]){
            a[i] <- b[i]
            print(paste(a, collapse=""), quote = FALSE)
        }
    }
}