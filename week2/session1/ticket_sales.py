def total_sales(ticket_sales):
    total_sales = 0
    for i in ticket_sales.values():
        total_sales += i
    return total_sales

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))

# Plan
    # declare variable for total sales 
    # iterate through dict.values()
     # add each value to total sale