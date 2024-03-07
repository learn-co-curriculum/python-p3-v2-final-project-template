from models.band import Band
from models.city import City
from models.concert import Concert
from models.concert_band import ConcertBand

def reseed():
    City.drop_table()
    Band.drop_table()
    Concert.drop_table()
    ConcertBand.drop_table()

    City.create_table()
    Band.create_table()
    Concert.create_table()
    ConcertBand.create_table()

    tickets = {"four-day pass": [503, 1000], "friday pass": [424, 800]}
    tickets2 = {"three-day pass": [480, 5000], "friday pass": [200, 4000]}
    nyc = City.create("New York")
    khaled = Band.create("DJ Khaled", ["Khaled Mohammed Khaled"], "Hip Hop", "New Orleans")
    mos_def = Band.create("Mos Def", ["Dante Terrell Smith"], "Hip Hop", "New York")
    metallica = Band.create("Metallica", ["James Hetfield", "Lars Ulrich", "Cliff Burton", "Jason Newsted"], "Thrash Metal", "Los Angeles")
    glass_animals = Band.create("Glass Animals", ["Dave Bayley", "Drew MacFarlane", "Edmund Irwin-Singer", "Joe Seaward"], "Indie Rock", "Oxford")
    jam = Concert.create("Jam Fest", "9/8/2010", ["DJ Khaled", "Mos Def"], "New York", tickets)
    ball = Concert.create("Mayor's Ball", "4/8/2025", [metallica, 1, "Glass Animals"], "International Waters", tickets2) # 1 will be the id of DJ Khaled

# import ipdb 
# ipdb.set_trace()