# example to calculate sales tax in different provinces
# include Non Canadian residents don't pay sales tax

country = input('What country do you live in?')
province = input('What province do you live in?')
tax = 0

if country.lower() == 'canada':
    if province in('Alberta','Nunavut', 'Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0
print(tax)