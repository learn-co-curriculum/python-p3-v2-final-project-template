from models.monster import Monster
import sqlite3


class Scenario:
    def __init__(self, name, description, monster_id):
        self.name = name
        self.description = description
        self.monster_id = monster_id

    # Define scenario_descriptions as a class attribute
    scenario_descriptions = [
        ("Enchanted Cavern", "You stumble upon the mesmerizing Glowworm Guardian."),
        ("Haunted Mansion", "As you explore the eerie mansion, you encounter the ghostly Apparition of Lady Eliza."),
        ("Crystaline Glacier",
         "While traversing the icy terrain, you cross paths with Frostbite, the Ice Elemental."),
        ("Abandoned Lighthouse",
         "Inside the creaky lighthouse, you face the vengeful spirit known as Captain Blackbeard's Shadow."),
        ("Volcanic Crater", "Amidst the molten lava flows, you confront the Fireborn Drake, a fearsome fire-breathing serpent."),
        ("Whispering Caves", "Deep within the caverns, you're confronted by the enigmatic Echo Harvester, a creature that feeds on sound."),
        ("Sunken Shipwreck", "Exploring the depths of the ocean, you encounter the spectral Captain Barnacle, cursed to protect his sunken ship."),
        ("Enchanted Meadow", "In a serene meadow, you come across the mischievous Sprite Sylph, guardian of the hidden fairy treasure."),
        ("Forgotten Temple", "Within the ancient temple's ruins, you awaken the wrath of the Stone Golem, guardian of lost relics."),
        ("Sunken Cursed Ship", "Deep in the murky depths, you cross paths with the malevolent Sea Wraith, the vengeful spirit of a cursed pirate captain."),
        ("Mysterious Marshlands", "Lost in the eerie marshes, you confront the Bog Whisperer, a cunning witch who weaves spells from the mists."),
        ("Forgotten Ruined City", "Among the crumbling city ruins, you face the Spectral Legionnaire, a ghostly guardian of a long-forgotten empire."),
        ("Floating Isles of Aether", "Amidst the floating isles suspended in the sky, you face the Aethereal Harbinger, a celestial being that guards the secrets of the ethereal realm."),
        ("Lunar Plateau", "Upon a desolate lunar plateau, you stumble upon the Lunarchid, a mysterious lunar entity that dances under the pale moonlight."),
    ]

    @classmethod
    def initialize_scenario(cls, conn):
        cursor = conn.cursor()

        # Modified SQL to include monster_id
        sql = """
            CREATE TABLE IF NOT EXISTS scenarios (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                monster_id INTEGER,
                FOREIGN KEY (monster_id) REFERENCES monsters (id)
            )
        """
        cursor.execute(sql)
        conn.commit()

        # Fetch all monsters from the monster table
        monsters = {name: id for id, name in cursor.execute(
            'SELECT id, name FROM monsters').fetchall()}

        # Iterate through each scenario description and find the corresponding monster id
        for name, description in cls.scenario_descriptions:
            matched_monster_name = next(
                (monster_name for monster_name in monsters if monster_name in description), None)

            if matched_monster_name:
                monster_id = monsters[matched_monster_name]
                scenario = cls(name, description, monster_id)
                scenario.save(cursor, conn)
            else:
                print(f"No matching monster found for scenario: {name}")

    def save(self, cursor, conn):
        sql = """
            INSERT INTO scenarios (name, description, monster_id)
            VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.description, self.monster_id))
        conn.commit()

    @classmethod
    def get_random_scenarios(cls, cursor, num_scenarios):
        sql = """
            SELECT * FROM scenarios
            ORDER BY RANDOM()
            LIMIT ?
        """
        rows = cursor.execute(sql, (num_scenarios,)).fetchall()
        return [cls(row[1], row[2], row[3]) for row in rows]
