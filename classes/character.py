class Character:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self

class Ninja(Character):

    def __init__( self , name ):
        super().__init__(name)
        # self.name = name
        self.strength = 15
        self.speed = 3
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        while(pirate.health > 10):
            pirate.health -= self.strength
            if(pirate.health == 0):
                print("character dead")
                return
        return self

class Pirate(Character):

    def __init__( self , name ):
        super().__init__(name)
        # self.name = name
        self.strength = 10
        self.speed = 3

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        while(ninja.health > 0 ):
            ninja.health -= self.strength
            if(ninja.health == 0):
                print("Character Dead")
                return
        return self
