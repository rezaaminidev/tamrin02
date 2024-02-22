print('This program determines whether you are overweight or not')
input('Please press enter to start the program\n')
weight = float(input('please write your weight\n'))
height = float(input('please write your height with meter like this : 1.90\n'))
bmi = weight / (height**2)
if(12<bmi<18):
    print('You are underweight')
elif(18<=bmi<=24):
    print('Your weight is ideal')
elif(24<bmi<=29):
    print('You are overweight')
elif(29<bmi<=39):
    print('you are fat')
elif(bmi>39):
    print('You are harmfully obese')    