#Project to simulate the game of SIM based on user inputs
from random import randint
import re

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

#Now it is Player's turn to play
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

#Now it is computer's turn to play
print ("Now it's my turn")
nw_nimsum = 0
#print (nimsum)
for i in pl_list:
 nw_nimsum = i ^ nw_nimsum
print ("now new sum is", nw_nimsum)
#for i in pl_list:
# bi_num = bin(i)
# print (bi_num, end = " ")
# print (bi_num[1])
ns = 0
#index = 0
for i in pl_list:
  ov = i
  while i !=0:
   #print ("**1",ov)
   nv = i -1
   pl_list[pl_list.index(i)] = nv
   i = nv
   print (pl_list)
   for j in pl_list:
    ns = j ^ ns
    print ("new sum", ns)
    #break
    # might need to move  the if statement below the above print
  if ns ==0:
    break 
  pl_list[pl_list.index(i)] = ov
     #pl_list[pl_list.index(i)] = ov
  #continue
  
print (pl_list)

  
 #print (pl_list.index(i)) --- to get index value of a list item
 
  

  
  

