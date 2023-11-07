from models.__init__ import CONN, CURSOR
from models.team import Team
from models.players import Players

def seed_database():
    Team.drop_table()
    Team.create_table()
    Players.drop_table()
    Players.create_table()
    
    
    atlanta_hawks = Team("Atlanta Hawks", "Southeast").save()
    boston_celtics = Team("Boston Celtics", "Atlantic").save()
    brooklyn_nets = Team("Brooklyn Nets", "Atlantic").save()
    charlotte_hornets = Team("Charlotte Hornets", "Southeast").save()
    chicago_bulls = Team("Chicago Bulls", "Central").save()
    cleveland_cavaliers = Team("Cleveland Cavaliers", "Central").save()
    dallas_mavericks = Team("Dallas Mavericks", "Southwest").save()
    denver_nuggets = Team("Denver Nuggets", "Northwest").save()
    detroit_pistons = Team("Detroit Pistons", "Central").save()
    golden_state_warriors = Team("Golden State Warriors", "Pacific").save()
    houston_rockets = Team("Houston Rockets", "Southwest").save()
    indiana_pacers = Team("Indiana Pacers", "Central").save()
    la_clippers = Team("LA Clippers", "Pacific").save()
    los_angeles_lakers = Team("Los Angeles Lakers", "Pacific").save()
    memphis_grizzlies = Team("Memphis Grizzlies", "Southwest").save()
    miami_heat = Team("Miami Heat", "Southeast").save()
    milwaukee_bucks = Team("Milwaukee Bucks", "Central").save()
    minnesota_timberwolves = Team("Minnesota Timberwolves", "Northwest").save()
    new_orleans_pelicans = Team("New Orleans Pelicans", "Southwest").save()
    new_york_knicks = Team("New York Knicks", "Atlantic").save()
    oklahoma_city_thunder = Team("Oklahoma City Thunder", "Northwest").save()
    orlando_magic = Team("Orlando Magic", "Southeast").save()
    philadelphia_76ers = Team("Philadelphia 76ers", "Atlantic").save()
    phoenix_suns = Team("Phoenix Suns", "Pacific").save()
    portland_trail_blazers = Team("Portland Trail Blazers", "Northwest").save()
    sacramento_kings = Team("Sacramento Kings", "Pacific").save()
    san_antonio_spurs = Team("San Antonio Spurs", "Southwest").save()
    toronto_raptors = Team("Toronto Raptors", "Atlantic").save()
    utah_jazz = Team("Utah Jazz", "Northwest").save()
    washington_wizards = Team("Washington Wizards", "Southeast").save()
    

    jordan_poole = Players("Jordan Poole", washington_wizards).save()
    johnny_davis = Players("Johnny Davis", washington_wizards).save()
    jared_butler = Players("Jared Butler", washington_wizards).save()


seed_database()
print("Seeded database")