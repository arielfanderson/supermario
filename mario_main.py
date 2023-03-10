__author__      = "Ariel Anderson"
__copyright__   = "Copyright 2023, SIE508, University of Maine"
__credits__     = ["Ariel Anderson"]

import mario_game as game
import mario_avatar as avatar

def main(): 
    ## User selected avatars.  
    peach = avatar.Avatar('Peach', 'Blonde', '67', 'Magic')
    mario = avatar.Avatar('Mario', 'Black', '63', 'Star Power')
    toadstool = avatar.Avatar('Toadstool','Mushroom Hair', '35', 'Mushroom Power' )

    ## Starts the game. 
    super_mario_game = game.Game()

    super_mario_game.startGame()
    
    ## User avatars are added to the game. 
    super_mario_game.add_avatars([peach, mario, toadstool])

    ## Each user avatar is animated based on choosen characteristcs. 
    super_mario_game.animate_avatars() 

    ## User changes all avatars supoer power to cartoon. 
    peach.change_superpower('cartoon')
    mario.change_superpower('cartoon')
    toadstool.change_superpower('cartoon')

    ## Each user avatar is animated based on new superpower 'cartoon'. 
    super_mario_game.animate_avatars()
    
if __name__ == '__main__':
    main()