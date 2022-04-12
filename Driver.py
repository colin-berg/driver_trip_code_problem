import math


class Driver:

    def __init__(self, name):
        self.name = name
        self.trips = []


    
  # adds a trip to the Driver object
    def add_trip(self, trip):
        self.trips.append(trip)

  # add function to summarize trip info 
    def sum_tripinfo(self):
        self.trips 

    # total miles traveled per trip 
    def get_total_miles(self):
        total_miles = 0
        if len(self.trips) == 0:
            return 0
        
        for trip in self.trips:
            total_miles += float(trip.miles)

        return math.floor(total_miles) 
    
    def get_mph(self):
        if len(self.trips) == 0:
            return 0
        total_hours = 0.
        for trip in self.trips:
            total_hours += trip.hours
            

        return self.get_total_miles() / total_hours
