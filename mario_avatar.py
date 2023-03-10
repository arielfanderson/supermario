__author__      = "Ariel Anderson"
__copyright__   = "Copyright 2023, SIE508, University of Maine"
__credits__     = ["Ariel Anderson"]


class Avatar: 
    ##Assigns name, hair, heighr, and superpower to each avatar. 
    def __init__(self, name, hair, height, superpower):
        self.name = name
        self.hair = hair
        self.height = height
        self.superpower = superpower 
    
    ## Allows user to change hair color.  
    def change_hair(self, new_hair): 
        self.hair = new_hair

    ## Allows user to change super power.      
    def change_superpower(self, new_superpower):
        self.superpower = new_superpower
    
    ## Animates each avatar. 
    def animate(self):
        print(f"Hello my name is {self.name}. My hair is {self.hair}. My height is {self.height} inches. My superpower is {self.superpower}.")
