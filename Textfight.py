import time
import random

inv = []
weapons = ['Fist']
armors = []
stageID: str = '0'
game = 1
health = 100
armor = 0
window1 = 'notbroken'
key1 = False
def fight(phealth, enemy, ehealth, eweapon1, protectRate=3, stage=None, protectionAmount=None, edamage1=None, edamage2=None, edamage3=None, eweapon2=None, eweapon3=None):
    playerHealth = phealth
    fighting = 1
    while fighting == 1:
        print('Your health: ' + str(playerHealth))
        print('Weapon: ' + weapons[0])
        attacking = 1
        while attacking == 1:
            if weapons[0] == 'Fist':
                do: str = input('1 Punch \n2 Protect with fist \n3 Escape\n')
            if weapons[0] == 'stick':
                do: str = input('1 Stab \n2 Protect with stick \n3 Escape\n')
            time.sleep(2)

            if do == '1':
                if weapons[0] == 'stick':
                    ehealth -= 15
                    print('Enemy health - 15 (' + str(ehealth) + ')')
                    attacking = 0
                if weapons[0] == 'Fist':
                    ehealth -= 10
                    print('Enemy health - 10 (' + str(ehealth) + ')')
                    attacking = 0
                time.sleep(2)
                if ehealth <= 0:
                    print(enemy + ' died')
                    stage[len(stage)] = 'b'
            if do == '2':
                if weapons[0] == 'stick':
                    playerHealth += 10
                    print('You protected 10 (' + str(playerHealth) + ')')
                    attacking = 0
                if weapons[0] == 'Fist':
                    ehealth += 10
                    print('You protected 10 (' + str(playerHealth) + ')')
                    attacking = 0
                time.sleep(2)
            if do == '3':
                print('You escapes with ' + str(playerHealth) + ' health')
                stagepart = stage[0:len(stage) - 1]
                int(stagepart)
                stage = stagepart




                time.sleep(3)
                return stage


        print(enemy + ' health: ' + str(ehealth))
        if eweapon2 == None:
            if eweapon3 == None:
                print('Weapon: ' + str(eweapon1) + ', ' + str(eweapon2))
            else:
                print('Weapon: ' + str(eweapon1) + ', ' + str(eweapon3))
        elif eweapon3 == None:
            if eweapon2 == None:
                print('Weapon: ' + str(eweapon1) + ', ' + str(eweapon2))
            else:
                print('Weapon: ' + str(eweapon1) + ', ' + str(eweapon2))

        else:
            print('Weapon: ' + str(eweapon1))
        time.sleep(2)


        ran = random.randint(1, (3 + protectRate))
        try:
            if ran == 1:
                playerHealth -= edamage1
                print(enemy + ' damaged you ' + edamage1 + ' with ' + eweapon1)
            elif ran == 2 and not eweapon2 == None:
                playerHealth -= edamage2
                print(str(enemy) + ' damaged you ' + str(edamage2) + ' with ' + str(eweapon2))
            elif ran == 3 and not eweapon3 == None:
                playerHealth -= edamage3
                print(str(enemy) + ' damaged you ' + str(edamage3) + ' with ' + str(eweapon3))

            elif ran == 4:
                ehealth += int(protectionAmount)
                print(str(enemy) + ' protected himself with ' + str(eweapon1))
            else:
                playerHealth -= edamage1
                print(str(enemy) + ' damaged you ' + str(edamage1) + ' with ' + str(eweapon1))
            time.sleep(2)
        except:
            playerHealth -= edamage1
            print(str(enemy) + ' damaged you ' + str(edamage1) + ' with ' + str(eweapon1))
            time.sleep(2)
        if playerHealth <= 25 and playerHealth >= 0:
            print('Your health is low, selecting protect with' + weapons[0] + ' or escape is recommended')
        if playerHealth <= 0:
            print('You died...')
            stage = '0'
            return stage


while game == 1:
    if stageID == '0':
        print('You wakes up in a forest...')
        time.sleep(2)
        print('With the sun in your eyes...')
        time.sleep(2)
        print('You founds a stick on the ground...')
        time.sleep(2)
    while stageID == '0':
        do: str = input('What do you do?\n1 Pick up\n2 Ignore\n')
        if do == '1':
            inv.insert(0, 'stick')
            weapons.insert(0, 'stick')
            print('You picks up the stick and goes on')
            stageID = '1'
            time.sleep(1)
        if do == '2':
            print('You ignored the stick and goes on')
            stageID = '1'
            time.sleep(1)
        else:
            pass

    while stageID == '1':
        do: str = input('You walks away but have to choose direction\n1 Right\n2 Left\n')
        if do == '1':
            print('You turns right and continues walk')
            stageID = '2'
            time.sleep(1)
        if do == '2':
            print('You turns left and continues walk')
            stageID = '3'
            time.sleep(1)


        else:
            pass
    if stageID == '2':
        print('In front of you, a cave appears')

    if stageID == '3':
        print('A lot of meters away a house appears')
    time.sleep(1)

    while stageID == '2':
        do: str = input('1 Go into cave \n2 Turn back\n')
        if do == '1':
            print('You goes into the cave and you see a BEAR!')
            stageID = '2A'
            health = 100 + armor
        if do == '2':
            stageID = '1'
        else:
            pass
    while stageID == '2A':
        stageID = fight(phealth=health, enemy='Bear', eweapon1='Paw', eweapon2='Second Paw',  ehealth=150, edamage1=25, edamage2=25, stage=stageID)
        print(': - Bear defeated - :')
        #time.sleep(1)
        #print('Bear dropped | Bear armor |')
        #armors.insert(0, 'bear armor')
        #inv.insert(0, 'bear armor')
        #armor = 25

    while stageID == '3':
        do: str = input('1 Go to house \n2 Turn back\n')
        if do == '1':
            print('You goes to the house...')
            stageID = '3A'
        if do == '2':
            stageID = '1'
        else:
            pass

    while stageID == '3A':
        if weapons[0] == 'stick':
            if window1 == 'notbroken':
                do: str = input('1 Knock on the door\n2 Break window with stick\n3 Turn back\n')
                if do == '1':
                    print('You knocks on the door...')
                    time.sleep(2)
                    print('...')
                    time.sleep(4)
                    print('No answer')
                    pass
                if do == '2':
                    stageID = '3B'
                    
                if do == '3':
                    stageID = '3'
                else:
                    pass
                
            else:
                do: str = input('1 Knock on the door\n2 Climb into crushed window\n3 Turn back\n')
                if do == '1':
                    print('You knocks on the door...')
                    time.sleep(2)
                    print('...')
                    time.sleep(4)
                    print('No answer')
                    pass
                if do == '2':
                    stageID = '3D'

                if do == '3':
                    stageID = '3'
                else:
                    pass
        else:   
            do: str = input('1 Knock \n2 Turn back\n')
        if do == '1':
            print('You knocks on the door...')
            time.sleep(2)
            print('...')
            time.sleep(4)
            print('No answer')
            pass
        if do == '2' and not weapons[0] == 'Fist':
            stageID = '3B'
        if do == '3' and not weapons[0] == 'Fist':
            stageID = '3'
        elif do == '2' and weapons[0] == 'Fist':
            stageID = '3'
        else:
            pass
    
    while stageID == '3B':
        window1 = 'broken'
        do: str = input('1 Climb into crushed window\n2 Run away\n')
        if do == '1':
            print('You knocks on the door...')
        
        if do == '1':
            stageID = '3C'
    
    while stageID == '3C': #needs to own stick or a breaker tool
        
        do: str = input('1 Knock on the door\n2 Climb into window\n3 Turn back\n')

        if do == '1':
            print('You knocks on the door...')
            time.sleep(2)
            print('...')
            time.sleep(4)
            print('No answer')
            pass
        if do == '2':
            print('You climbs into the broken window...')
            time.sleep(1)
            print('In the house, there is a key on a table')
            stageID = '3D'
        if do == '3':
            stageID = '3'
        else:
            pass

    while stageID == '3D':  # needs to own stick or a breaker tool

        do: str = input('1 Pick key\n2 Keep going\n3 Turn back\n')

        if do == '1':
            print('You Picks up the key and keeps going around in the house')
            key1 = True
            time.sleep(1)
            print('You found a fridge, a door and a bed')
            
            time.sleep(2)
            stageID = '3E'
            
        if do == '2':
            stageID = '3E'
        if do == '3':
            stageID = '3'
        else:
            pass

    while stageID == '3E':  # needs to own stick or a breaker tool

        do: str = input('1 Open fridge\n2 Open door\n3 Check bed\n4 Turn back\n')

        if do == '1':
            print('You opens the fridge...')
            time.sleep(2)
            print('The fridge is empty')
           
            time.sleep(2)
            pass
        if do == '2':
            time.sleep(1)
            if key1 == True:
                print('You opens the door with the key...')
                stageID = '3F'
                
            if key1 == False:
                print('The door is locked')
                pass
        
        if do == '3':
            print('You looks under the bed but there is nothing there')
            pass
            
        
        if do == '4':
            stageID = '3'
        else:
            pass






