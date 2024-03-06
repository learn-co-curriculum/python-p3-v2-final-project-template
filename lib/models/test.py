from band import Band
from city import City
from concert import Concert
from concert_band import ConcertBand
#gotta make Band.home_city use an object or key

City.drop_table()
Band.drop_table()
Concert.drop_table()
ConcertBand.drop_table()

City.create_table()
Band.create_table()
Concert.create_table()
ConcertBand.create_table()

tickets = {"four-day pass": [503, 1000], "friday pass": [424, 800]}
nyc = City.create("New York")
khaled = Band.create("DJ Khaled", ["Khaled Mohammed Khaled"], "Hip Hop", "New Orleans")
mos_def = Band.create("Mos Def", ["Dante Terrell Smith"], "Hip Hop", "New York")
jam = Concert.create("Jam Fest", "9/8/2010", ["DJ Khaled", "Mos Def"], "New York", tickets)
