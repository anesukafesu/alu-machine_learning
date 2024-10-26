#!/usr/bin/env python3
""" Implements sentientPlanets
"""
import requests


def sentientPlanets():
    """ Returns a list of names of all sentient planets.
    Args:
        None
    Returns:
        List: A list of names of all sentient planets.
    """
    next_url = 'https://swapi-api.alx-tools.com/api/species?page=1'
    home_planets = []

    while next_url is not None:
        response = requests.get(next_url)

        if response.status_code == 200:
            data = response.json()
            next_url = data['next']
            candidate_species = data['results']

            for species in candidate_species:
                if is_species_sentient(species):
                    homeworld_url = species['homeworld']

                    if homeworld_url:
                        homeworld = requests.get(homeworld_url).json()
                        home_planets.append(homeworld['name'])

        else:
            print("Error:", response.status_code)
            break

    return home_planets


def is_species_sentient(species):
    """ Determines if a species is sentient or not.
    Args:
        species (dict): The species whose sentience is to be
        determined.
    Returns:
        Boolean: True if the species is sentient.
        False if not.
    """
    return species['designation'] == 'sentient' or \
        species['classification'] == 'sentient'
