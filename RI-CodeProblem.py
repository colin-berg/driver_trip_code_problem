"""
This program tracks driving history for people. 
"""

#imports 
import math
from Driver import Driver
from Trip import Trip

#function to read in a file, line by line into a nested list 
def read_data_into_list(file):
  driver_data = [[item.strip() for item in line.rstrip('\n').split()] for line in open(file, 'r')]
  return driver_data

# function to convert our nested list of data into a dictionary with key : value as 'Driver_name' : 'Driver Object'
def conv_dict(driver_data):
  driver_dict = {}
  for item in driver_data:
    driver_name = item[1]
    if len(item) == 2:
      driver_dict[driver_name] = Driver(driver_name)
    else:
      driver_dict[driver_name].add_trip(Trip(driver_name, item[2], item[3], item[4]))
      
  
 
      

  return driver_dict


#calling the read data function and conv_dict function 
driver_data = read_data_into_list('drivers.txt')

driver_dict_data = conv_dict(driver_data)

# sorting the items in driver_dict_data by total miles traveled, decending
sorted_driver_data = sorted(driver_dict_data.items(), key = lambda kv:kv[1].get_total_miles(), reverse=True)

# converting the sorted list items back into a dictionary for efficient parsing 
sorted_dict_driver_data = dict(sorted_driver_data)

for driver_name, driver in sorted_dict_driver_data.items(): 
  print(f"{driver_name}: {driver.get_total_miles()} miles {'' if driver.get_mph() == 0 else '@ ' + str(math.ceil(driver.get_mph())) + ' mph'} ")

    


     


  
















