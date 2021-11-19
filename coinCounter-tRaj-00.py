'''
Program: Coin Counter
Filename: coinCounter-tRaj-00.py
Author: Tushar Raj
Description: takes the user input and calculate the coin counter report
Revisions: No revisions made
'''
#There is no import statement
#There are no literal constraint
#There are no class defined

### Step 1: Announce, prompt and get Response
print("Coin Counter:")
print("Program to count coins and calculate values\n")

user_input = input("Enter coin string: ").lower()

#Checks for the valid input if not there quits the program
if (any(i not in "pndqh" for i in user_input)):
    print("Please enter a valid string")
    quit()

### Step 2: Calculate the number of pennies,nickles,dimes, quaters and half-dollars
p,n,d,q,h=0,0,0,0,0 #Initilazing the variables to 0
for i in user_input: # using the for loop to pick up each character one by one and check based of condition and increase the respective counter variable
    if(i == "p"): #check for pennies and increase counter varibale p
        p+=1
    elif(i == "n"):#check for nickles and increase counter varibale n
        n+=1
    elif(i == "d"):#check for dimes and increase counter varibale d
        d+=1
    elif(i == "q"):#check for quaters and increase counter varibale q
        q+=1
    else:
        h+=1 #else increase counter varibale h for hald dollars
total=(p*0.01+n*0.05+d*0.10+q*0.25+h*0.50) #Calculate the total amount
halfDollar,dime="0.50","0.10"

### Step 3: Print thee result in desired format
print("\n===========================================")
print(f"{f'Coin Counter Report':^43}")
print("===========================================\n")
print(f"Coin{f'Value':>19}\t{f' ':>3}Number{f' ':>4}Amount")
print(f"===={f'=====':>19}\t{f' ':>3}======{f' ':>4}======")
print(f"Pennies{f' ':>8}{f'${0.01}':>8}\t{f' ':>5}{f'{p}':>2}{f' ':>6}${f'{p*0.01:4.2f}':>5}")
print(f"Nickels{f' ':>8}{f'${0.05}':>8}\t{f' ':>5}{f'{n}':<2}{f' ':>6}${f'{n*0.05:4.2f}':>5}")
print(f"Dimes{f' ':>10}{f'${dime}':>8}\t{f' ':>5}{f'{d}':<2}{f' ':>6}${f'{d*0.10:4.2f}':>5}")
print(f"Quaters{f' ':>8}{f'${0.25}':>8}\t{f' ':>5}{f'{q}':<2}{f' ':>6}${f'{q*0.25:4.2f}':>5}")
print(f"Half-dollars{f' ':>3}{f'${halfDollar}':>8}\t{f' ':>5}{f'{h}':<2}{f' ':>6}${f'{h*0.50:4.2f}':>5}")
print(f"{f'Total amount: $ {total}':>43}")

#Dosplay user that coin counter program has ended
print("\n\n****Coin Counter Program have ended****")
