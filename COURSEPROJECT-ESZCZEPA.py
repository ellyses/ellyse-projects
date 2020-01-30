import math
import random
import shlex

def check_argument(args):
    if (len(args)>0) and (args[0].isdigit() == True) and (int(args[0]) > 0):
        return int(args[0])
    else:
        return -1

### place your code below this line ###
    
menu = '''
1) Dice number from (2 to 5) for simulation, i.e., Dice 5
2) Confirm number of dice used in simulation, i.e. Confirm
3) Roll simulation dice a number of times, i.e. Roll 10
4) Report the simulation results, i.e., Report
5) Help menu, i.e., Help
6) Quit menu, i.e. Quit

Enter command (Dice N, Confirm, Roll N, Report, Quit) below:
'''

print(menu)
number_of_dice = ''
sim_report = []
sim_number = ''

results = []

var_run = []
var_sumofdie = []
var_dicenumbers = []

zippedlist = zip(var_run,var_sumofdie,var_dicenumbers)


### place your code above this line ###

while True:

    
    try:
        cmd, *args = shlex.split(input('> '))
        if len(args) == 0:
            args = []
    except ValueError:
        cmd = -1
        
    console_argument = check_argument(args)

    ### place your code below this line ###

    if cmd.lower() == 'dice'.lower():
        if (console_argument in range(2,6)):
            print('Your simulation will use',console_argument,'dice.')
            number_of_dice = console_argument
            
        else:
            print('Eror: You must select a number of die between 2 and 5.')
            
    elif cmd.lower() == 'confirm'.lower():
        print('Your selected number of die is:',number_of_dice,'die.')

        
    elif cmd.lower() == 'help'.lower():
        print(menu)

    elif cmd.lower() == 'quit'.lower():
        print('Thank you for using Casino Dice Simulator. Goodbye.')
        break
                    
    elif cmd.lower() == 'report'.lower():
        for a,b,c in zippedlist:
            print('Run:', a,'Sum:',b,'Dice Numbers:',c)

        
                
    elif cmd.lower() == 'roll'.lower():
        if (console_argument > 0):
            sim_number = console_argument
            for a in range(1,sim_number+1):
                z = []
                for b in range(number_of_dice):
                    z.append(random.randint(1,6))
                sumoflist = sum(z)
                var_run.append(a)
                var_sumofdie.append(sumoflist)
                var_dicenumbers.append(z)
            print('You rolled the die',sim_number,'times.')
                
         

        elif console_argument < 1:
            print('You must choose a number greater than zero, i.e. roll 10')
            
    else:
        print('Error: You have entered an unknown command:', cmd)
        
