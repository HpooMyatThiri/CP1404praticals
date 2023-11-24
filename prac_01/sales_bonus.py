"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""

'''
get sales_value
while sales_value >= 0
    if sales_value < 1000
        bonus = sales_value * 0.1
    else 
        bonus = sales_value * 0.15
    display bonus 
    get sales_value
display "Thank you for using!!"
'''


sales_value = float(input("Enter sales: $"))
while sales_value >= 0:
    if sales_value < 1000:
        bonus = sales_value * 0.1
    else:
        bonus = sales_value * 0.15
    print("Bonus is $",bonus)
    sales_value = float(input("Enter sales: $"))
print("Thank you for using!!")
