             DRIVER TRIPS TRACKER
            -----------------------

                    Classes:
                   ----------
        |------------------------------|
        |            Driver            |
        |------------------------------|
        | name:                 string |
        | trips:                list   |
        |------------------------------|
        | add_trip()                   |
        | sum_trip_info()              |
        | get_total_miles()            |
        | get_mph()                    |
        |------------------------------|


        |------------------------------|
        |            Trip              |
        |------------------------------|
        | name:                 string |
        | start_time:           string |
        | end_time:             string |
        | miles:                double |
        | time_delta:           double |
        | hours:                double |
        | mph:                  double |
        |------------------------------|
        | get_trip_info()              |
        | __get_time_delta()           |
        | __get_hours()                |
        |------------------------------|
        
        
                Design Reasoning:
               -------------------
               
        After looking at the raw text file, the two key objects were Drivers and their Trips.
        Because of this, I decided to use an object oriented approach and model two main classes as 
        Drivers and Trips. I organized the trips as a property of the Driver class so that the results 
        of the functions in the Trip class could be easily correlated to their respective Drivers. 
