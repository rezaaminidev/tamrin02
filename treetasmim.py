
print('please write your name\n')
name = input()

print(f'{name} do you hungry? please type yes Or no\n')
yesOrNo= input()
if (yesOrNo == 'yes'):
    print('You should go eat\n')
    input('Press Enter to ask the next question\n')
    print('What is your favorite food? Choose one of these options\n')
    food =  input('kabab , jooje , abgoosht\n')
    print('please write your age')
    age = int(input())
    
    if(food == 'jooje' and age> 60):
        print('jooje lotfan kam bokhorid')
    elif(food == 'jooje' and age <=60):
        print('Do you like soft drinks? yes or no \n')
        yesorno2 =input()
        if(yesorno2 == 'yes'):
            if(age<=30):
                print('Please drink soda sparingly')
            elif(age>30):
                print('Please do not drink soda, it is harmful')    
        elif(yesorno2=='no'):
            print('its so great\n')
            print('Please eat more vegetables')        
    if(food == 'kabab' and age > 60):
        print('kabab baraye shoma zarar darad')
    elif(food == 'kabab' and age<=60):
        print('Do you like soft drinks? yes or no \n')
        yesorno3 =input()
        if(yesorno3 == 'yes'):
            if(age<=30):
                print('Please drink soda sparingly')
            elif(age>30):
                print('Please do not drink soda, it is harmful')    
        elif(yesorno3 =='no'):
            print('its so great\n')
            print('Please eat more vegetables')
    if(food == 'abgoosht'):
        print('This food is good for all ages')   
    else:
        print('You did not select any entry, I cannot help you')
elif(yesOrNo == 'no'):

    print('are you thirsty?\n')

    elsa = input('please type yes or no \n')
    if(elsa == 'yes'):
        print('Go have a drink')
    elif(elsa == 'no'):
        print('Thank you very much for answering my questions')
else:
    print('Run the program from the beginning and answer the questions accurately')

