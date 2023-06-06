class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    enemies_defeated=0
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.intrest = None

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            enemies_defeated+=1
            return True
        else:
            print(self.name + " crashes you, puny adventurer!")
            return False
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def set_intrest(self, item_intrest):
        self.intrest = item_intrest

    def get_intrest(self):
        return self.intrest


    def steal(self):
        print("You stole from "+ self.name)

    def bribe(self, bribe_item):
        if bribe_item == self.intrest:
            print("You bribe " + self.name + " off with the " + bribe_item)
            return True
        else:
            print(self.name + " gets annoyed and attacks you!")
            return False

        
    
class Freind(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def hug(self):
        print("You hugged "+ self.name)

    def gift(self):
        print(self.name + " gave you a gift.")
