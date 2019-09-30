#Task12
#Compulsory_Task

#Building an investment calculator to calculate interest earned

import math

principal = float(input("Please enter in the amount you are depositing: ")) #This is the principal amount to be invested
interest_rate = (float(input("Type in the interest rate (as a %) [dont type in the '%' symbol]: "))/100) #Divided it by 100 to already get it to a decimal percentage format
years = int(input("Number of years to be invested: ")) #cast to int, assumed for the moment that we wouldnt do part years
interest_type = input("Enter the type of interest to be used [Either 'compound' or 'simple']: ") 

print("=====OUTCOME=====")
print("\nThe original investment amount was R",str(principal),", at a",str(interest_rate*100), "% interest rate, for ",str(years)," years.")  #Re-prints a summary of the inputs provided by user 
if interest_type == "compound":
    final_investment_value = principal* math.pow((1+interest_rate),years)    #This is the compond interest calculation; A will equal the total value of the investment after the investment period
elif interest_type == "simple":
    final_investment_value = principal*(1+interest_rate*years) # Simple interest calculation
else:
    print("You have not entered in the interest type correctly, please try again") # Runs if user entered interest type incorrectly

print("The value of the investment at the end of the period, using ", interest_type, " interest is: R", str(round(final_investment_value,2))) # Summary of final investment amount

