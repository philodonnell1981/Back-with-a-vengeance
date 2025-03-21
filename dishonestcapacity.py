# a program that shows how misleading flash memory
# manufacturers are about the advertised capacities
# of their products

print('Enter TB or GB for the advertised unit:')
unit = input('>')

#Calculate the amount that the advertised capacity lies
if unit == 'TB' or unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    discrepancy = 1000000000 / 1073741824

print('Enter the advertised capacity:')
adv_cap = input('>')
adv_cap = float(adv_cap)

#Calculate the real capacity and round it to the nearest hundredths
#and convert it to a string si it can be concatenated
real_cap = str(round(adv_cap * discrepancy, 2))

print('The actual capacity is ' + real_cap + ' ' + unit)
