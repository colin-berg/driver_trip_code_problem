from datetime import *


class Trip:

    def __init__(self, name, start_time, end_time, miles):
        self.name = name 
        self.start_time = start_time
        self.end_time = end_time
        self.miles = miles 
        self.timedelta = self.__get_timedelta()
        self.hours = self.__get_hours()
        self.mph = float(self.miles) / self.hours

    #public method(s)
    def get_trip_info(self):
        return self.start_time, self.end_time, self.miles, self.timedelta, self.hours, self.mph

    
    #private method(s)
    def __get_time_delta(self):
        start_time = datetime.strptime(self.start_time, "%H:%M")
        end_time = datetime.strptime(self.end_time, "%H:%M")
        return end_time - start_time
        
    def __get_hours(self):
        return self.timedelta.total_seconds() / 3600
        



    

