import time
import random

inv = []
weapons = ['Fist']
stageID: str = '0'
game = 1
health = 100

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
                stage = '2'



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
        print('In front of you, a cave appears')
    time.sleep(1)

    while stageID == '2':
        do: str = input('1 Go into cave \n2 Turn back\n')
        if do == '1':
            print('You goes into the cave and you see a BEAR!')
            stageID = '2A'
            health = 100
        if do == '2':
            stageID = '1'
        else:
            pass
    while stageID == '2A':
        stageID = fight(phealth=health, enemy='Bear', eweapon1='Paw', eweapon2='Second Paw',  ehealth=150, edamage1=25, edamage2=25)







