#Retail company validation
# Defining the function which will calculate the profit
def calculate_profit(total_sales, total_cost):
    # calculate profit by subtracting total cost from total sales
    profit = total_sales - total_cost
    # return the profit
    return profit
#initialize the variable which will store the total profit
total_profit = 0
# call the function to calculate the profit for electronics category
profit_electronics = calculate_profit(20000, 15000)
# add the profit for electronics category to the total profit
total_profit += profit_electronics
# call the function to calculate the profit for clothing category
profit_clothing = calculate_profit(30000, 25000)
# add the profit for clothing category to the total profit
total_profit += profit_clothing
# call the function to calculate the profit for home goods category
profit_home_goods = calculate_profit(40000, 35000)
# add the profit for home goods category to the total profit
total_profit += profit_home_goods
# print the total profit
print("Total profit for the year: $" + str(total_profit))
# calculate profit percentage for electronics category
profit_percentage_electronics = (profit_electronics/20000)*100
# calculate profit percentage for clothing category
profit_percentage_clothing = (profit_clothing/30000)*100

# calculate profit percentage for home goods category
profit_percentage_home_goods = (profit_home_goods/40000)*100
# print the profit percentage for each category
print("Profit percentage by category:")
print("Electronics: " + str(profit_percentage_electronics) + "%")
print("Clothing: " + str(profit_percentage_clothing) + "%")
print("Home goods: " + str(profit_percentage_home_goods) + "%")
