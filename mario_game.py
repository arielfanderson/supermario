class Game: 
    def __init__(self):
        self.avatar_list = []
    def add_avatar(self, name): 
        results = list(filter(lambda x: x['name'] == name, self.avatar_list))
        if results:
            print("stored")
        else:
            self.avatar_list.append({'name': name})
    def add_all_Avatar(self, avatar_list):
        for avatar in avatar_list:
            self.avatar_list.append(avatar) 
    def delete_avatar(self, name):

        idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(self.avatar_list)))
    
        if idxs_items: 
            i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        #print("idxs_items[0][0], idxs_items[0][1]: ", idxs_items[0][0], " item in list, value:", idxs_items[0][1])
            del self.avatar_list[i]
        
        else:
            print('Can\'t delete "{}" because it\'s not stored')
    def stopGame(self): 
        self.avatar_list.clear() 

class Avatar: 
    def __init__(self, name, hair, height, superpower):
        self.name = name
        self.hair = hair
        self.height = height
        self.superpower = superpower 



mygame = Game()
avatar = Avatar() 

avatar1 = ('Peach', 'Blonde', 64, 'Magic')


mygame.add_all_Avatar(avatar1)


print(mygame.avatar_list)

mygame.delete_avatar('Peach')

print(mygame.avatar_list)

mygame.stopGame()

print(mygame.avatar_list)