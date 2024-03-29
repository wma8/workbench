if(FALSE) {
   "This is a demo for multi-line comments and it should be put inside either a single
      OR double quote"
}

myString <- "Hello World!"
print( myString )

# data type
v <- TRUE
print(class(v))
v <- 2L
print(class(v))
v <- 2+5i
print(class(v))

# Create a vector.
apple <- c('red', 'green', 'yellow')
print(apple)

# Create a list.
list1 <- list(c(2,5,3), 21.3, sin)
print(list1)

# Create a matrix.
M = matrix( c('a','a','b','c','b','a'), nrow = 2,
 ncol = 3, byrow = FALSE)
print(M)

# Create an array.
a <- array(c('green', 'yellow'), dim = c(3,3,2))
print(a)

# Create a vector
apple_colors <- c('green','green','yellow','red','red','red','green')

# Create a factor object.
factor_apple <- factor(apple_colors)

# Print the factor.
print(factor_apple)
print(nlevels(factor_apple))

# Create the data frame.
BMI <- data.frame(
    gender = c("Male", "Male", "Female"),
    heght = c(152, 171.5, 165),
    weight = c(81, 93, 78),
    Age = c(42, 38, 26)
)
print(BMI)



# Assignment Related
# Assignment using equal operator.
var.1 = c(0,1,2,3)           

# Assignment using leftward operator.
var.2 <- c("learn","R")   

# Assignment using rightward operator.   
c(TRUE,1) -> var.3           

print(var.1)
cat ("var.1 is ", var.1 ,"
")
cat ("var.2 is ", var.2 ,"
")
cat ("var.3 is ", var.3 ,"
")

var_x <- "Hello"
cat("The class of var_x is ",class(var_x),"
")

var_x <- 34.5
cat("  Now the class of var_x is ",class(var_x),"
")

var_x <- 27L
cat("   Next the class of var_x becomes ",class(var_x),"
")

print(ls())

# List the variables starting with the pattern "var".
print(ls(pattern = "var"))

# Variables with '.' is hidden, use the following method to find them
print(ls(all.names=TRUE))

# Use it to remove variables
rm(var.3)

# You can remove all the variables
rm(list = ls())


x <- switch(
    3, 
    "first",
    "second",
    "third",
    "fourth"
)
print(x)


common.compute <- function(x, type) {
    switch(type,
           mean = mean(x),
           median = median(x),
           sum = sum(x),
           max = max(x),
           min = min(x),
           sqrt = sqrt(x)
    )
}
x <- c(11, 23, 9, 49, 46, 92, 29, 33)
common.compute(x, "mean")

.libPaths()
library()
search()
install.packages("XML")

# Looping
v <- c("Hello", "loop")
cnt <- 2

# Repeat
repeat {
    print(v)
    cnt <- cnt+1

    if(cnt > 5){
        break
    }
}

# For loop
v <- LETTERS[1:4]
for (i in v){
    print(i)
}

# next ==> continue in java
for(i in v) {
    if(i == "B") {
        next
    }
    print(i)

}

