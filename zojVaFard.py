print('This program is designed to get an even or odd number\n')
input('Please press enter to start the program\n')
number = int(input('Please enter your number\n'))
zoj = number % 2 
if(zoj == 0):
    print('This number is even\n')

elif(zoj == 1):
    print('This number is odd\n\n')