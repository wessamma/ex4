# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn




############    Task 1     ########################


'''

c = 3
while c > 0 :

       n1 = int(input('Enter first number :'))
       n2 = int(input('Enter second number :'))

       if n1 == n2 :
        print (' Number are equal')
       else :
        print ('Numbers are not equal')

       if n2 > n1 :
        print ('Second number is greater than first number')
       else :
        if n2 >= n1 :
         print ('second number is greater than or equal to  first number')

       if n1 > 1000 and n2 > 1000 :
        print ('both numbers are big')
        Big_number = 1
        print ('big_numbers is set to  True')
       elif n1 < 1000 or n2 < 1000 :
        print ('both numbers are not big')
        Big_number = 0
        print ('big_numbers is set to  False')

        c-=1

       
'''



###############     Task 2   ##########################



list_of_months = ['January','February' ,'March', 'May', 'July', 'August', 'October', 'December','April',  'June',  'September', 'November']
list_of_31_days_months = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
list_of_30_days_months = ['April',  'June',  'September', 'November']

print ('List of months: ',list_of_31_days_months)

c = 3
while c > 0 :

 month = input ('Input the name of Month:')
 if month in list_of_months :
    break 
 else :
    print (' tray again')
 c-=1

if c == 0 :
    print ('wrong')
else :
    if month in list_of_31_days_months :
        print ('Number of days: 31 days')

    elif month in list_of_30_days_months : 
        print ('Number of days: 30 days')
    else :
        print ('Number of days: 28 or 29 days')

    

####################


