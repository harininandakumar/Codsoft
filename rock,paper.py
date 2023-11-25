import random

user=input(['rock','paper','scissor'])
lap=random.choice(['rock','paper','scissor'])

if user==lap:
    print('tie')
elif user=="rock":
    if lap=="paper":
        print("you lose",lap,"covers",user)
    else:
        print("you win",user,"smashes",lap)

elif user=='paper':
    if lap=="scissor":
        print("you lose",lap,"out",user)
    else:
        print("you win",user,"covers",lap)

elif user=="scissor":
    if lap=="rock":
        print("you lose",lap,"smashes",user)
    else:
        print("you win",user,"out",lap)        

else:
    print("check")