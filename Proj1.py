#Project to simulate the game of SIM based on user inputs
from random import randint
import re
import random

#name = input("Please enter your name: ")
while True:
 name = input("Please enter your name: ")
 if len(name) ==0 :
  print ("Please enter non-blank name")
  continue
 else:
  print(name[:1])
  break

 
rand = randint(3,6)
#print ("this is the piles selection")
#print (rand)
pilecount = range(rand)
#print (*range(4)) ---to display the range in one line
print ('\n')
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
print (pl_list)

#print (dir(pl_list)) 
#Calculate initial value of NIM sum
nimsum = 0
#print (nimsum)
for i in pl_list:
 nimsum = i ^ nimsum
print (nimsum, end = " ")
#print (nimsum, end = " ")

winner = False

while winner is False:

#Now it is Player's turn to play
 winchk = (all([x==0 for x in pl_list])) 
 if winchk is True:
  break
 print ("Choose Pile number from following listed pile numbers -->", end ="")
 for i in range(len(pl_list)):
  print (i+1, end =" ")
 choice =int(input(":"))
 print ("Choose number of stones to remove from your selected pile",choice, ":", end ="")
 if pl_list[choice-1] ==1:
  print ("This is the last one you can remove", ":", end="")
  stone_ch = int(input())
 else:
  print ("(Choose between 1 to", pl_list[choice-1],":)", end="")
  stone_ch = int(input())
 upd_stack = pl_list[choice-1] - stone_ch
 pl_list[choice-1] = upd_stack
 print (pl_list)
 winchk = (all([x==0 for x in pl_list])) 
 if winchk is True:
  print (name, "wins")
  break

#Now it is computer's turn to play
 print ("Now it's my turn")
 nw_nimsum = 0
#print (nimsum)
 for i in pl_list:
  nw_nimsum = i ^ nw_nimsum
 print ("now new sum is", nw_nimsum)
 if nw_nimsum == 0:
  chklen = len(pl_list)
  ranindx = random.randint(0,chklen)
  ranival = pl_list[ranindx]
  pickran = randint(range(ranival))
  pl_list[pl_list.index(ranindx)] = pickran
  break
  
 chkpt = 0
 cntr = 0
#index = 0
 for i in pl_list:
   ov = pl_list[cntr]
  #ns = 0
   while i !=0:
   #print ("**1",ov)
    ns = 0
    nv = i -1
    # need to handle this check because some list items can be same:
    pl_list[cntr] = nv
    i = nv
    print (pl_list)
    for j in pl_list:
     ns = j ^ ns
    print ("new sum", ns)
    #break
    #ns = 0
    if ns ==0:
     chkpt = 1
     break
    elif i == 0:  
     pl_list[cntr] = ov
     cntr = cntr +1
     #pl_list[pl_list.index(i)] = ov
  #continue
  #chkpt =1
   if chkpt ==1:
     break
  
 print (pl_list)
 winchk = (all([x==0 for x in pl_list])) 
 if winchk is True:
  print ("I win")
  break
 pilecount = len(pl_list)


 for i in range(pilecount):
  print("Pile ",i+1 ,":", end = "")
  for d in range(pl_list[i]):
     print(" X ", end= "")
  print('\n')
 
 
#pl_list[pl_list.index(i)] = nv

# This has been test.... continue after this check  
 #print (pl_list.index(i)) --- to get index value of a list item