no_of_boys = int(input("Enter the number of boys: "))
no_of_girls = int(input("Enter the number of boys: "))
print("Boys: " + str(round(no_of_boys*100/(no_of_boys+no_of_girls))) + "%")
print("Girls: ", str(round(no_of_girls*100/(no_of_boys+no_of_girls))) + "%")
