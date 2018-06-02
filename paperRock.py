import random
agent = random.randint(0,2)
gamer = int (input("Pls choose a number (0,1,2)"))
knowledgebase ={0:'scissor' ,1:'rock',2:'paper'}
print('computer selected ',knowledgebase.get(agent))
print('you selected',knowledgebase.get(gamer))
if(agent==0):
    if(gamer==2):
        print('you lost')
    elif(gamer==1):
      print('you won')
    else:
       print('draw')
if(agent==1):
    if(gamer==2):
      print('you won')
    elif(gamer==0):
      print('you lost')
    else:
      print('draw')
if(agent==2):
    if(gamer==0):
      print('you won')
    elif(gamer==1):
      print('you lost')
    else:
      print('draw')
y=input("Press 0 to exit")