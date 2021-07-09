import time
import random

inv = [] #keeps inventory when dies?
weapons = ['Fist']
armors = []
shields = []
stageID: str = '0'
game = 1
health = 100
armor = 0
window1 = 'notbroken'
key1 = False
treasure = False

def fight(phealth, enemy, ehealth, eweapon1, protectRate=3, stage=None, protectionAmount=None, edamage1=None, edamage2=None, edamage3=None, eweapon2=None, eweapon3=None, shield=None, _armor_=None):
    if _armor_ == 'bear armor':
        armor = 50
    playerHealth = int(phealth) + int(armor)
    fighting = 1
    while fighting == 1:
        print('Your health: ' + str(playerHealth))
        print('Weapon: ' + str(weapons[0]))
        if not shield == None:
            print('Shield: ' + str(shield))
        if not _armor_ == None:
            print('Armor: ' + str(_armor_))
        
        attacking = 1
        while attacking == 1:
            if weapons[0] == 'Fist':
                print('1 Punch')
            elif weapons[0] == 'stick':
                print('1 Stab')
            if shields[0] == 'iron shield':
                print('2 Protect with shield')
            elif shield == None:
                print('2 Protect with ' + str(weapons[0]))

            do: str = input('3 Escape\n')
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
                    if enemy == 'Bear':
                        print(': - Bear defeated - :')
                        time.sleep(1)
                        print('Bear dropped | Bear armor |')
                        armors.insert(0, 'bear armor')
                        inv.insert(0, 'bear armor')

                    
                    
            if do == '2':
                if shields[0] == 'iron shield' and not shields[0] == None:
                    playerHealth += 70
                    print('You protected 70 (' + str(playerHealth) + ') with ' + shields[0])
                    attacking = 0
                    do = ''
                elif weapons[0] == 'iron axe':
                    playerHealth += 10
                    print('You protected 10 (' + str(playerHealth) + ') with ' + weapons[0])
                elif weapons[0] == 'tree sword':
                    playerHealth += 30
                    print('You protected 30 (' + str(playerHealth) + ') with ' + weapons[0])
                elif weapons[0] == 'stick':
                    playerHealth += 10
                    print('You protected 10 (' + str(playerHealth) + ') with ' + weapons[0])
                    attacking = 0
                elif weapons[0] == 'Fist':
                    ehealth += 10
                    print('You protected 10 (' + str(playerHealth) + ') with ' + weapons[0])
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
                print('Weapons: ' + str(eweapon1) + ', ' + str(eweapon2))
            else:
                print('Weapons: ' + str(eweapon1) + ', ' + str(eweapon3))
        elif eweapon3 == None:
            if eweapon2 == None:
                print('Weapons: ' + str(eweapon1) + ', ' + str(eweapon2))
            else:
                print('Weapons: ' + str(eweapon1) + ', ' + str(eweapon2))

        else:
            print('Weapon: ' + str(eweapon1))
        time.sleep(2)


        ran = random.randint(1, (3 + protectRate))
        try:
            if ran == 1:
                if armor > edamage1:
                    playerHealth = ((playerHealth + armor) - edamage1) - (armor - edamage1)
                else:
                    playerHealth = ((playerHealth + armor) - edamage1)
                print(enemy + ' damaged you ' + edamage1 + ' with ' + eweapon1)
            elif ran == 2 and not eweapon2 == None:
                if armor > edamage2:
                    playerHealth = ((playerHealth + armor) - edamage2) - (armor - edamage2)
                else:
                    playerHealth = ((playerHealth + armor) - edamage2)
                print(str(enemy) + ' damaged you ' + str(edamage2) + ' with ' + str(eweapon2))
            elif ran == 3 and not eweapon3 == None:
                if armor > edamage3:
                    playerHealth = ((playerHealth + armor) - edamage3) - (armor - edamage3)
                else:
                    playerHealth = ((playerHealth + armor) - edamage3)
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

#future enemy: spider
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
            print('You walks away but have to choose direction\n')
        if do == '2':
            print('You ignores the stick and goes on')
            stageID = '1'
            time.sleep(1)
            print('You walks away but have to choose direction')
        else:
            pass

    while stageID == '1':
        do: str = input('1 Go right\n2 Go left\n')
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
            health = 100
        if do == '2':
            print('Choose direction')
            stageID = '1'

        else:
            pass
    while stageID == '2A':
        stageID = fight(phealth=health, enemy='Bear', eweapon1='Paw', eweapon2='Second Paw',  ehealth=150, edamage1=25, edamage2=25, stage=stageID, shield=shields, _armor_=armors[0])
        

    while stageID == '3':
        do: str = input('1 Go to house \n2 Turn back\n')
        if do == '1':
            print('You goes to the house...')
            stageID = '3A'
        if do == '2':
            print('Choose direction')
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
                    do = ' '
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
                    do = ' '
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
            print('You climbs into the broken window...')
            time.sleep(1)
            print('In the house, there is a key on a table')
            stageID = '3D'

            pass
        if do == '2':
            print('You runs back to the way split')
            stageID = '1'

    while stageID == '3C': #needs to own stick or a breaker tool

        do: str = input('1 Knock on the door\n2 Climb into crushed window\n3 Turn back\n')

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
            if key1 == False:
                print('In the house, there is a key on a table')
                stageID = '3D'
            else:
                stageID = '3E'

        if do == '3':
            stageID = '3'
        else:
            pass

    while stageID == '3D':  # needs to own stick or a breaker tool
        if key1 == False:
            do: str = input('1 Pick key\n2 Keep going\n3 Turn back\n')
        else:
            stageID = '3E'

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
            do = ''
            pass
        if do == '2':
            time.sleep(1)
            if key1 == True:
                print('You opens the door with the key...')
                time.sleep(2)
                if treasure == False:
                    print('There is 3 tools and weapons in this room, pick one')
                    stageID = '3F'
                else:
                    print('Wrong key')

            if key1 == False:
                print('The door is locked')
                do = ''
                pass

        if do == '3':
            print('You looks under the bed but there is nothing there')
            do = ''
            pass


        if do == '4':
            stageID = '3'
        else:
            pass

    while stageID == '3F' and treasure == False:  # needs to own stick or a breaker tool
        treasure = True
        do: str = input('1 A tree sword\n2 An iron axe\n3 An iron shield\n4 Turn back\n (You can only pick one, and only now, so think wisely)\n')

        if do == '1':
            print('- * You picks the tree sword * -')
            inv.insert(0, 'tree sword')
            weapons.insert(0, 'tree sword')
            for i in range(5):
                time.sleep(1)
                print('.', end='')
            do = ''
            print('\nYou wakes up again, but outside the house...')
            stageID = '1'

        if do == '2':
            print('- * You picks the iron axe * -')
            inv.insert(0, 'iron axe')
            weapons.insert(0, 'iron axe')
            for i in range(5):
                time.sleep(1)
                print('.', end='')
            do = ''
            print('\nYou wakes up again, but outside the house...')
            stageID = '1'


        if do == '3':
            print('- * You picks the iron shield * -')
            inv.insert(0, 'iron shield')
            shields.insert(0, 'iron shield')
            for i in range(5):
                time.sleep(1)
                print('.', end='')
            do = ''
            print('\nYou wakes up again, but outside the house...')
            stageID = '1'
            #stageID = '4'


        if do == '4':
            stageID = '3'
        else:
            pass





