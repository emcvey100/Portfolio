from character import Enemy
dave = Enemy("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("Hi. I am Dave!")
dave.talk()

dave.set_weakness("cheese")

print("what will you fight with?")
fight_with = input()
dave.fight(fight_with)
