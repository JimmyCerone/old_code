import requests

import json

Url = 'https://taxrates.api.avalara.com/address'

key = '38JakZZeFpYb4FMntvtnaZdErBQvsH8vuaBQ7MHds8ApypIaoFcJM6jXuxTx0RmxD+4SrXWmTTSHgzdVjXrQcw=='

street = raw_input("What is your street address? ")

state = raw_input("\nWhat state do you reside in? \nBoth two letter code and full name are acceptable. ")

city = raw_input("\nWhat city do you live in? ")

postal = raw_input("\nWhat is your zip/postal code? ")

country = 'usa'

response = requests.get(Url, params={'apikey': key, 'street': street, 'city': city, 'state': state, 'country': country, 'postal': postal })

tax_rate = json.loads(response.content)['totalRate']

tax_rate = (tax_rate / 100) + 1

total_price = 0.0

savings = 0.0

count = 0

next_item = raw_input('\nWould you like to begin (Yes/No)? ')

while next_item == 'Yes':
    
    if count == 0:        
        
        item_name = raw_input("\nWhat is the name of your first item? ")
        
    else:
        item_name = raw_input("\nWhat is the name of the next item? ")

    taxable = str(raw_input("\nIs " + item_name + " taxable (Yes/No)? "))
    
    item_price = float(raw_input('\nHow much does ' + item_name + ' cost? '))

    #Just a thought/musing. How would you be able to accomodate a percent for the discount?
    #What about accounting for the difference between 40% off and 40% of original price?
    
    discount = float(raw_input('\nWhat is the discount for ' + item_name + '? '))
    
    if taxable == 'No':
        total_price = item_price + total_price
    else:
        total_price = (item_price - discount) * tax_rate + total_price
    
    savings = (discount * tax_rate) + savings
    
    #I acknowledge this formula looks quite weird. But I'm taking into account the fact that since the discount is applied before tax, it saves you the raw discount amount plus the tax rate you would have payed on that discount....
    #So this formula is your true savings, not just the raw amount off. 
    
    next_item = str(raw_input('\nMore items? (Yes/No)? '))
    
    count = count + 1
    
print "\nYou purchased %i items for a total price of $%6.2f." % (count, total_price)

print "\nYou saved $%6.2f via coupons." % (savings)