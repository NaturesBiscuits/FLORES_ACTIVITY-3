print("Sales Tax Calculator")
amount = float(input("Enter purchase amount: "))

tax = amount * 0.06

print("\nAmount:",amount,"\nSales Tax:","{:.2f}".format(tax))
