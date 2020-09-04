
import random

# CONSTANTS

DYNAMIC_LIST_NAME = "dynamic.txt"

#function for opening file and getting list
def get_list_from_file():
    with open(DYNAMIC_LIST_NAME, 'r') as in_file:
        available_stations = in_file.readlines()

    return available_stations

#function for replacing file with updated list
def replace_file_from_list(remaining_stations):
    with open(DYNAMIC_LIST_NAME, 'w') as out_file:
        out_file.writelines(remaining_stations)

    return

#function for randomly selecting index in list
def select_station_index(num_stations):
    return random.randint(0, num_stations - 1)

#function for determining whether element should be eliminated
def prompt_delete():
    print("delete station? (y/n)")
    choice = input()
    if choice == "y":
        return True
    else:
        return False

#function for eliminating element from list
def eliminate_station_from_index(index, stations):

    remaining_stations = []

    for i, station in enumerate(stations):
        if(i == index):
            continue
        remaining_stations.append(station)

    return remaining_stations

#main function
def get_station():

    stations = get_list_from_file()

    target_station_index = select_station_index(len(stations))

    print(stations[target_station_index])
    if prompt_delete():
        stations = eliminate_station_from_index(target_station_index, stations)

    replace_file_from_list(stations)

    return

get_station()




