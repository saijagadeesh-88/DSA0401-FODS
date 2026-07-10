
sales <- matrix(c(100, 120, 130,
                  90, 110, 115,
                  150, 140, 135),
                nrow = 3, byrow = TRUE)

print("Sales Matrix:")
print(sales)
avg_price <- rowMeans(sales)

print("Average price of each product:")
print(avg_price)
overall_avg <- mean(avg_price)

cat("Overall Average Price:", overall_avg, "\n")
barplot(avg_price,
        main = "Average Price of Products",
        xlab = "Products",
        ylab = "Average Price",
        names.arg = c("Product 1", "Product 2", "Product 3"))

pie(avg_price,
    labels = c("Product 1", "Product 2", "Product 3"),
    main = "Average Price Distribution")



