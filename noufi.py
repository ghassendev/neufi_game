from random import randint
from pyfiglet import figlet_format
import random
import pygame
import math
main=figlet_format("welcome to noufi 9 !",font="doom")
print(main)
pmoney=30
bmoney=30
while pmoney>0 and bmoney>0:
    l=["♦","♣","♠","♥"]
    c=[random.choice(l) for i in range(3)]
    player=[randint(1,10) for i in range(3)]

    p=str(player[0])+c[0],str(player[1])+c[1],str(player[2])+c[2]
    bot=[randint(1,10) for i in range(3)]
    b=str(bot[0])+c[0],str(bot[1])+c[1],str(bot[2])+c[2]
    #sans=[8,9,10]

    saisir=input("si vous voulez jouer saisir y sinon saisir q ?")
    if saisir=="q":
        exit()

    while saisir=="y":
        print("player got:",p)
        #print("bot got :",b)


        o=input("saisir un card de votre main")
        if o=="" : print("vous devez saisir une valeur")
        while  o.isnumeric():

            c=int(o)
            if c==(player[0]):
                chose=c
                print("tu a choisi",chose)
            elif c==(player[1]):
                chose=c
                print("tu a choisi",chose)
            elif c==(player[2]):
                chose=c
                print("tu a choisi",chose)
            else:
                chose=0
                print("s'il vous choisir un nombre a partir de votre main")


            if bmoney>25:
                k=random.choice(bot)
                print("le bot a choisi",k)
            elif bmoney<25 and bmoney>10:
                k=max(bot)
                print("le bot a choisi", k)
            elif bmoney<10:
                k=10
                print("le bot a choisi",k)
            if chose>k:
                print(chose,">",k,"player win")
                if chose==max(player):
                    pmoney+=1
                    bmoney-=1
                    print("vous avez choisi le maximum")
                elif chose==min(player):
                    pmoney+=5
                    bmoney-=5
                    print("vous avez ganger avec le minimum bravo!!!")
                else:
                    pmoney+=3
                    bmoney-=3
                    print("vous avez gagner avec le moyen")

            elif chose<k:
                print(chose,"<",k,"bot win")
                pmoney-=1
                bmoney+=1



            else:
                print(chose,"=",k,"draw")
            print("your money=", pmoney)
            print("bot money=", bmoney)
            break
        break

    if  pmoney<=0:
         print("your money is over !!!!")
    elif bmoney<=0:
        print("bot money over you win ☺☺☺☺☺☺")




