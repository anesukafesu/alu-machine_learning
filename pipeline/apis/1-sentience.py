#!/usr/bin/env python3
""" Implements sentientPlanets
"""
import requests
import json

def sentientPlanets():
    """ Returns a list of names of all sentient planets.
    Args:
        None
    Returns:
        List: A list of names of all sentient planets.
    """
    next_url = 'https://swapi-api.alx-tools.com/api/planets?page=1'
    result = []

    while next_url is not None:
        response = requests.get(next_url)

        if response.status_code == 200:
            data = json.loads(response.text)
            next_url = data['next']
            candidate_planets = data['results']
            sentient_planets = filter(is_planet_sentient, candidate_planets)
            result.append(list(map(lambda p: p['name'], sentient_planets)))
        else:
            print("Error:", response.status_code)
            break
    
    return result


def is_planet_sentient(planet):
    """ Determines if a planet contains sentient life or not.
    Args:
        planet (dict): The planet whose sentience is to be
        determined.
    Returns:
        Boolean: True if the planet contains sentient life.
        False if not.
    """
    population = planet['population']

    if population is None:
        return False
    
    return int(population) > 0