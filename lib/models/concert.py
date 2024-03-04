class Concert:
    all = []

    def __init__(self, name, date, band, city, ticket_cost):
        self.name = name
        self.date = date
        self.band = band
        self.city = city
        self.ticket_cost = ticket_cost  

        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date) > 0:
            self._date = date
        else:
            raise ValueError("Date must be a non-empty string")

    @property
    def ticket_cost(self):
        return self._ticket_cost

    @ticket_cost.setter
    def ticket_cost(self, ticket_cost):
        if isinstance(ticket_cost, dict):
            for ticket_type, details in ticket_cost.items():
                if not isinstance(ticket_type, str):
                    raise TypeError("Ticket type must be a string")
                if not (isinstance(details, list) and len(details) == 2):
                    raise TypeError("Details must be a list with two elements: cost and attendance")
                cost, attendance = details
                if not (isinstance(cost, (int, float)) and cost >= 0):
                    raise ValueError("Cost must be a non-negative number")
                if not (isinstance(attendance, int) and attendance >= 0):
                    raise ValueError("Attendance must be a non-negative integer")
            self._ticket_cost = ticket_cost
        else:
            raise TypeError("Ticket cost must be a dictionary")

        
        
         #concert band 
        #must be of type band
        #should be able ti change after the cocert is instantiated

    @property
    def band(self):
        return self._band

    @band.setter
    
    def band(self, band):
       from models.band import Band
       if isinstance(band, Band):
           self._band + band 
       else :
            raise Exception("Band must be an instrance of Band class!")
   
    def city(self, City):
       from models.City import City
       if isinstance(City, City):
           self._City = City
       else :
            raise Exception("Band must be an instrance of Band class!")
     

   

    
