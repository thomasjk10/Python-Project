#################################################################################
#          Project to simulate the game of SIM based on user inputs             #
#################################################################################

from random import randint
import re
import random


#----------------------This section accepts Player's Name------------------------#
while True:
    name = input("Please enter your name: ")
    name_chk = re.compile("^[a-zA-Z]+|_[0-9]+")
    if not re.match(name_chk,name) :
        print ("Please enter name without blanks or special characters")
        continue
    elif len(name) < 4:
        print ("Please enter upto 4 Characters")
        continue
    else:
        print ("Welcome ", name,)
        break

        
#----------------------This section accepts Player's Name------------------------#


#----------------------This section displays Playing Board-----------------------#
rand = randint(3,6)
pilecount = range(rand)
print ("Here is your game to play")
print ('\n')

pl_list = list()


for i in pilecount:
    a = (randint(1,10))
    pl_list.append(a)
    print("Pile ",i+1 ,":", end = "")
    for j in range(a):
        print(" X ", end= "")
    print('\n')

nimsum = 0
for i in pl_list:
    nimsum = i ^ nimsum


#----------------------This section displays Playing Board-----------------------#



#----------------------This section accepts Player's Choice----------------------#

winner = False

while winner is False:

#Now it is Player's turn to play
 winchk = (all([x==0 for x in pl_list])) 
 if winchk is True:
    winner = True
    break
 
 pilecho = input("Choose Pile number from following listed pile numbers --> ")
 try:
    choice = int(pilecho)
    try:
        pl_list[choice-1]
        if pl_list[choice-1] ==0:
            print ("This Pile is already Empty: ")
            continue
    except IndexError:
        print ("Try again:")
        continue
 except ValueError:
    print ("Please choose valid numeric Pile number only")
    continue
    
 try:
  valchi = pl_list[choice-1]
 except IndexError:
  print ("Please choose a Valid Pile only:")
  continue

 while True:
    if pl_list[choice-1] ==1:
        print ("Choose number of stones to remove from your selected pile", end ="")
        print ("(This is the last one you can remove) ", ":", end="")
        stone_chi = input()
        if stone_chi.isdigit() is False:
            print ("Please enter valid numeric value from given choices")
            continue
        elif int(stone_chi) > pl_list[choice-1]:
            print ("This pile does not contain", stone_chi, "stones, Try again")
            continue
        else:
            break
    else:
        print ("Choose number of stones to remove from your selected pile", end ="")
        print ("(Choose between 1 to", pl_list[choice-1],":)", end="")
        stone_chi = input()
        if stone_chi.isdigit() is False:
            print ("Please enter valid numeric value from given choices")
            continue
        elif int(stone_chi) > pl_list[choice-1]:
            print ("This pile does not contain", stone_chi, "stones, Try again")
            continue
        else:
            break

 upd_stack = pl_list[choice-1] - int(stone_chi)
 pl_list[choice-1] = upd_stack
 
 winchk = (all([x==0 for x in pl_list])) 
 if winchk is True:
    winner = True
    print (name, "wins")
    break

#----------------------This section accepts Player's Choice----------------------#



#----------------------This section calcuates Computer's Move--------------------#

#Now it is computer's turn to play
 print('\n')
 print ("Now it's my turn")
 nw_nimsum = 0
 for i in pl_list:
    nw_nimsum = i ^ nw_nimsum
 nz_list = list()
 
 if nw_nimsum == 0:
  
    for q in pl_list:
        if q!= 0:
            getindx = pl_list.index(q)
            nz_list.append(q)
            pickran = randint(0,q)
            pl_list[getindx] = pickran
            getindx = 0

            for i in range(len(pl_list)):
                print("Pile ",i+1 ,":", end = "")
                for d in range(pl_list[i]):
                    print(" X ", end= "")
                print('\n')
            break
    continue
     
  
 chkpt = 0
 cntr = 0

 for i in pl_list:
    ov = pl_list[cntr]
    while i !=0:
        ns = 0
        nv = i -1
        pl_list[cntr] = nv
        i = nv

        for j in pl_list:
            ns = j ^ ns

        if ns == 0:
            chkpt = 1
            break
        elif i == 0:  
            pl_list[cntr] = ov
     
    cntr = cntr +1
    if chkpt ==1:
        break
  
 winchk = (all([x==0 for x in pl_list])) 
 if winchk is True:
    winner = True
    print ("I win")
    break
 pilecount = len(pl_list)

 #----------------------This section calcuates Computer's Move--------------------#

 for i in range(pilecount):
    print("Pile ",i+1 ,":", end = "")
    for d in range(pl_list[i]):
        print(" X ", end= "")
    print('\n')
