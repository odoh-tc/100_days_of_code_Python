print("""
  
                                                     ..::''''::..
                                           .:::.   .;''        ``;.
   ....                                    :::::  ::    ::  ::    ::
 ,;' .;:                ()  ..:            `:::' ::     ::  ::     ::
 ::.      ..:,:;.,:;.    .   ::   .::::.    `:'  :: .:' ::  :: `:. ::
  '''::,   ::  ::  ::  `::   ::  ;:   .::    :   ::  :          :  ::
,:';  ::;  ::  ::  ::   ::   ::  ::,::''.    .    :: `:.      .:' ::
`:,,,,;;' ,;; ,;;, ;;, ,;;, ,;;, `:,,,,:'   :;:    `;..``::::''..;'
                                                     ``::,,,,::''

""")

print("Smiles, Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

text = input("You\'re at a crossroad. Where do you want to go? Type 'left' or 'right'?\n").lower()
if text == 'left':
    text_1 = input("You\'ve come to a lake."
                   "There is an island in the middle of the lake. Type \"wait\" to wait for a boat."
                                                                             " Type \"swim\" to swim across.?\n").lower()
    if text_1 == 'wait':
        text_2 = input("You arrive at the island unharmed. There is a house with 5 doors. One red, one green, "
                       "one orange, one yellow and one"
                       " blue. Which colour do you choose?\n").lower()
        if text_2 == 'blue':
            print("You enter a room of beasts. Game Over.")
        elif text_2 == 'yellow':
            print("You found the treasure! You Win!")
        elif text_2 == 'red':
            print("You get attacked by an angry trout. Game Over.")
        elif text_2 == 'green':
            print("You get attacked by an angry trout. Game Over.")
        elif text_2 == 'orange':
            print("It\'s a room full of fire. Game Over.")
        else:
            print("You chose a door that doesn\'t exist. Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over")

