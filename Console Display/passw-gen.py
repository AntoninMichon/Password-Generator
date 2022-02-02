# Program Writen By Michon Antonin
# Program while work on Python 3.9.7

# Imports :

from random import randint

# Variables :

low_letter = "abcdefghijklmnop"

high_letter = "ABCDEFGHIJKLMNOP"

spec_chara = "%:/&()[]{}#$:"

all = low_letter + high_letter + spec_chara


def gen(sym):
    ok = False
    passwd = ""
    while not ok :
        n_sym = eval(input("Enter the number of charactere => "))
        if n_sym < 8 :
            print("Your password will be too short, enter a number between 8 and 16")
        elif n_sym > 16 :
            print("Your password will be too long, enter a number between 8 and 16")
        else :
            ok = True 
    
    for a in range(n_sym):
        ran = randint(0, len(sym)-1)
        passwd += sym[ran]
    return passwd

password = gen(all)
print(password)



## Ty for use my program
## Contact :
# Mail : antonin.michon@laposte.net
# Twitter : @anto_mch
