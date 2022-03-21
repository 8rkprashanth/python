import string
from xmlrpc.client import boolean
temp = int(input("enter the temperature value"))
value = boolean(input(('input the boolean value')))
print('value is ' + str(value))
if value == True :
    print('entered boolean value is true')
forecast ='rain'

if temp>90:
    print('this is too hot')
print("the temp is less than the "+str(temp))

temp_1=int(input('enter another temperature'))
if temp_1 == 25:
    print('it is cool day '+temp_1)
elif temp_1 <= 20:
    print("it is a cold day")
else:
    print('it is hot day ' + forecast)