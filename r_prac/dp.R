y <- data.frame(a=1,b=2)
dput(y,file="y.R")
new.y <- dget("y.R")
