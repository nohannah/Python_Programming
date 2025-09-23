cost =float( input("Enter the meal cost :"))
tip = float(input("Enter the tip percentage you want to give :"))
tip_amount = (tip/100) * cost
print ("The tip amount is :$ ",(f"{tip_amount:.2f}") )