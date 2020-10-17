"""
This is a console bot program.
1. Starts with a greeting and ask the name of person.
2. Greets and welcomes the person.
3. Asks the user to give Tags based on which it returns the  programs
4. Responds to user input appropriately and gives the available programs.
"""

import random 
from datetime import datetime
from Greeting import welcome
from ProgramBot import prob_name
from Intro import greet_introduce
from Menu import menu

greet_introduce() # Greeting Function
welcome() # Welcomes the User 
# Available Tags
available_tags = ["binary search" , "brute force" , "constructive algorithms" , "data structures"
         , "dfs and similar" , "divide and conquer" , "dp" , "geometry" , "graphs" , "hashing"]
x = menu() # Calling the menu() function

while(x!=3): # Base Condition for while loop
    if(x==2):
        prob_name(random.randint(1,100)) # Selecting 10 problems in a sequence by a random number in between 1 and 100
    elif(x==1):
        print("AVAILABLE TAGS :-        ","    ,   ".join(available_tags)) # Printing the Available Tags
    print()
    x=menu() # Recursively Asking for the user input until he/she wants to end the Bot.

print("--------THANK YOU! FOR USING THIS BOT---------") # Thanking message