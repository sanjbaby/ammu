number_of_pizza = eval(input("how many pizzas"))
cost_of_each_pizza = eval(input("cost of each pizza"))
subtotal = number_of_pizza * cost_of_each_pizza
tax_rate = 0.08
sales_tax = tax_rate*subtotal
final_total = subtotal + sales_tax
print("the total cost is",final_total)
print("this includes the sales tax plus subtotal which is",subtotal,sales_tax)







