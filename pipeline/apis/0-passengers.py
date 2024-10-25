#!/usr/bin/env python3
""" Implements availableShips
"""
import requests
import json


def availableShips(n_passengers):
    """ Function to get all available ships from SWAPI
    """
    next_url = "https://swapi-api.alx-tools.com/api/starships/?page=1"
    ships = []

    while not next_url is None:
        response = requests.get(next_url)

        if response.status_code == 200:
            data = json.loads(response.text)
            next_url = data['next']
            viable_ships = filter(lambda s: int(s['passengers']) > n_passengers, data['results'])
            ships.append(list(map(lambda s: s['name'], viable_ships)))

        else:
            print(f"Request failed with status code: {response.status_code}")
    
    return ships