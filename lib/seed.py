from models.world import World
from models.player import Player

Player.create_table()
World.create_table()
Player.create_table2()

seed1 = Player("Matt")
seed2 = Player("Nicole")
seed3 = Player("GreatTashi")
seed4 = Player("Brair")
seed5 = World("Howling Castle")
seed6 = World("Newb Start")
seed7 = World("Tashi's World")

seed1.save()
seed2.save()
seed3.save()
seed4.save()
seed5.save()
seed6.save()
seed7.save()

seed1.login(seed5)
seed1.login(seed7)
seed2.login(seed6)
seed2.login(seed5)
seed2.login(seed7)
seed3.login(seed6)
seed3.login(seed7)
seed4.login(seed5)

data1 = Player("CowSlayer")
data1.save()
data1.login(seed6)