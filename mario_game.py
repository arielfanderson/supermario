__author__      = "Ariel Anderson"
__copyright__   = "Copyright 2023, SIE508, University of Maine"
__credits__     = ["Ariel Anderson"]

class Game: 
    ## Intializes internal list of avatars.
    def startGame(self):

        self.avatar_list = []

    ## Adds avatars one at a time to internal list.     
    def add_avatar(self, avatar): 

        for i in self.avatar_list:
            if i.name == avatar.name:
                print("stored")
                return
        self.avatar_list.append(avatar)
    
    ## Adds all avatars to internal list as a bulk action. 
    def add_avatars(self, avatar_list): 

        for avatar in avatar_list: 
            self.add_avatar(avatar)

    ## Animates all avatars at the same time. 
    def animate_avatars(self): 

        for avatar_obj in self.avatar_list: 
            avatar_obj.animate()

    ## Deletes one avatar from the list at a time. 
    def delete_avatar(self, avatar):

        remaining_avatars = []
        for avatarname in self.avatar_list:
           if avatarname.name != avatar: 
              remaining_avatars.append(avatarname)

        self.avatar_list = remaining_avatars

    ## Deletes all avatars from internal list ending the game. 
    def stopGame(self): 

        self.avatar_list.clear() 
        print('Game Over')



