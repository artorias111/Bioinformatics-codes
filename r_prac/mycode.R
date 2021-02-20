myfunction <- function(){
    x <- rnorm(100)
    mean(x)
}

second <- function(x){
    x+rnorm(length(x))
}

x <- c(1,2,NA,4,NA,5)
bad <- is.na(x)
x[!bad]

#Vectorized computatations in R (This is a comment)