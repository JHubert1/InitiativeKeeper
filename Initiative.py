import sys
import numpy as np
from numpy import random
print("\n-Welcome to the Initiative Keeper v1.3-\n")
Party_input = input("Please enter the party members (space-separated): (PC1 PC2 PC3)\nParty: ")
Party = Party_input.split()
#Party = ["Norrin","Himo","Vuddar","Olafur","Taro"]
print("\nParty is:",Party,"\n")
flag=True
Party_copy = Party
COUNTER = 0

while(flag):
    new_enc = input("Do you want to run an encounter?\n y/n: ")

    if(new_enc=="y"):
        print("Enter Initiatives for: ", Party,"(space-separated)")
        initiatives_party_input = input()
        init_party = initiatives_party_input.split()

        for i in range(0,len(init_party)):
            init_party[i] = int(init_party[i])

        monsters_input = input("Enter monsters list (space separated)\n")
        monsters = monsters_input.split()


        init_monsters = []
        for i in range(0,len(monsters)):
            init_monsters.append(np.random.randint(0,20+1))

        #combine npcs and inits

        for i in range(0,len(monsters)):
            Party.append(monsters[i])
            init_party.append(init_monsters[i])

        sorted = np.argsort(init_party)
        #print(sorted)
        sorted = sorted[::-1]
        Party_sorted = []
        init_party_sorted = []
        #print(Party,init_party)
        for i in range(0,len(Party)):
            Party_sorted.append(Party[sorted[i]])
            init_party_sorted.append(init_party[sorted[i]])
        COUNTER += 1
        print("\n###########-ENCOUNTER NR.%d-#################" % COUNTER)
        for i in range(0,len(Party_sorted)):
            if(Party_sorted[i] in monsters):
                print("    ",Party_sorted[i],"-",init_party_sorted[i])
            else:
                print("PC: ",Party_sorted[i],"-",init_party_sorted[i])
        print("#######################################\n")
        Party_reset = []
        for i in range(0,len(Party)-len(monsters)):
            Party_reset.append(Party[i])
        Party = Party_reset

    else:
        print(" Do you really want to quit?")
        quitting = input("  y/n: ")
        if quitting=="y":
            flag=False
            rndnmr = np.random.randint(0,3)
            if(rndnmr ==0):
                print("See you.")
            if(rndnmr ==1):
                print("Bye.")
            if(rndnmr ==2):
                print("Bye bye.")
            if(rndnmr ==3):
                print("Hope to see you again.")
            sys.exit()
