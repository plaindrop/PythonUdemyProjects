from ast import If
from tkinter import W


print("How old are you?")
age = input()


if age:
    age = int(age)
    
    if age >= 18 and age < 21 :
        #Under 21 and atleast 18 needs a wristband
        print("You can enter, but you need a wristband")
    elif age >= 21:      
        #21+ can drinl, normal entry  
        print("You are good to enter and you can drink")
    else:
        #Too young, sorry
        print("You can't come in little one:(.")
else:
    print("Please enter an age.")

