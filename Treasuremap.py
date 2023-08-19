print('''
 _                                                           
| |                                                          
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ __ ___   __ _ _ __  
| __| '__/ _ \/ _` / __| | | | '__/ _ \ '_ ` _ \ / _` | '_ \ 
| |_| | |  __/ (_| \__ \ |_| | | |  __/ | | | | | (_| | |_) |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_| |_| |_|\__,_| .__/ 
                                                      | |    
                                                      |_|    
                                                      ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

turn=input("Ypu arrived at a crossroad do you want to take a left or right turn?")
turn=turn.lower()
if turn=="left":
    sea=input("You have arrived at a seashore, do you wish to swim or wait?" )
    sea=sea.lower()
    if sea=="wait":
        door=input("You reached an island and see 3 doors with colors Red, Yellow and Blue. Which color do yo choose?")
        door=door.lower()
        if door=="red":
            print("Burned by fire. GAME OVER.")
        elif door=="yellow":
            print("YOU WIN!")
        elif door=="blue":
            print("Eaten by beasts. GAME OVER")
        else:
            print("GAME OVER")
    else:
        print("Attacked by shark.GAME OVER")


else:
    print("You fell into hell.GAME OVER")   
