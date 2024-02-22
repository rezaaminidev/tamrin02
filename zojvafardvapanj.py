print('This program is designed to get an even or odd number\n')
input('Please press enter to start the program\n')
number = int(input('Please enter your number\n'))
zoj = number % 2 
if(zoj == 0):
    print('This number is even\n')
    if(number%5 == 0):
        print('bar panj bakhshpazir ast lotfan adad dovom ra vared konid\n')
        number2 = int(input())
        plus = number + number2
        print(f'majmoe adad bedast amade shode {plus}\n')
    else:
        print('bar panj bakhshpazir nist\n')

elif(zoj == 1):
    print('This number is odd\n')