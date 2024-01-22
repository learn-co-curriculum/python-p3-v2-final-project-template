#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.player import Player
from models.level import Level
from models.game import Game
# from models.pet import Pet

def seed_database():
    Player.drop_table()
    Level.drop_table()
    Game.drop_table()
    Player.create_table()
    Level.create_table()
    Game.create_table()

    # # Create seed data
    level1 = Level.create("1-a", "Beginner", "Hello, World!")
    level2 = Level.create("1-b", "Beginner", "Practice makes perfect.")
    level3 = Level.create("1-c", "Beginner", "Keyboard ninja in training.")
    level4 = Level.create("1-d", "Beginner", "The quick brown fox jumps over the lazy dog.")
    level5 = Level.create("1-e", "Beginner", "Keyboard ninja in training.")
    level6 = Level.create("1-f", "Beginner", "Coding is fun!")
    level7 = Level.create("1-g", "Beginner", "Type your way to victory.")
    level8 = Level.create("1-h", "Beginner", "Challenge accepted, fingers ready!")
    level9 = Level.create("1-i", "Beginner", "Words are your playground.")
    level10 = Level.create("1-j", "Beginner", "Unlock the keyboard wizard in you.")
    level11 = Level.create("2-a", "Intermediate", "The quick brown fox jumps over the lazy dog.")
    level12 = Level.create("2-b", "Intermediate", "A journey of a thousand miles begins with a single step.")
    level13 = Level.create("2-c", "Intermediate", "In the midst of winter, I found there was, within me, an invincible summer.")
    level14 = Level.create("2-d", "Intermediate", "Success is not final, failure is not fatal: It is the courage to continue that counts.")
    level15 = Level.create("2-e", "Intermediate", "The only limit to our realization of tomorrow will be our doubts of today.")
    level16 = Level.create("2-f", "Intermediate", "Life is what happens when you're busy making other plans.")
    level17 = Level.create("2-g", "Intermediate", "Believe you can and you're halfway there.")
    level18 = Level.create("2-h", "Intermediate", "The greatest glory in living lies not in never falling, but in rising every time we fall.")
    level19 = Level.create("2-i", "Intermediate", "It does not matter how slowly you go, as long as you do not stop.")
    level20 = Level.create("2-j", "Intermediate", "The best way to predict the future is to create it.")
    level21 = Level.create("3-a", "Advanced", "The entropy of the universe tends to a maximum, but human creativity strives to defy that cosmic inevitability.")
    level22 = Level.create("3-b", "Advanced", "Quantum mechanics introduces us to a world where particles exist in multiple states until observed, challenging our classical intuitions.")
    level23 = Level.create("3-c", "Advanced", "In the realm of artificial intelligence, neural networks emulate the complexity of the human brain, pushing the boundaries of machine learning.")
    level24 = Level.create("3-d", "Advanced", "Chaos theory reveals the underlying order in seemingly random systems, demonstrating the exquisite sensitivity to initial conditions.")
    level25 = Level.create("3-e", "Advanced", "Einstein's theory of relativity revolutionized our understanding of space and time, showing the interplay between mass, energy, and gravity.")
    level26 = Level.create("3-f", "Advanced", "The intricacies of genetic code govern the blueprint of life, unraveling the mysteries of inheritance and evolution.")
    level27 = Level.create("3-g", "Advanced", "Nanotechnology manipulates matter at the molecular and atomic levels, opening doors to innovations with profound implications.")
    level28 = Level.create("3-h", "Advanced", "Dark matter and dark energy, constituting the majority of the cosmos, challenge physicists to decipher the enigma of the universe's composition.")
    level29 = Level.create("3-i", "Advanced", "The intersection of philosophy and quantum physics beckons us to ponder the nature of reality and the role of consciousness in shaping it.")
    level30 = Level.create("3-j", "Advanced", "Cryptocurrencies employ blockchain technology, disrupting traditional finance and ushering in a decentralized era of digital transactions.")

seed_database()
print("Seeded database")
