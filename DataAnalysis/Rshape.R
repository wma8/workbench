# Create vector objects.
city <- c("Tampa", "Seattle", "Hartford", "Denver")
state <- c("FL", "WA", "CT", "CO")
zipcode <- c(33602, 98104, 06161, 80294)

# Combine above three vectors into one data frame.
addresses <- cbind(city, state, zipcode)

# Print a header
cat("Data frame example")

# Print the data frame.
print(addresses)

# Create another data frame with similar columns
new.address <- data.frame(
    city = c("Lowry","Charlotte"),
   state = c("CO","FL"),
   zipcode = c("80230","33949"),
   stringsAsFactors = FALSE
)

print(new.address)

# Combine rows form both the data frames.
all.addresses <- rbind(addresses, new.address)

cat("The combined example")
print(all.addresses)


