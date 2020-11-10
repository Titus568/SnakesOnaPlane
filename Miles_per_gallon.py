

print ("The following will calculate the Miles Per Gallon of your vehicle.")
miles_driven=int(input("Enter miles driven "))
gas_used=int(input("Enter gallons of gas used "))
mpg=miles_driven/gas_used
print("Your miles per gallon (MPG) is", mpg)
if mpg>=30:
    print ("Your vehicle is pretty green.")
elif mpg>=25:
    print ("Your vehicle has a decent MPG but you could do better.")
elif mpg>=18:
    print ("Your vehicle has rather low MPG.")
else:
    print ("You may want to look at a more efficient vehicle.")