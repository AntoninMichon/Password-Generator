# Program Writen By Michon Antonin
# Program work on Python 3.9.7

# Imports :

from random import choice

# Variables :

low_letter = "abcdefghijklmnop"

high_letter = "ABCDEFGHIJKLMNOP"

spec_chara = "%:/&()[]{}#$:"

all = low_letter + high_letter + spec_chara


def gen(sym):
    """[Genere a random password]

    Args:
        sym ([String]): [All charactere who can be in password]

    Returns:
        [String]: [Password]
    """
    ok = False
    while not ok :
        user = int(input("Enter the number of charactere => "))
        if user < 6 :
            print("Your password will be too short, enter a number between 6 and 16")
        elif user > 16 :
            print("Your password will be too long, enter a number between 6 and 16")
        else :
            ok = True
    
    passwd =  "".join(choice(sym) for a in range(user))
    return passwd

password = gen(all)
print(password)



## Ty for use my program ;

## Contact :
# Mail : antonin.michon@laposte.net
# Twitter : @anto_mch