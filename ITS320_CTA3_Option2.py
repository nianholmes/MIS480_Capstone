#Create dictionary through function with range of values
def tax_rates(x):           
    return {0<=x<=499:'10%', 500<=x<=1499:'15%', 1500<=x<=2499:'20%', 2500<=x:'30%'}[1]

#Gather weekly income from user
x = int(input('Please input weekly income: ')) 

#Locate tax rate from dictionary
final_tax = tax_rates(x)

#Calculate annual income
annual_income = int(x * 52) 

#Calculate the tax owed based on tax rate and weekly income
if final_tax == '10%':      
    tax_owed = int(x * .1)
elif final_tax == '15%':
    tax_owed = int(x * .15)
elif final_tax == '20%':
    tax_owed = int(x * .2)
elif final_tax == '30%':
    tax_owed = int(x * .3)

#Display results
print('Your income is: $', x, 'per week, or $',annual_income, 'per year.')
print('Your tax rate is:', final_tax)     
print('Your taxes owed are: $', tax_owed, 'per week, or $',int(tax_owed*52), 'per year.')    

