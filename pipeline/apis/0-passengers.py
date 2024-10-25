#!/usr/bin/env python3
""" Implements availableShips
"""
import requests
import json


def availableShips(n_passengers):
    """ Function to get all available ships from SWAPI.
    Args:
        n_passengers: The number of passengers to be
        accommodated.
    Returns:
        list: A list of the names of ships that could be
        used.
    """
    next_url = "https://swapi-api.alx-tools.com/api/starships/?page=1"
    ships = []

    while next_url is not None:
        response = requests.get(next_url)

        if response.status_code == 200:
            data = json.loads(response.text)
            next_url = data['next']

            viable_ships = filter(lambda ship: is_suitable_ship(ship, n_passengers), data['results'])
            ships.append(list(map(lambda s: s['name'], viable_ships)))

        else:
            print(f"Request failed with status code: {response.status_code}")
            break

    return ships


def is_suitable_ship(ship, n_passengers):
    """ Function that decides if a ship is has enough
    capacity to carry a given number of passengers.

    Args:
        ship(dictionary): A dictionary containing the ship's
        information
        n_passengers (int): The number of passengers to be
        carried by the ship
    Returns:
        boolean: True if the ship is suitable. False if
        it is not suitable. 
    """
    max_passengers = ship['passengers']

    if max_passengers is not None:
        return int(max_passengers) > n_passengers
    else:
        return False
