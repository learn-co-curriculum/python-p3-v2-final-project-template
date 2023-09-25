class Monster:
    def __init__(self, id, name, hit_points=100):
        self.name = name
        self.hit_points = hit_points

#creates basic monster
def create_monster(name, hit_points):
    return Monster(name, hit_points)

monster1 = create_monster("Wolf", 100)
monster2 = create_monster("thief", 50)

print(monster1)
print(monster2)
